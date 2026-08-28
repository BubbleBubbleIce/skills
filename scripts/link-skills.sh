#!/usr/bin/env bash
# Link this repo's skills into ~/.agents/skills so Codex / other agents
# pick up edits immediately. Per-skill symlinks (not the whole repo):
# ~/.agents/skills also holds third-party skills that are not in this repo.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${AGENTS_SKILLS_DIR:-$HOME/.agents/skills}"
BACKUP_ROOT="${AGENTS_SKILLS_BACKUP:-$HOME/.agents/skills-backup}"
MODE="safe" # safe | force | adopt

usage() {
  cat <<'EOF'
Usage: scripts/link-skills.sh [--force | --adopt-agents]

Link each skill in this repo to ~/.agents/skills/<name>.

  (default)         Link missing skills. Replace identical copies with
                    symlinks. Leave diverged copies untouched and report them.
  --force           Backup diverged ~/.agents/skills copies, then point at
                    this repo (repo wins).
  --adopt-agents    Copy diverged ~/.agents/skills copies back into this
                    repo, then symlink (agents copy wins, then stays in sync).

Environment:
  AGENTS_SKILLS_DIR      default: ~/.agents/skills
  AGENTS_SKILLS_BACKUP   default: ~/.agents/skills-backup
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --force) MODE="force"; shift ;;
    --adopt-agents) MODE="adopt"; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "unknown argument: $1" >&2; usage >&2; exit 2 ;;
  esac
done

mkdir -p "$DEST"

# Print: dest_name<TAB>abs_src_path
discover_skills() {
  local dir name nested
  for dir in "$REPO_ROOT"/*/; do
    [[ -d "$dir" ]] || continue
    name="$(basename "$dir")"
    case "$name" in
      scripts|.git|.cursor) continue ;;
    esac
    if [[ -f "${dir}SKILL.md" ]]; then
      printf '%s\t%s\n' "$name" "$(cd "$dir" && pwd)"
      continue
    fi
    for nested in "$dir"*/; do
      [[ -d "$nested" && -f "${nested}SKILL.md" ]] || continue
      printf '%s\t%s\n' "$(basename "$nested")" "$(cd "$nested" && pwd)"
    done
  done
}

same_tree() {
  diff -rq "$1" "$2" >/dev/null 2>&1
}

backup_dir() {
  local src="$1" name="$2"
  local stamp dest
  stamp="$(date +%Y%m%d-%H%M%S)"
  dest="$BACKUP_ROOT/${name}-${stamp}"
  mkdir -p "$BACKUP_ROOT"
  cp -a "$src" "$dest"
  printf '%s\n' "$dest"
}

link_one() {
  local name="$1" src="$2" dest="$DEST/$name"

  if [[ -L "$dest" ]]; then
    local current
    current="$(readlink "$dest")"
    if [[ "$current" == "$src" ]]; then
      printf 'ok      %s\n' "$name"
      return 0
    fi
    ln -sfn "$src" "$dest"
    printf 'relink  %s  (%s -> %s)\n' "$name" "$current" "$src"
    return 0
  fi

  if [[ ! -e "$dest" ]]; then
    ln -s "$src" "$dest"
    printf 'link    %s\n' "$name"
    return 0
  fi

  if [[ ! -d "$dest" ]]; then
    printf 'skip    %s  (not a directory: %s)\n' "$name" "$dest" >&2
    return 1
  fi

  if same_tree "$src" "$dest"; then
    rm -rf "$dest"
    ln -s "$src" "$dest"
    printf 'replace %s  (identical copy -> symlink)\n' "$name"
    return 0
  fi

  case "$MODE" in
    safe)
      printf 'diverge %s  (repo and ~/.agents/skills differ; pass --force or --adopt-agents)\n' "$name"
      return 0
      ;;
    force)
      local bak
      bak="$(backup_dir "$dest" "$name")"
      rm -rf "$dest"
      ln -s "$src" "$dest"
      printf 'force   %s  (backup %s)\n' "$name" "$bak"
      return 0
      ;;
    adopt)
      local bak
      bak="$(backup_dir "$dest" "$name")"
      rsync -a --delete --exclude .git "$dest"/ "$src"/
      rm -rf "$dest"
      ln -s "$src" "$dest"
      printf 'adopt   %s  (copied agents -> repo; backup %s)\n' "$name" "$bak"
      return 0
      ;;
  esac
}

status=0
while IFS=$'\t' read -r name src; do
  [[ -n "$name" ]] || continue
  if ! link_one "$name" "$src"; then
    status=1
  fi
done < <(discover_skills)

exit "$status"
