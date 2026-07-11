# Postmortem — format

> Produced by `/postmortem` after `/do` finishes and the human reviews the PR, when the
> result fell short of intent. Saved as `./tmp/<id>/postmortem.md` (local for now).
> The point is **compound learning**: fix the root cause in *our system* (skill / agent /
> template / criteria), so the same gap can't recur.

---
```yaml
---
type: postmortem
item: <id>
pr: <url or #>
---
```

# Postmortem — `<item>`

## What we asked for
`<the intent + desired end state, briefly>`

## What `/do` delivered vs intended
`<the gap the human found on PR review — concrete>`

## Why the gap happened
`<root cause in OUR system, not just the code: was it a thin ticket? a weak verification`
`criterion? a review blind spot? a missing architecture direction?>`

## What to change so it doesn't recur
`<a concrete improvement to a specific skill / sub-agent / template / verification block>`

## System change (deferred)
`<future: open a GitHub issue against dcouple/skills carrying this note. Off for now.>`
