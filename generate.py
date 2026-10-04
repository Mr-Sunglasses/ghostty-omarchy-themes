#!/usr/bin/env python3
"""Port Omarchy themes to Ghostty theme files.

Reads each theme's colors.toml from an Omarchy checkout, resolves the palette
with the same alias/fallback cascade as Omarchy's bin/omarchy-theme-color, and
renders Omarchy's own default/themed/ghostty.conf.tpl into themes/. Each theme
also sets a matching macOS app icon and split divider color (see extras()).

Usage: ./generate.py [path-to-omarchy-checkout]
       (clones https://github.com/omacom/omarchy into a temp dir if omitted)
"""

import re
import subprocess
import sys
import tempfile
import tomllib
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent / "themes"
PREVIEW_DIR = Path(__file__).resolve().parent / "previews"
REPO = "https://github.com/omacom/omarchy"

# Display names where title-casing the directory name isn't right.
NAME_OVERRIDES = {
    "catppuccin": "Catppuccin Mocha",
    "catppuccin-latte": "Catppuccin Latte",
    "retro-82": "Retro 82",
    "rose-pine": "Rose Pine Dawn",
}


def mix(start, end, amount):
    s = [int(start[i : i + 2], 16) for i in (1, 3, 5)]
    e = [int(end[i : i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{int(a * (1 - amount) + b * amount + 0.5):02x}" for a, b in zip(s, e))


def resolve(raw):
    """Mirror resolve_theme_colors() from bin/omarchy-theme-color."""
    c = {k: str(v) for k, v in raw.items()}

    def alias(key, fallback):
        if not c.get(key) and c.get(fallback):
            c[key] = c[fallback]

    for key, short in {
        "background": "bg",
        "dark_background": "dark_bg",
        "darker_background": "darker_bg",
        "lighter_background": "lighter_bg",
        "foreground": "fg",
        "dark_foreground": "dark_fg",
        "light_foreground": "light_fg",
        "bright_foreground": "bright_fg",
    }.items():
        alias(key, short)

    alias("background", "color0")
    alias("foreground", "color7")
    if c.get("background"):
        c["color0"] = c["background"]
    if c.get("foreground"):
        c["color7"] = c["foreground"]

    for name, n in [("red", 1), ("green", 2), ("yellow", 3), ("blue", 4), ("magenta", 5), ("cyan", 6)]:
        alias(name, f"color{n}")
        alias(f"bright_{name}", f"color{n + 8}")
    alias("magenta", "purple")
    alias("bright_magenta", "bright_purple")

    c.setdefault("bright_foreground", c.get("color15") or c["foreground"])
    c.setdefault("dark_foreground", c.get("color8") or c["foreground"])
    c.setdefault("muted", c.get("color8") or c["dark_foreground"])
    c.setdefault("selection", c.get("selection_background") or c.get("color8") or c.get("color0") or c["background"])
    c.setdefault("selection_background", c["selection"])
    c.setdefault("selection_foreground", c["bright_foreground"])

    for name in ("red", "yellow", "green", "cyan", "blue", "magenta"):
        if not c.get(f"bright_{name}"):
            c[f"bright_{name}"] = mix(c[name], "#ffffff", 0.20)
    return c


def render(template, colors, name):
    def sub(m):
        key = m.group(1)
        if key not in colors:
            sys.exit(f"{name}: template needs unresolved key '{key}'")
        return colors[key]

    return re.sub(r"\{\{\s*([A-Za-z0-9_]+)\s*\}\}", sub, template)


def is_light(colors):
    mode = colors.get("mode") or colors.get("theme_type")
    if mode:
        return mode == "light"
    bg = colors["background"]
    return sum(int(bg[i : i + 2], 16) for i in (1, 3, 5)) > 382


def extras(colors):
    """Settings beyond colors that should follow the theme when it changes.

    Ghostty's custom-style app icon is drawn from these colors, so switching
    theme also recolors the Dock icon: the ghost uses the cursor color and the
    screen is a gradient from the background to the selection color.
    """
    return {
        "macos-icon": "custom-style",
        "macos-icon-frame": "aluminum" if is_light(colors) else "plastic",
        "macos-icon-ghost-color": colors["bright_foreground"],
        "macos-icon-screen-color": f'{colors["background"]},{colors["selection_background"]}',
        "split-divider-color": colors.get("accent") or colors["blue"],
    }


EXTRAS_HEADER = """\
# Matching app icon and split divider, so they change along with the theme.
# The macos-icon-* settings only affect macOS. To keep your own icon or
# divider, set them in your Ghostty config: it takes precedence over the theme
# (for example `macos-icon = official`)."""

FRAME_FILL = {"plastic": "#1d1d1f", "aluminum": "#c9cbcf"}


def preview_svg(body, label, icon):
    """Draw the theme's colors, 16-color palette and app icon colors."""
    values = dict(re.findall(r"^([a-z-]+) = (#[0-9A-Fa-f]{6})$", body, re.M))
    palette = dict(re.findall(r"^palette = (\d+)=(#[0-9A-Fa-f]{6})$", body, re.M))
    bg, fg = values["background"], values["foreground"]
    cells = "".join(
        f'<rect x="{16 + (i % 8) * 46}" y="{48 + (i // 8) * 30}" width="40" height="24" rx="4" fill="{palette[str(i)]}"/>'
        for i in range(16)
    )
    # Icon swatch: frame, gradient screen, and a simple ghost in the ghost color.
    screen_from, screen_to = icon["macos-icon-screen-color"].split(",")
    ghost = icon["macos-icon-ghost-color"]
    icon_svg = (
        f'<defs><linearGradient id="screen" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="{screen_from}"/><stop offset="1" stop-color="{screen_to}"/>'
        f"</linearGradient></defs>"
        f'<rect x="398" y="30" width="72" height="72" rx="16" fill="{FRAME_FILL[icon["macos-icon-frame"]]}"/>'
        f'<rect x="405" y="37" width="58" height="58" rx="11" fill="url(#screen)"/>'
        f'<path d="M422 84 V62 a12 12 0 0 1 24 0 V84 l-4-4 -4 4 -4-4 -4 4 -4-4 z" fill="{ghost}"/>'
        f'<circle cx="430" cy="63" r="2.2" fill="{screen_from}"/><circle cx="438" cy="63" r="2.2" fill="{screen_from}"/>'
    )
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="486" height="124" viewBox="0 0 486 124">'
        f'<rect width="486" height="124" rx="8" fill="{bg}" stroke="{palette["8"]}"/>'
        f'<text x="16" y="30" fill="{fg}" font-family="ui-monospace,Menlo,monospace" font-size="15">{label}</text>'
        f"{cells}{icon_svg}</svg>\n"
    )


def main():
    if len(sys.argv) > 1:
        src = Path(sys.argv[1])
    else:
        src = Path(tempfile.mkdtemp()) / "omarchy"
        subprocess.run(["git", "clone", "--quiet", "--depth", "1", REPO, str(src)], check=True)

    template = (src / "default/themed/ghostty.conf.tpl").read_text()
    commit = subprocess.run(
        ["git", "-C", str(src), "rev-parse", "--short", "HEAD"], capture_output=True, text=True
    ).stdout.strip()

    OUT_DIR.mkdir(exist_ok=True)
    PREVIEW_DIR.mkdir(exist_ok=True)
    for old in [*OUT_DIR.glob("Omarchy *"), *PREVIEW_DIR.glob("*.svg")]:
        old.unlink()

    for colors_file in sorted(src.glob("themes/*/colors.toml")):
        slug = colors_file.parent.name
        theme_dir = colors_file.parent
        # A theme may ship a hand-written Ghostty config; prefer it over the template.
        shipped = theme_dir / "ghostty.conf"
        name = "Omarchy " + NAME_OVERRIDES.get(slug, slug.replace("-", " ").title())
        colors = resolve(tomllib.loads(colors_file.read_text()))
        body = shipped.read_text() if shipped.exists() else render(template, colors, slug)
        icon = extras(colors)
        header = f"# {name}\n# Ported from Omarchy theme '{slug}' ({REPO}, commit {commit or 'unknown'})\n\n"
        extra_lines = "\n".join(f"{k} = {v}" for k, v in icon.items())
        (OUT_DIR / name).write_text(f'{header}{body.rstrip(chr(10))}\n\n{EXTRAS_HEADER}\n{extra_lines}\n')
        (PREVIEW_DIR / f"{slug}.svg").write_text(preview_svg(body, name, icon))
        print(f"{slug:18} -> themes/{name}")


if __name__ == "__main__":
    main()
