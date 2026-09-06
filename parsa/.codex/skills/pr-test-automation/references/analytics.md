# Analytics

## PostHog And Browser Analytics

PostHog JavaScript drops capture events from likely bots. Headless Playwright can still fetch PostHog config and run `identify`, while `capture` events are silently dropped because `navigator.webdriver` is `true`, the user agent looks automated, or `navigator.userAgentData.brands` includes `HeadlessChrome`.

When the explicit goal is to validate product analytics in local automation:

- Use a normal browser user agent.
- Mask only the automation bot signals for the test context. Setting `userAgent` is not enough if `navigator.userAgentData` still exposes headless Chrome:

```js
const context = await browser.newContext({
  userAgent:
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' +
    '(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
})

await context.addInitScript(() => {
  const brands = [
    { brand: 'Chromium', version: '125' },
    { brand: 'Google Chrome', version: '125' },
    { brand: 'Not.A/Brand', version: '24' },
  ]
  const fullVersionList = brands.map((brand) => ({
    ...brand,
    version: `${brand.version}.0.0.0`,
  }))

  Object.defineProperty(navigator, 'webdriver', { get: () => undefined })
  Object.defineProperty(navigator, 'userAgentData', {
    get: () => ({
      brands,
      mobile: false,
      platform: 'Windows',
      getHighEntropyValues: async () => ({
        brands,
        mobile: false,
        platform: 'Windows',
        architecture: 'x86',
        bitness: '64',
        model: '',
        uaFullVersion: '125.0.0.0',
        fullVersionList,
      }),
      toJSON: () => ({ brands, mobile: false, platform: 'Windows' }),
    }),
  })
})
```

- If the UI branches on OS or desktop/mobile, set the relevant platform signal intentionally and disclose it:

```js
await context.addInitScript(() => {
  Object.defineProperty(navigator, 'platform', { get: () => 'Win32' })
})
```

- Keep the page open long enough for PostHog batching, or trigger an unload only after waiting.
- Query PostHog for the unique marker. Do not treat `flags` or config requests as evidence that capture events were ingested.
- If event order looks wrong under automation, rerun with human-paced waits before treating it as a product bug.

## Multi-Surface Attribution Flows

Some PRs only work when a marketing site, API route, installer, desktop app, or mobile client is tested as one product flow. When attribution or install/download analytics cross those boundaries:

- Test companion PRs together in the worktree or preview environment that actually serves each surface.
- Validate route-level behavior directly before browser testing. For install/download flows, assert fresh tokens are accepted, stale or malformed tokens are dropped, invalid files or inputs are rejected, and crawler-facing routes are excluded when needed.
- Browser clipboard tests should compare visible UI text with clipboard text. It is common for the visible command/link to stay clean while the copied value includes a hidden `ref`, `utm`, or attribution token.
- If client-side analytics must create a distinct id but production capture is not part of the test, use a dummy public key and intercept analytics endpoints. If production verification is requested, use a unique marker and query the analytics project afterward.
- Use temporary app data directories for native app tests so config migrations, attribution files, cookies, and local databases do not touch the user's real profile.
- For Electron, Tauri, React Native, or similar native-shell mocks, event subscription APIs must return cleanup functions. Promise-returning mocks for `on*` or `subscribe*` APIs can create false crashes that look like product regressions.
- Direct captures that fire before an analytics SDK is fully initialized need explicit host, token, and distinct-id assertions. A request falling back to the SDK vendor default host before app config loads is usually a product bug, not enough evidence that the event will reach the intended project.
- Capture both the happy path and one negative path: accepted/refreshed attribution, stale or malformed attribution, user opt-in or opt-out, and any server-side invalid-input analytics.

## Analytics Identity Verification

Event ingestion alone is not enough — verify PERSON STITCHING whenever a PR touches
analytics, signup, login, or session handling:

- Group verification queries by `person_id`, never by `person.properties.*` — event-time
  person properties differ per row and can make N merged users each look like "one clean
  person". Six merged QA users passed an email-grouped check; a `person_id`-grouped check
  exposed they were all a single person.
- Inspect raw `distinct_id` per event when stitching looks wrong — it names the exact
  identity that captured the event and usually identifies the merge vector directly.
- When the PR touches identity stitching itself (aliasing, identify calls, distinct-id or
  session-identity plumbing) — or the product targets shared devices — run a
  **multi-user same-browser pass**: several signups and login switches in one browser
  profile, then assert each user resolved to a separate person AND that functional session
  state (websocket auth, cookies) followed the switch. Shared-machine bugs (identity
  merges, stale-socket auth) are invisible to single-user passes; the pass is expensive,
  so reserve it for changes where that failure mode is actually in play.
- Suspect STACKED causes when a fix's re-verification still fails: fix one vector, re-run
  the proof, and let the raw distinct_id data name the next vector. Do not assume the fix
  simply "didn't work".
- Test events fired immediately before hard navigations (checkout redirects, external
  scheduling links): SDK batching silently drops them on unload; they need per-capture
  `sendBeacon` transport. Absence in the warehouse — not the network tab — is the proof.
