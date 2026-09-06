# Publishing

## Durable PR QA Descriptions, Comments, And Screenshots

When testing an open PR, preserve the result where reviewers will look first:

- Create a local artifact folder such as `tmp/pr-<number>-qa/` containing raw screenshots, scripts, the exact PR Markdown, and `pr-assets-manifest.json`.
- Classify every image before upload. Do not upload PHI, secrets, private customer data, real inbox contents, payment details, MFA codes, production admin data, or anything inappropriate for every person who can read the PR. Keep sensitive images local and redact a copy only when the redaction can be verified visually.
- Prefer a repository-owned durable surface. For GitHub PRs, discover and reuse a published, mutable, long-lived release such as `pr-assets` or the repository's documented equivalent:

  ```bash
  repo="$(gh repo view --json nameWithOwner --jq .nameWithOwner)"
  default_branch="$(gh repo view --json defaultBranchRef --jq .defaultBranchRef.name)"
  gh release list -R "$repo" --limit 100 \
    --json tagName,name,isDraft,isPrerelease
  gh release view pr-assets -R "$repo" \
    --json tagName,isDraft,isPrerelease,isImmutable,url,assets
  ```

  Do not create a release per PR. Do not use an arbitrary temporary host when a suitable repository release exists.
- If no suitable release exists, creating one dedicated long-lived `pr-assets` release is a separate hard stop requiring an exact grant such as `{"action":"create_release","repo":"owner/name","tag":"pr-assets"}`. Generic GitHub, PR, comment, or asset-upload authorization does not grant creation. Use the default branch as its target and keep it out of Latest-release semantics:

  ```bash
  gh release create pr-assets -R "$repo" --title "PR assets" \
    --notes "Long-lived image assets for pull requests and QA evidence." \
    --latest=false --target "$default_branch"
  ```

  If release creation or upload is not authorized, do not fall back to a temporary host. Write the intended filenames, manifest, exact `gh release create` / `gh release upload` commands, and ready-to-paste marked PR Markdown into the artifact folder; report that durable publication is blocked.
- Compute the source SHA-256 before upload. Name every asset with stable context plus content identity, for example `pr-<number>-<head-short-sha>-<content-sha12>-<step>.png`. Use a branch slug when the PR number does not exist yet. Sanitize names to portable lowercase ASCII.
- Make reruns idempotent. Inspect release assets before uploading. If the exact name exists and its GitHub digest-or a downloaded byte-for-byte hash when no digest is present-matches the local file, reuse its URL. If the content differs, do not overwrite or use `gh release upload --clobber`; extend the hash or add a deterministic suffix and upload a new asset so an older PR never changes underneath reviewers.
- Upload with `gh release upload <tag> <path> -R "$repo"`, then read back the release and asset metadata. Require the intended tag, a non-draft release, uploaded asset state, expected filename, size, SHA-256 digest when GitHub supplies it, and `browser_download_url`.
- Perform a direct GET of the uploaded bytes (authenticated through GitHub for private repositories), not only a HEAD request. Compare the downloaded SHA-256 and size with the local source and verify the decoded file type or image magic; an HTML login/error page with a misleading status is a failure. Record the verification timestamp and result.
- Maintain `pr-assets-manifest.json` across reruns. For each asset record the repository, release tag and URL, PR number, head commit, source path, semantic step, asset name, local SHA-256 and size, asset API URL, browser download URL, upload-or-reuse status, timestamp, and content-verification result. Never put tokens, cookies, or sensitive test data in the manifest.
- Treat the PR description as the primary review surface. Append or replace only the section between `<!-- pr-test-automation-summary:start -->` and `<!-- pr-test-automation-summary:end -->` without rewriting the human-authored PR summary. If a legacy `<!-- codex-pr-test-automation-summary -->` section exists, migrate that section once instead of duplicating it. Keep the PR description QA section compact and include:
  - current QA status;
  - test account/org/marker identifiers;
  - user journeys and surface areas tested;
  - key external evidence IDs, such as Stripe subscription IDs, email IDs, PostHog event names, webhook IDs, or database readback;
  - key screenshot previews when UI review is central and the set is small enough to skim;
  - a link to the detailed QA comment or local artifacts when the full evidence is long;
  - what remains for human review and what was intentionally skipped.
- Post or update one PR comment whose owned content is bounded by `<!-- pr-test-automation-detail:start -->` and `<!-- pr-test-automation-detail:end -->` when detailed evidence, logs, or screenshot galleries are too large for the PR description. Recognize the legacy `<!-- codex-pr-test-automation -->` marker so reruns update rather than duplicate an older comment. Include:
  - summary of automated manual QA outcome;
  - test account/org/marker identifiers;
  - user journeys and surface areas tested;
  - screenshot previews, not just screenshot links;
  - connector/provider evidence such as PostHog, Stripe, email, SMS, logs, or database readback;
  - what remains for human review and what was intentionally skipped.
- Render safe uploaded screenshots inline so reviewers can skim without opening every link. Do not leave the PR description or QA comment as a plain list of screenshot URLs when UI changed.
- Prefer grouped preview galleries:
  - Use one `<details open>` section per user journey or touched UI surface when there are many screenshots.
  - Put screenshots in chronological order and label each one with the journey step and state it proves.
  - Add a one-sentence explanation for each screenshot that answers: what surface/state is this, and what should the reviewer notice?
  - Use a two-column Markdown/HTML table for compact skimming when there are more than four screenshots.
  - Use direct image URLs in Markdown image syntax or HTML `<img>` tags. If using HTML, constrain width around `360`-`480` pixels so the PR remains readable.
- Keep unsafe screenshots local only and say why. Examples: payment card entry screens, PHI, secrets, private customer data, real inbox contents, MFA codes, or production admin data. Mention their local paths without rendering or uploading them.
- When updating an existing marked QA summary or comment, replace dead, expiring, temporary, or local-only image references with verified durable URLs and inline previews during the same update instead of adding a second comment. Preserve all author-written text outside the markers. If an image URL outside a marker is broken, change only that URL after verifying the intended replacement; do not rewrite the surrounding prose.
- Example compact preview block:

```markdown
<details open>
<summary>Signup journey screenshots</summary>

| Step | Preview |
| --- | --- |
| Account details | Shows the default account form before submission; reviewer should check required fields and spacing.<br><img src="https://example.test/01-account.png" width="420" alt="Account details form"> |
| Validation error | Shows the blocked submit state; reviewer should check copy, focus, and error placement.<br><img src="https://example.test/02-validation.png" width="420" alt="Validation error state"> |

</details>
```
- If PR commenting is not authorized or a connector is unavailable, write the exact Markdown comment body into the artifact folder and report the path.
