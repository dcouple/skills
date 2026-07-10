# Draft a work item — shared mechanics

Used by `/create-feature`, `/create-epic`, and `/create-issue` when writing
`./tmp/<id>/item.md`. The calling skill supplies the document template (from
its own `references/` directory) and any type-specific content rules.

- Check `./tmp/discussions/` for a decision log from the conversation that
  produced this item (match by slug and date). Carry its decisions and
  constraints into the item's locked directions rather than re-deriving
  them; link it from `refs/` if it holds more than the item should inline.
- Pick `<id>`: short kebab-case slug from the title. Create `./tmp/<id>/`.
- Write `item.md` following the caller's template. A template is a skeleton
  plus authoring notes: emit the filled-in frontmatter and body only — the
  "— format" title line and the backtick-quoted guidance are notes to you,
  not part of the document.
- Embed verification criteria per `~/.references/verification-criteria.md`:
  EARS-style, numbered `AC1…`, each mapped to a method from
  `~/.references/verification-methods.md` and matched to the change type's
  rubric in `~/.references/rubrics/`. No "works correctly".
- Keep it LEAN: `/do` starts fresh and is capable — omit anything it can
  reasonably decide itself.
- Save transcript-worthy raw material (key discussion excerpts, mock-ups,
  links, research worth keeping) to `./tmp/<id>/refs/` and link from the
  item — never inline.
- Leave `status: draft` until publish.
