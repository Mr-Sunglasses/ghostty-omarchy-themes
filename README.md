# Omarchy themes for Ghostty

All 22 themes from [Omarchy](https://github.com/omacom/omarchy) ported to the [Ghostty](https://ghostty.org) terminal, for macOS and Linux.

The colors are generated straight from each Omarchy theme's `colors.toml` using Omarchy's own Ghostty template, so you get exactly what Omarchy itself writes for Ghostty: background, foreground, cursor, selection and the full 16-color ANSI palette.

## Quick install

```sh
curl -fsSL https://raw.githubusercontent.com/Mr-Sunglasses/ghostty-omarchy-themes/main/install.sh | bash
```

Then pick a theme in your Ghostty config (`~/.config/ghostty/config`):

```
theme = Omarchy Tokyo Night
```

Reload Ghostty with <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>,</kbd> (macOS) or <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>,</kbd> (Linux).

### Other ways to install

From a clone:

```sh
git clone https://github.com/Mr-Sunglasses/ghostty-omarchy-themes
cd ghostty-omarchy-themes
./install.sh
```

Or manually: copy the files in [`themes/`](themes) into `~/.config/ghostty/themes/`.

### Tips

Follow your system's light/dark appearance:

```
theme = light:Omarchy Catppuccin Latte,dark:Omarchy Catppuccin Mocha
```

Browse every installed theme with a live preview:

```sh
ghostty +list-themes
```

## Themes

| Theme | Mode | Config | Palette |
|---|---|---|---|
| Catppuccin Latte | Light | `theme = Omarchy Catppuccin Latte` | <img src="previews/catppuccin-latte.svg" width="300" alt="Catppuccin Latte palette"> |
| Catppuccin Mocha | Dark | `theme = Omarchy Catppuccin Mocha` | <img src="previews/catppuccin.svg" width="300" alt="Catppuccin Mocha palette"> |
| Ethereal | Dark | `theme = Omarchy Ethereal` | <img src="previews/ethereal.svg" width="300" alt="Ethereal palette"> |
| Everforest | Dark | `theme = Omarchy Everforest` | <img src="previews/everforest.svg" width="300" alt="Everforest palette"> |
| Flexoki Light | Light | `theme = Omarchy Flexoki Light` | <img src="previews/flexoki-light.svg" width="300" alt="Flexoki Light palette"> |
| Gruvbox | Dark | `theme = Omarchy Gruvbox` | <img src="previews/gruvbox.svg" width="300" alt="Gruvbox palette"> |
| Hackerman | Dark | `theme = Omarchy Hackerman` | <img src="previews/hackerman.svg" width="300" alt="Hackerman palette"> |
| Kanagawa | Dark | `theme = Omarchy Kanagawa` | <img src="previews/kanagawa.svg" width="300" alt="Kanagawa palette"> |
| Last Horizon | Dark | `theme = Omarchy Last Horizon` | <img src="previews/last-horizon.svg" width="300" alt="Last Horizon palette"> |
| Lumon | Dark | `theme = Omarchy Lumon` | <img src="previews/lumon.svg" width="300" alt="Lumon palette"> |
| Lupine | Light | `theme = Omarchy Lupine` | <img src="previews/lupine.svg" width="300" alt="Lupine palette"> |
| Matte Black | Dark | `theme = Omarchy Matte Black` | <img src="previews/matte-black.svg" width="300" alt="Matte Black palette"> |
| Miasma | Dark | `theme = Omarchy Miasma` | <img src="previews/miasma.svg" width="300" alt="Miasma palette"> |
| Nord | Dark | `theme = Omarchy Nord` | <img src="previews/nord.svg" width="300" alt="Nord palette"> |
| Osaka Jade | Dark | `theme = Omarchy Osaka Jade` | <img src="previews/osaka-jade.svg" width="300" alt="Osaka Jade palette"> |
| Retro 82 | Dark | `theme = Omarchy Retro 82` | <img src="previews/retro-82.svg" width="300" alt="Retro 82 palette"> |
| Ristretto | Dark | `theme = Omarchy Ristretto` | <img src="previews/ristretto.svg" width="300" alt="Ristretto palette"> |
| Rose Pine Dawn | Light | `theme = Omarchy Rose Pine Dawn` | <img src="previews/rose-pine.svg" width="300" alt="Rose Pine Dawn palette"> |
| Solitude | Dark | `theme = Omarchy Solitude` | <img src="previews/solitude.svg" width="300" alt="Solitude palette"> |
| Tokyo Night | Dark | `theme = Omarchy Tokyo Night` | <img src="previews/tokyo-night.svg" width="300" alt="Tokyo Night palette"> |
| Vantablack | Dark | `theme = Omarchy Vantablack` | <img src="previews/vantablack.svg" width="300" alt="Vantablack palette"> |
| White | Light | `theme = Omarchy White` | <img src="previews/white.svg" width="300" alt="White palette"> |

## Regenerating from upstream

[`generate.py`](generate.py) (Python 3.11+, no dependencies) rebuilds `themes/` and `previews/` from the latest Omarchy. It resolves each palette with the same fallback rules as Omarchy's `omarchy-theme-color` and renders Omarchy's `default/themed/ghostty.conf.tpl`, so new themes and template changes upstream are picked up automatically.

```sh
./generate.py                 # clones omarchy into a temp dir
./generate.py ~/src/omarchy   # or use an existing checkout
```

## Credits

Theme palettes are from [Omarchy](https://github.com/omacom/omarchy) by David Heinemeier Hansson and its contributors, and from the original theme authors (Catppuccin, Tokyo Night, Rosé Pine, Nord, Gruvbox, Everforest, Kanagawa, Flexoki and others). Released under the [MIT License](LICENSE).
