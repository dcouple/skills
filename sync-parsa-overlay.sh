#!/usr/bin/env bash
# Overlay parsa's personal set on top of a user-level orchestra install
# (dcouple/orchestra scripts/sync-user.sh runs first). Commutative with it:
# any name orchestra owns is installed here as p-<name>, never canonical, so
# the two syncs can run in any order without clobbering each other.
#
# Usage: sync-parsa-overlay.sh <path-to-orchestra-export-or-clone>
set -euo pipefail
REPO="$(cd "$(dirname "$0")" && pwd)"
ORCH="${1:?usage: sync-parsa-overlay.sh <path-to-orchestra-checkout>}"
sedi() { if sed --version >/dev/null 2>&1; then sed -i "$@"; else sed -i '' "$@"; fi; }

CS="$HOME/.claude/skills"; CA="$HOME/.claude/agents"; XS="$HOME/.codex/skills"
mkdir -p "$CS" "$CA" "$XS"

# materially-equivalent by charter — orchestra's copy wins, no p- clutter
SKIP_OVERLAP="excalidraw-pr-diagrams"

install_set() { # src-dir dest-dir orchestra-dir
  local src="$1" dest="$2" orch="$3" d name
  for d in "$src"/*/; do
    [ -f "$d/SKILL.md" ] || continue
    name="$(basename "$d")"
    if [ -d "$orch/$name" ]; then
      case " $SKIP_OVERLAP " in *" $name "*) echo "skip (equivalent): $name"; continue;; esac
      rm -rf "$dest/p-$name"
      cp -R "$d" "$dest/p-$name"
      [ -f "$dest/p-$name/SKILL.md" ] && sedi "s/^name: $name\$/name: p-$name/" "$dest/p-$name/SKILL.md"
      echo "overlap: $name → p-$name"
    else
      rsync -a "$d" "$dest/$name/"
    fi
  done
}

install_set "$REPO/parsa/.claude/skills" "$CS" "$ORCH/claude/skills"
install_set "$REPO/parsa/.codex/skills"  "$XS" "$ORCH/codex/skills"

for f in "$REPO"/parsa/.claude/agents/*.md; do
  name="$(basename "$f")"
  if [ -f "$ORCH/claude/agents/$name" ]; then
    cp "$f" "$CA/p-$name"
    base="${name%.md}"
    sedi "s/^name: $base\$/name: p-$base/" "$CA/p-$name"
    echo "overlap: agents/$name → p-$name"
  else
    rsync -a "$f" "$CA/$name"
  fi
done

for skill in "$REPO"/parsa/business/*/ "$REPO"/parsa/seo/*/; do
  [ -f "$skill/SKILL.md" ] && rsync -a "$skill" "$CS/$(basename "$skill")/"
done

# parsa's pipelines keep using parsa's reviewers via their p- twins
if [ -f "$CS/create-plan/SKILL.md" ] && [ -f "$CA/p-plan-reviewer.md" ]; then
  sedi 's/subagent_type: "plan-reviewer"/subagent_type: "p-plan-reviewer"/' "$CS/create-plan/SKILL.md"
fi
if [ -f "$XS/plan/SKILL.md" ] && [ -d "$XS/p-plan-reviewer" ]; then
  sedi 's/`plan-reviewer`/`p-plan-reviewer`/' "$XS/plan/SKILL.md"
fi

echo "parsa overlay complete."
