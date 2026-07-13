#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

copy_agents() {
  local src="$1"
  local dst="$2"
  mkdir -p "$dst"
  cp -f "$src"/* "$dst"/
  printf 'Installed %s -> %s\n' "$src" "$dst"
}

copy_agents "$ROOT/.claude/agents" "$HOME/.claude/agents"
copy_agents "$ROOT/.codex/agents" "$HOME/.codex/agents"
copy_agents "$ROOT/.cursor/agents" "$HOME/.cursor/agents"
copy_agents "$ROOT/.opencode/agents" "$HOME/.config/opencode/agents"

printf '\nInstalled the Organization Agent Swarm at user scope.\n'
