#!/usr/bin/env bash
# Merged sync: install parsa's AND tyler's sets into the user-level dirs.
#
# Collision policy: tyler's names win (his /discussion → /create-* → /do flow
# stays canonical); parsa's collided originals are preserved under a `p-`
# prefix (e.g. /p-discussion) so both remain invocable. Collisions are
# detected dynamically — nothing here to update when either set grows.
#
# Run from anywhere: ./sync-merged.sh
set -euo pipefail
REPO="$(cd "$(dirname "$0")" && pwd)"

CLAUDE_SKILLS="$HOME/.claude/skills"
CLAUDE_AGENTS="$HOME/.claude/agents"
CODEX_SKILLS="$HOME/.codex/skills"
REFERENCES="$HOME/.references"
mkdir -p "$CLAUDE_SKILLS" "$CLAUDE_AGENTS" "$CODEX_SKILLS" "$REFERENCES"

# portable in-place sed (macOS/BSD vs GNU)
sedi() { if sed --version >/dev/null 2>&1; then sed -i "$@"; else sed -i '' "$@"; fi; }

# --- 1. parsa first, tyler second: tyler wins name collisions -------------
rsync -a "$REPO/parsa/.claude/skills/" "$CLAUDE_SKILLS/"
rsync -a "$REPO/parsa/.claude/agents/" "$CLAUDE_AGENTS/"
rsync -a "$REPO/parsa/.codex/skills/"  "$CODEX_SKILLS/"
rsync -a "$REPO/tyler/.claude/skills/" "$CLAUDE_SKILLS/"
rsync -a "$REPO/tyler/.claude/agents/" "$CLAUDE_AGENTS/"
rsync -a "$REPO/tyler/.codex/skills/"  "$CODEX_SKILLS/"
rsync -a "$REPO/tyler/references/"     "$REFERENCES/"

# --- 2. business + seo suites (parsa-only, no collisions) -----------------
for skill in "$REPO"/parsa/business/*/ "$REPO"/parsa/seo/*/; do
  [ -f "$skill/SKILL.md" ] && cp -r "$skill" "$CLAUDE_SKILLS/$(basename "$skill")"
done

# --- 3. preserve parsa's collided originals under p- ----------------------
# skills (dirs) and codex skills
for pair in ".claude/skills:$CLAUDE_SKILLS" ".codex/skills:$CODEX_SKILLS"; do
  sub="${pair%%:*}" dest="${pair##*:}"
  for name in $(comm -12 <(ls "$REPO/parsa/$sub" | sort) <(ls "$REPO/tyler/$sub" | sort)); do
    rm -rf "$dest/p-$name"
    cp -r "$REPO/parsa/$sub/$name" "$dest/p-$name"
    [ -f "$dest/p-$name/SKILL.md" ] && sedi "s/^name: $name\$/name: p-$name/" "$dest/p-$name/SKILL.md"
    echo "collision: $sub/$name → tyler's; parsa's kept as p-$name"
  done
done
# agents (flat .md files)
for f in $(comm -12 <(ls "$REPO/parsa/.claude/agents" | sort) <(ls "$REPO/tyler/.claude/agents" | sort)); do
  name="${f%.md}"
  cp "$REPO/parsa/.claude/agents/$f" "$CLAUDE_AGENTS/p-$f"
  sedi "s/^name: $name\$/name: p-$name/" "$CLAUDE_AGENTS/p-$f"
  echo "collision: agents/$f → tyler's; parsa's kept as p-$f"
done

# --- 4. re-wire parsa skills to their p- dependencies ---------------------
# create-plan spawns parsa's plan-reviewer, which now lives at p-plan-reviewer
if [ -f "$CLAUDE_SKILLS/create-plan/SKILL.md" ] && [ -f "$CLAUDE_AGENTS/p-plan-reviewer.md" ]; then
  sedi 's/subagent_type: "plan-reviewer"/subagent_type: "p-plan-reviewer"/' "$CLAUDE_SKILLS/create-plan/SKILL.md"
fi

echo "merged sync complete."
