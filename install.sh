#!/usr/bin/env bash
# Install the Omarchy Ghostty themes into Ghostty's user theme directory.
#
#   ./install.sh                     # from a clone of this repo
#   curl -fsSL https://raw.githubusercontent.com/Mr-Sunglasses/ghostty-omarchy-themes/main/install.sh | bash

set -euo pipefail

REPO="Mr-Sunglasses/ghostty-omarchy-themes"
DEST="${XDG_CONFIG_HOME:-$HOME/.config}/ghostty/themes"

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" 2>/dev/null && pwd || true)"

if [[ -n $script_dir && -d $script_dir/themes ]]; then
  src="$script_dir/themes"
else
  tmp="$(mktemp -d)"
  trap 'rm -rf "$tmp"' EXIT
  echo "Downloading themes from github.com/$REPO..."
  curl -fsSL "https://github.com/$REPO/archive/refs/heads/main.tar.gz" | tar -xz -C "$tmp"
  src="$tmp/ghostty-omarchy-themes-main/themes"
fi

mkdir -p "$DEST"
cp "$src"/Omarchy* "$DEST"/

count=$(find "$src" -name 'Omarchy*' | wc -l | tr -d ' ')
echo "Installed $count themes to $DEST"
echo
echo "Add one to your Ghostty config (~/.config/ghostty/config), e.g.:"
echo "  theme = Omarchy Tokyo Night"
echo
echo "Then reload Ghostty (cmd+shift+, on macOS, ctrl+shift+, on Linux)."
