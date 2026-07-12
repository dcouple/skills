#!/usr/bin/env bash
# Sync: install parsa's set into the user-level dirs.
#
# Tyler's set ("Orchestra") moved to https://github.com/dcouple/orchestra
# and no longer installs to user-level dirs — it syncs one-way into each
# consumer repo (.claude/, .codex/, .references/) via that repo's workflow.
# The old merged install (tyler-wins collision policy, p- prefixes) is gone
# with it; this script now installs parsa's set under its own names.
#
# Run from anywhere: ./sync-merged.sh
set -euo pipefail
REPO="$(cd "$(dirname "$0")" && pwd)"

CLAUDE_SKILLS="$HOME/.claude/skills"
CLAUDE_AGENTS="$HOME/.claude/agents"
CODEX_SKILLS="$HOME/.codex/skills"
mkdir -p "$CLAUDE_SKILLS" "$CLAUDE_AGENTS" "$CODEX_SKILLS"

rsync -a "$REPO/parsa/.claude/skills/" "$CLAUDE_SKILLS/"
rsync -a "$REPO/parsa/.claude/agents/" "$CLAUDE_AGENTS/"
rsync -a "$REPO/parsa/.codex/skills/"  "$CODEX_SKILLS/"

# business + seo suites
for skill in "$REPO"/parsa/business/*/ "$REPO"/parsa/seo/*/; do
  # rsync, not cp -r: cp into an existing dir nests a copy inside it on rerun
  [ -f "$skill/SKILL.md" ] && rsync -a "$skill" "$CLAUDE_SKILLS/$(basename "$skill")/"
done

echo "sync complete (parsa's set)."
echo "note: previously-installed tyler skills / p- copies are not removed;"
echo "prune stale ones by hand if you no longer want them."
