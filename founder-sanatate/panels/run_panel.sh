#!/usr/bin/env bash
# Rulează panelul de cumpărători founder-consumer cu sub-agenți independenți (claude -p, fără unelte).
# Fiecare cumpărător primește brieful lui (scris de panel.py) + același sufix pentru toți (uniform_suffix.txt).
# Răspunsul propriu al cumpărătorului e salvat cu `panel.py save` (calea de rezervă din SKILL.md).
# usage: run_panel.sh <panel_dir> [model] [parallel]
set -u
DIR="$1"; MODEL="${2:-sonnet}"; PAR="${3:-10}"
HERE="$(cd "$(dirname "$0")" && pwd)"
TOOL="/tmp/claude-0/-home-user-Research/443ae51e-6356-5470-b8f1-0cb21e6eb50e/scratchpad/ext/founder-skill/skills/founder-consumer/panel.py"
NEUTRAL="/tmp/claude-0/-home-user-Research/443ae51e-6356-5470-b8f1-0cb21e6eb50e/scratchpad/neutral"
mkdir -p "$DIR/raw" "$NEUTRAL"
python3 -I "$TOOL" --dir "$DIR" prompts >/dev/null
todo=$(python3 -I "$TOOL" --dir "$DIR" check | awk -F: '{print $1}')
export DIR MODEL HERE TOOL NEUTRAL
run_one() {
  id="$1"
  ( cd "$NEUTRAL" && cat "$DIR/briefs/$id.md" "$HERE/uniform_suffix.txt" | \
    timeout 300 claude -p --model "$MODEL" --tools "" --no-session-persistence --strict-mcp-config ) > "$DIR/raw/$id.txt" 2>"$DIR/raw/$id.err"
  python3 -I "$TOOL" --dir "$DIR" save "$id" < "$DIR/raw/$id.txt" >/dev/null 2>>"$DIR/raw/$id.err" && echo "$id ok" || echo "$id FAILED"
}
export -f run_one
printf '%s\n' $todo | xargs -P "$PAR" -I{} bash -c 'run_one {}'
python3 -I "$TOOL" --dir "$DIR" check || true
