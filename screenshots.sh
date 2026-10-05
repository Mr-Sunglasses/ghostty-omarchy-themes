#!/bin/bash
# Retake screenshots/<slug>.png for every theme in themes/ (macOS only).
#
# Opens a fresh Ghostty window per theme (ignoring your own config), prints the
# same sample output in each, captures the window and closes it. Needs Ghostty,
# Xcode command line tools (swiftc) and Screen Recording permission for the
# terminal you run this from.
#
#   ./screenshots.sh                 # all themes
#   ./screenshots.sh "Tokyo Night"   # only themes whose name contains this
set -euo pipefail

ROOT=$(cd "$(dirname "$0")" && pwd)
WORK=$(mktemp -d)
trap 'rm -rf "$WORK"' EXIT

# Finds a Ghostty window by title and prints "<window id> <pid>".
cat >"$WORK/winid.swift" <<'EOF'
import CoreGraphics
let title = CommandLine.arguments[1]
let list = CGWindowListCopyWindowInfo([.optionOnScreenOnly], kCGNullWindowID) as! [[String: Any]]
for w in list where (w[kCGWindowOwnerName as String] as? String) == "Ghostty" {
    if (w[kCGWindowName as String] as? String) == title {
        print(w[kCGWindowNumber as String]!, w[kCGWindowOwnerPID as String]!)
    }
}
EOF
swiftc -O "$WORK/winid.swift" -o "$WORK/winid"

# Sample output shown in every screenshot.
cat >"$WORK/demo.sh" <<'EOF'
#!/bin/bash
E=$'\e'; R="$E[0m"; B="$E[1m"
p() { printf '%s\n' "$1"; }
printf '\e[?25l'; clear
p "${B}$E[34m~/code/omarchy$R on $E[35m main$R $E[33m!2$R"
p "$E[32m❯$R ls"
p "${B}$E[34mbin$R  ${B}$E[34mconfig$R  ${B}$E[34mthemes$R  $E[32minstall.sh$R  README.md  $E[36mlogo.svg$R  ${B}$E[31mbackup.tar.gz$R"
p ""
p "$E[32m❯$R git diff --stat && git log --oneline -3"
p " themes/tokyo-night.toml | 6 $E[32m++++$E[31m--$R"
p " install.sh              | 2 $E[32m+$E[31m-$R"
p "$E[33m4f2a91c$R ($E[36mHEAD -> $E[32mmain$R) Add new theme"
p "$E[33mb81e0d7$R Tune ${B}palette$R contrast"
p "$E[33m03cc5e2$R $E[90mInitial commit$R"
p ""
p "$E[32m❯$R cat hello.py"
p "$E[35mdef$R $E[34mgreet$R(name: $E[33mstr$R) -> $E[33mstr$R:"
p "    $E[90m# say hello to the world$R"
p "    $E[35mreturn$R $E[32mf\"Hello, {name}!\"$R"
p ""
p "$E[32m❯$R palette"
line=""; for i in 0 1 2 3 4 5 6 7; do line+="$E[4${i}m     $R"; done; p " $line"
line=""; for i in 0 1 2 3 4 5 6 7; do line+="$E[10${i}m     $R"; done; p " $line"
p " $E[31mred$R $E[32mgreen$R $E[33myellow$R $E[34mblue$R $E[35mmagenta$R $E[36mcyan$R $E[37mwhite$R $E[90mgray$R"
p ""
printf '%s' "$E[32m❯$R $E[7m $R"
sleep 600
EOF
chmod +x "$WORK/demo.sh"

mkdir -p "$ROOT/screenshots"
for theme in "$ROOT"/themes/Omarchy*; do
    name=$(basename "$theme")
    [[ $name == *"${1:-}"* ]] || continue
    slug=$(sed -n "s/.*Omarchy theme '\([^']*\)'.*/\1/p" "$theme")
    open -na Ghostty.app --args --config-default-files=false --theme="$theme" \
        --title="$name" --font-size=14 --window-width=78 --window-height=21 \
        --window-padding-x=14 --window-padding-y=10 --background-opacity=1 \
        --window-save-state=never --confirm-close-surface=false \
        --quit-after-last-window-closed=true --macos-icon=official \
        --command="$WORK/demo.sh"
    wid=""
    for _ in $(seq 1 40); do
        read -r wid pid < <("$WORK/winid" "$name") || true
        [ -n "$wid" ] && break
        sleep 0.25
    done
    if [ -z "$wid" ]; then
        echo "no window for $name" >&2
        continue
    fi
    sleep 1.5
    screencapture -x -o -l "$wid" "$ROOT/screenshots/$slug.png"
    kill "$pid"
    echo "$name -> screenshots/$slug.png"
    sleep 0.5
done
