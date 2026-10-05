# Omarchy themes for Ghostty

All 22 themes from [Omarchy](https://github.com/omacom/omarchy) ported to the [Ghostty](https://ghostty.org) terminal, for macOS and Linux.

The colors are generated straight from each Omarchy theme's `colors.toml` using Omarchy's own Ghostty template, so you get exactly what Omarchy itself writes for Ghostty: background, foreground, cursor, selection and the full 16-color ANSI palette.

On macOS, each theme also recolors **Ghostty's app icon** and the **split divider** to match, so switching theme changes the Dock icon too ([details](#matching-app-icon)).

## Quick install

```sh
curl -fsSL https://raw.githubusercontent.com/Mr-Sunglasses/ghostty-omarchy-themes/main/install.sh | bash
```

Then pick a theme ([screenshots](#screenshots)) in your Ghostty config (`~/.config/ghostty/config`):

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

| Theme | Mode | Config | Palette & icon colors |
|---|---|---|---|
| Catppuccin Latte | Light | `theme = Omarchy Catppuccin Latte` | <img src="previews/catppuccin-latte.svg" width="360" alt="Catppuccin Latte palette and icon colors"> |
| Catppuccin Mocha | Dark | `theme = Omarchy Catppuccin Mocha` | <img src="previews/catppuccin.svg" width="360" alt="Catppuccin Mocha palette and icon colors"> |
| Ethereal | Dark | `theme = Omarchy Ethereal` | <img src="previews/ethereal.svg" width="360" alt="Ethereal palette and icon colors"> |
| Everforest | Dark | `theme = Omarchy Everforest` | <img src="previews/everforest.svg" width="360" alt="Everforest palette and icon colors"> |
| Flexoki Light | Light | `theme = Omarchy Flexoki Light` | <img src="previews/flexoki-light.svg" width="360" alt="Flexoki Light palette and icon colors"> |
| Gruvbox | Dark | `theme = Omarchy Gruvbox` | <img src="previews/gruvbox.svg" width="360" alt="Gruvbox palette and icon colors"> |
| Hackerman | Dark | `theme = Omarchy Hackerman` | <img src="previews/hackerman.svg" width="360" alt="Hackerman palette and icon colors"> |
| Kanagawa | Dark | `theme = Omarchy Kanagawa` | <img src="previews/kanagawa.svg" width="360" alt="Kanagawa palette and icon colors"> |
| Last Horizon | Dark | `theme = Omarchy Last Horizon` | <img src="previews/last-horizon.svg" width="360" alt="Last Horizon palette and icon colors"> |
| Lumon | Dark | `theme = Omarchy Lumon` | <img src="previews/lumon.svg" width="360" alt="Lumon palette and icon colors"> |
| Lupine | Light | `theme = Omarchy Lupine` | <img src="previews/lupine.svg" width="360" alt="Lupine palette and icon colors"> |
| Matte Black | Dark | `theme = Omarchy Matte Black` | <img src="previews/matte-black.svg" width="360" alt="Matte Black palette and icon colors"> |
| Miasma | Dark | `theme = Omarchy Miasma` | <img src="previews/miasma.svg" width="360" alt="Miasma palette and icon colors"> |
| Nord | Dark | `theme = Omarchy Nord` | <img src="previews/nord.svg" width="360" alt="Nord palette and icon colors"> |
| Osaka Jade | Dark | `theme = Omarchy Osaka Jade` | <img src="previews/osaka-jade.svg" width="360" alt="Osaka Jade palette and icon colors"> |
| Retro 82 | Dark | `theme = Omarchy Retro 82` | <img src="previews/retro-82.svg" width="360" alt="Retro 82 palette and icon colors"> |
| Ristretto | Dark | `theme = Omarchy Ristretto` | <img src="previews/ristretto.svg" width="360" alt="Ristretto palette and icon colors"> |
| Rose Pine Dawn | Light | `theme = Omarchy Rose Pine Dawn` | <img src="previews/rose-pine.svg" width="360" alt="Rose Pine Dawn palette and icon colors"> |
| Solitude | Dark | `theme = Omarchy Solitude` | <img src="previews/solitude.svg" width="360" alt="Solitude palette and icon colors"> |
| Tokyo Night | Dark | `theme = Omarchy Tokyo Night` | <img src="previews/tokyo-night.svg" width="360" alt="Tokyo Night palette and icon colors"> |
| Vantablack | Dark | `theme = Omarchy Vantablack` | <img src="previews/vantablack.svg" width="360" alt="Vantablack palette and icon colors"> |
| White | Light | `theme = Omarchy White` | <img src="previews/white.svg" width="360" alt="White palette and icon colors"> |

## Screenshots

Each theme applied in Ghostty on macOS (default font, `ls`, `git` output, some code and the 16-color palette).

<table>
<tr>
<td align="center"><b>Catppuccin Latte</b><br><img src="screenshots/catppuccin-latte.png" alt="Catppuccin Latte in Ghostty"></td>
<td align="center"><b>Catppuccin Mocha</b><br><img src="screenshots/catppuccin.png" alt="Catppuccin Mocha in Ghostty"></td>
</tr>
<tr>
<td align="center"><b>Ethereal</b><br><img src="screenshots/ethereal.png" alt="Ethereal in Ghostty"></td>
<td align="center"><b>Everforest</b><br><img src="screenshots/everforest.png" alt="Everforest in Ghostty"></td>
</tr>
<tr>
<td align="center"><b>Flexoki Light</b><br><img src="screenshots/flexoki-light.png" alt="Flexoki Light in Ghostty"></td>
<td align="center"><b>Gruvbox</b><br><img src="screenshots/gruvbox.png" alt="Gruvbox in Ghostty"></td>
</tr>
<tr>
<td align="center"><b>Hackerman</b><br><img src="screenshots/hackerman.png" alt="Hackerman in Ghostty"></td>
<td align="center"><b>Kanagawa</b><br><img src="screenshots/kanagawa.png" alt="Kanagawa in Ghostty"></td>
</tr>
<tr>
<td align="center"><b>Last Horizon</b><br><img src="screenshots/last-horizon.png" alt="Last Horizon in Ghostty"></td>
<td align="center"><b>Lumon</b><br><img src="screenshots/lumon.png" alt="Lumon in Ghostty"></td>
</tr>
<tr>
<td align="center"><b>Lupine</b><br><img src="screenshots/lupine.png" alt="Lupine in Ghostty"></td>
<td align="center"><b>Matte Black</b><br><img src="screenshots/matte-black.png" alt="Matte Black in Ghostty"></td>
</tr>
<tr>
<td align="center"><b>Miasma</b><br><img src="screenshots/miasma.png" alt="Miasma in Ghostty"></td>
<td align="center"><b>Nord</b><br><img src="screenshots/nord.png" alt="Nord in Ghostty"></td>
</tr>
<tr>
<td align="center"><b>Osaka Jade</b><br><img src="screenshots/osaka-jade.png" alt="Osaka Jade in Ghostty"></td>
<td align="center"><b>Retro 82</b><br><img src="screenshots/retro-82.png" alt="Retro 82 in Ghostty"></td>
</tr>
<tr>
<td align="center"><b>Ristretto</b><br><img src="screenshots/ristretto.png" alt="Ristretto in Ghostty"></td>
<td align="center"><b>Rose Pine Dawn</b><br><img src="screenshots/rose-pine.png" alt="Rose Pine Dawn in Ghostty"></td>
</tr>
<tr>
<td align="center"><b>Solitude</b><br><img src="screenshots/solitude.png" alt="Solitude in Ghostty"></td>
<td align="center"><b>Tokyo Night</b><br><img src="screenshots/tokyo-night.png" alt="Tokyo Night in Ghostty"></td>
</tr>
<tr>
<td align="center"><b>Vantablack</b><br><img src="screenshots/vantablack.png" alt="Vantablack in Ghostty"></td>
<td align="center"><b>White</b><br><img src="screenshots/white.png" alt="White in Ghostty"></td>
</tr>
</table>

## Matching app icon

Every theme file sets Ghostty's `custom-style` app icon in the theme's colors, along with a matching split divider:

```
macos-icon = custom-style
macos-icon-frame = plastic                    # aluminum for light themes
macos-icon-ghost-color = <cursor color>
macos-icon-screen-color = <background>,<selection>
split-divider-color = <accent>
```

Change `theme` in your config, restart Ghostty, and the Dock icon follows. The icon swatches in the table above are simplified previews of these colors; Ghostty draws the actual icon.

**Opting out:** anything in your own config takes precedence over the theme, so to keep the standard icon add:

```
macos-icon = official
```

Notes:

- The `macos-icon-*` settings only apply on macOS. The split divider color works everywhere.
- Ghostty marks `custom-style` as experimental, so a future Ghostty release may change how it looks.
- Remove any `macos-icon*` or `split-divider-color` lines from your own config if you want the theme to control them.
- Icon changes need a full restart of Ghostty (quit and reopen), not just a config reload.

## Regenerating from upstream

[`generate.py`](generate.py) (Python 3.11+, no dependencies) rebuilds `themes/` and `previews/` (including the icon colors) from the latest Omarchy. It resolves each palette with the same fallback rules as Omarchy's `omarchy-theme-color` and renders Omarchy's `default/themed/ghostty.conf.tpl`, so new themes and template changes upstream are picked up automatically.

```sh
./generate.py                 # clones omarchy into a temp dir
./generate.py ~/src/omarchy   # or use an existing checkout
```

On macOS, [`screenshots.sh`](screenshots.sh) retakes the terminal screenshots by opening Ghostty with each theme and capturing the window (needs Screen Recording permission for your terminal):

```sh
./screenshots.sh                 # all themes
./screenshots.sh "Tokyo Night"   # just one
```

## Credits

Theme palettes are from [Omarchy](https://github.com/omacom/omarchy) by David Heinemeier Hansson and its contributors, and from the original theme authors (Catppuccin, Tokyo Night, Rosé Pine, Nord, Gruvbox, Everforest, Kanagawa, Flexoki and others). Released under the [MIT License](LICENSE).
