#!/usr/bin/env bash
# Sync one user's skill set into the user-level dirs.
# Usage: ./sync-merged.sh [parsa|tyler]  (default: parsa)
set -euo pipefail
REPO="$(cd "$(dirname "$0")" && pwd)"

USER="${1:-parsa}"

if [ ! -d "$REPO/$USER" ]; then
  echo "error: no directory $REPO/$USER" >&2
  echo "usage: sync-merged.sh [parsa|tyler]" >&2
  exit 1
fi

CLAUDE_SKILLS="$HOME/.claude/skills"
CLAUDE_AGENTS="$HOME/.claude/agents"
CODEX_SKILLS="$HOME/.codex/skills"
REFERENCES="$HOME/.references"
mkdir -p "$CLAUDE_SKILLS" "$CLAUDE_AGENTS" "$CODEX_SKILLS" "$REFERENCES"

# Sync the chosen user's set
[ -d "$REPO/$USER/.claude/skills" ] && rsync -a "$REPO/$USER/.claude/skills/" "$CLAUDE_SKILLS/"
[ -d "$REPO/$USER/.claude/agents" ] && rsync -a "$REPO/$USER/.claude/agents/" "$CLAUDE_AGENTS/"
[ -d "$REPO/$USER/.codex/skills" ]  && rsync -a "$REPO/$USER/.codex/skills/"  "$CODEX_SKILLS/"
[ -d "$REPO/$USER/references" ]     && rsync -a "$REPO/$USER/references/"     "$REFERENCES/"

# Business + seo suites (parsa-only, no-op for tyler)
for dir in business seo; do
  [ -d "$REPO/$USER/$dir" ] || continue
  for skill in "$REPO/$USER/$dir"/*/; do
    [ -f "$skill/SKILL.md" ] && rsync -a "$skill" "$CLAUDE_SKILLS/$(basename "$skill")/"
  done
done

echo "synced $USER's skills to user-level dirs."
