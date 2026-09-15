# Publish a PR visual

Use only when asset publication and PR updates are authorized. Keep sensitive data out of public images and manifests.

## Durable destination

- Prefer a repository-owned, published, mutable, long-lived release such as `pr-assets`; inspect the actual release and permissions first.
- Creating a release needs a separate exact grant, for example `{"action":"create_release","repo":"owner/name","tag":"pr-assets"}`. PR/comment/upload authority does not imply release-creation authority.
- When explicitly authorized to create it, target the default branch, set `--latest=false`, and describe its long-lived asset purpose. Do not create one release per PR.
- If publication is unavailable or unauthorized, retain the source/render in Grain when connected or local storage otherwise; provide the prepared commands and Markdown and report the blocker. Do not switch to an arbitrary temporary host.

## Upload and verify

1. Compute the PNG SHA-256 and size. Use a portable name such as `pr-<number>-<head-short-sha>-<content-sha12>-visual-overview.png`, or a branch slug before PR creation.
2. Inspect existing assets. Reuse only when the existing digest or downloaded bytes match; use a longer digest/deterministic suffix for different content. Never use `--clobber`.
3. After upload/reuse, read back the release and asset: repository, tag, non-draft state, uploaded state, name, size, digest where available, and browser URL.
4. GET the bytes, with authentication for private assets. Compare hash/size and decode or inspect image magic; an HTML error page is not an image.

Record `pr-assets-manifest.json` with repository, release tag/URL, PR number, head commit, source/render paths, asset name, SHA-256, size, API/browser URLs, upload-or-reuse status, timestamp, and content-verification result. Save it with the task's shared artifacts; never include credentials.

## Update the PR

- Embed the verified image in `## Visual Overview`, bounded by `<!-- pr-visual-overview:start -->` and `<!-- pr-visual-overview:end -->`.
- Preserve author-owned text. Replace only the marked section; for a broken image outside markers, change only the confirmed asset URL.
- Use a body file or structured API payload so Markdown is data, not shell syntax.
- Read back the PR body and verify image access and formatting. A successful upload alone is not a completed handoff.
- Avoid redundant diagrams unless the user requested another format.

Track assets in the repository only when requested or required by tracked documentation. Use the project's asset location and stable links; do not silently commit temporary PR files.
