<div align="center">

# Omarchy themes for Ghostty

**All 22 [Omarchy](https://github.com/omacom/omarchy) themes, ported to the [Ghostty](https://ghostty.org) terminal.**<br>
Exact colors, a matching app icon for every theme, and matching Neovim, btop, bat and tmux themes.

[![Themes](https://img.shields.io/badge/themes-22-7aa2f7)](#gallery) [![Ghostty](https://img.shields.io/badge/for-Ghostty-9ece6a)](https://ghostty.org) [![Platforms](https://img.shields.io/badge/macOS%20%C2%B7%20Linux-supported-e0af68)](#install) [![License](https://img.shields.io/github/license/Mr-Sunglasses/ghostty-omarchy-themes?color=bb9af7)](LICENSE)

[Install](#install) · [Gallery](#gallery) · [App icon](#a-matching-app-icon) · [Other apps](#matching-app-themes) · [oms](https://oms.kanishkk.xyz)

<img src="screenshots/hero.png" alt="Tokyo Night, Catppuccin Latte, Gruvbox and Rose Pine Dawn in Ghostty" width="820">

</div>

## Why these themes

- **Exact Omarchy colors.** Each theme is generated from Omarchy's own `colors.toml` with Omarchy's own Ghostty template, so you get what Omarchy itself writes: background, foreground, cursor, selection and all 16 ANSI colors.
- **The Dock icon follows the theme.** On macOS, every theme recolors Ghostty's app icon and the split divider to match ([details](#a-matching-app-icon)).
- **Your other tools match too.** Neovim, btop, bat and tmux themes in the same colors live in [`apps/`](apps).
- **17 dark and 5 light themes**, kept in sync with Omarchy by one script.

> [!TIP]
> **Want the wallpapers too?** [**oms**](https://github.com/Mr-Sunglasses/oms) is a small macOS app for these themes. Pick a theme with a live preview and it sets Ghostty, the matching wallpaper on every Space, and Neovim, btop, bat and tmux, all at once. It can even follow light and dark mode.
>
> ```sh
> curl -fsSL https://kanishkk.xyz/oms | bash
> ```

## Install

```sh
curl -fsSL https://raw.githubusercontent.com/Mr-Sunglasses/ghostty-omarchy-themes/main/install.sh | bash
```

This copies the themes into `~/.config/ghostty/themes`. Then pick one in your Ghostty config (`~/.config/ghostty/config`):

```ini
theme = Omarchy Tokyo Night
```

Reload Ghostty with <kbd>Cmd</kbd> <kbd>Shift</kbd> <kbd>,</kbd> on macOS or <kbd>Ctrl</kbd> <kbd>Shift</kbd> <kbd>,</kbd> on Linux.

<details>
<summary><b>Other ways to install</b></summary>

From a clone:

```sh
git clone https://github.com/Mr-Sunglasses/ghostty-omarchy-themes
cd ghostty-omarchy-themes
./install.sh
```

Or by hand: copy the files in [`themes/`](themes) into `~/.config/ghostty/themes/`.

</details>

### Tips

Follow your system's light and dark appearance:

```ini
theme = light:Omarchy Catppuccin Latte,dark:Omarchy Catppuccin Mocha
```

Browse every installed theme with a live preview:

```sh
ghostty +list-themes
```

## Gallery

Every theme in Ghostty on macOS, showing `ls`, `git`, some code and the 16-color palette. Copy the line under a screenshot into your config to use that theme.

<table>
<tr>
<td align="center" width="50%"><img src="screenshots/catppuccin-latte.png" alt="Catppuccin Latte in Ghostty"><br><b>Catppuccin Latte</b> · <sub>☀︎ light</sub><br><code>theme = Omarchy Catppuccin Latte</code></td>
<td align="center" width="50%"><img src="screenshots/catppuccin.png" alt="Catppuccin Mocha in Ghostty"><br><b>Catppuccin Mocha</b> · <sub>☾ dark</sub><br><code>theme = Omarchy Catppuccin Mocha</code></td>
</tr>
<tr>
<td align="center" width="50%"><img src="screenshots/ethereal.png" alt="Ethereal in Ghostty"><br><b>Ethereal</b> · <sub>☾ dark</sub><br><code>theme = Omarchy Ethereal</code></td>
<td align="center" width="50%"><img src="screenshots/everforest.png" alt="Everforest in Ghostty"><br><b>Everforest</b> · <sub>☾ dark</sub><br><code>theme = Omarchy Everforest</code></td>
</tr>
<tr>
<td align="center" width="50%"><img src="screenshots/flexoki-light.png" alt="Flexoki Light in Ghostty"><br><b>Flexoki Light</b> · <sub>☀︎ light</sub><br><code>theme = Omarchy Flexoki Light</code></td>
<td align="center" width="50%"><img src="screenshots/gruvbox.png" alt="Gruvbox in Ghostty"><br><b>Gruvbox</b> · <sub>☾ dark</sub><br><code>theme = Omarchy Gruvbox</code></td>
</tr>
<tr>
<td align="center" width="50%"><img src="screenshots/hackerman.png" alt="Hackerman in Ghostty"><br><b>Hackerman</b> · <sub>☾ dark</sub><br><code>theme = Omarchy Hackerman</code></td>
<td align="center" width="50%"><img src="screenshots/kanagawa.png" alt="Kanagawa in Ghostty"><br><b>Kanagawa</b> · <sub>☾ dark</sub><br><code>theme = Omarchy Kanagawa</code></td>
</tr>
<tr>
<td align="center" width="50%"><img src="screenshots/last-horizon.png" alt="Last Horizon in Ghostty"><br><b>Last Horizon</b> · <sub>☾ dark</sub><br><code>theme = Omarchy Last Horizon</code></td>
<td align="center" width="50%"><img src="screenshots/lumon.png" alt="Lumon in Ghostty"><br><b>Lumon</b> · <sub>☾ dark</sub><br><code>theme = Omarchy Lumon</code></td>
</tr>
<tr>
<td align="center" width="50%"><img src="screenshots/lupine.png" alt="Lupine in Ghostty"><br><b>Lupine</b> · <sub>☀︎ light</sub><br><code>theme = Omarchy Lupine</code></td>
<td align="center" width="50%"><img src="screenshots/matte-black.png" alt="Matte Black in Ghostty"><br><b>Matte Black</b> · <sub>☾ dark</sub><br><code>theme = Omarchy Matte Black</code></td>
</tr>
<tr>
<td align="center" width="50%"><img src="screenshots/miasma.png" alt="Miasma in Ghostty"><br><b>Miasma</b> · <sub>☾ dark</sub><br><code>theme = Omarchy Miasma</code></td>
<td align="center" width="50%"><img src="screenshots/nord.png" alt="Nord in Ghostty"><br><b>Nord</b> · <sub>☾ dark</sub><br><code>theme = Omarchy Nord</code></td>
</tr>
<tr>
<td align="center" width="50%"><img src="screenshots/osaka-jade.png" alt="Osaka Jade in Ghostty"><br><b>Osaka Jade</b> · <sub>☾ dark</sub><br><code>theme = Omarchy Osaka Jade</code></td>
<td align="center" width="50%"><img src="screenshots/retro-82.png" alt="Retro 82 in Ghostty"><br><b>Retro 82</b> · <sub>☾ dark</sub><br><code>theme = Omarchy Retro 82</code></td>
</tr>
<tr>
<td align="center" width="50%"><img src="screenshots/ristretto.png" alt="Ristretto in Ghostty"><br><b>Ristretto</b> · <sub>☾ dark</sub><br><code>theme = Omarchy Ristretto</code></td>
<td align="center" width="50%"><img src="screenshots/rose-pine.png" alt="Rose Pine Dawn in Ghostty"><br><b>Rose Pine Dawn</b> · <sub>☀︎ light</sub><br><code>theme = Omarchy Rose Pine Dawn</code></td>
</tr>
<tr>
<td align="center" width="50%"><img src="screenshots/solitude.png" alt="Solitude in Ghostty"><br><b>Solitude</b> · <sub>☾ dark</sub><br><code>theme = Omarchy Solitude</code></td>
<td align="center" width="50%"><img src="screenshots/tokyo-night.png" alt="Tokyo Night in Ghostty"><br><b>Tokyo Night</b> · <sub>☾ dark</sub><br><code>theme = Omarchy Tokyo Night</code></td>
</tr>
<tr>
<td align="center" width="50%"><img src="screenshots/vantablack.png" alt="Vantablack in Ghostty"><br><b>Vantablack</b> · <sub>☾ dark</sub><br><code>theme = Omarchy Vantablack</code></td>
<td align="center" width="50%"><img src="screenshots/white.png" alt="White in Ghostty"><br><b>White</b> · <sub>☀︎ light</sub><br><code>theme = Omarchy White</code></td>
</tr>
</table>

<details>
<summary><b>Palettes and app icon colors</b></summary>
<br>

Each preview shows the 16-color palette and, on the right, the colors the theme gives Ghostty's app icon.

| Theme | Mode | Palette & icon |
|---|---|---|
| Catppuccin Latte | Light | <img src="previews/catppuccin-latte.svg" width="380" alt="Catppuccin Latte palette and icon colors"> |
| Catppuccin Mocha | Dark | <img src="previews/catppuccin.svg" width="380" alt="Catppuccin Mocha palette and icon colors"> |
| Ethereal | Dark | <img src="previews/ethereal.svg" width="380" alt="Ethereal palette and icon colors"> |
| Everforest | Dark | <img src="previews/everforest.svg" width="380" alt="Everforest palette and icon colors"> |
| Flexoki Light | Light | <img src="previews/flexoki-light.svg" width="380" alt="Flexoki Light palette and icon colors"> |
| Gruvbox | Dark | <img src="previews/gruvbox.svg" width="380" alt="Gruvbox palette and icon colors"> |
| Hackerman | Dark | <img src="previews/hackerman.svg" width="380" alt="Hackerman palette and icon colors"> |
| Kanagawa | Dark | <img src="previews/kanagawa.svg" width="380" alt="Kanagawa palette and icon colors"> |
| Last Horizon | Dark | <img src="previews/last-horizon.svg" width="380" alt="Last Horizon palette and icon colors"> |
| Lumon | Dark | <img src="previews/lumon.svg" width="380" alt="Lumon palette and icon colors"> |
| Lupine | Light | <img src="previews/lupine.svg" width="380" alt="Lupine palette and icon colors"> |
| Matte Black | Dark | <img src="previews/matte-black.svg" width="380" alt="Matte Black palette and icon colors"> |
| Miasma | Dark | <img src="previews/miasma.svg" width="380" alt="Miasma palette and icon colors"> |
| Nord | Dark | <img src="previews/nord.svg" width="380" alt="Nord palette and icon colors"> |
| Osaka Jade | Dark | <img src="previews/osaka-jade.svg" width="380" alt="Osaka Jade palette and icon colors"> |
| Retro 82 | Dark | <img src="previews/retro-82.svg" width="380" alt="Retro 82 palette and icon colors"> |
| Ristretto | Dark | <img src="previews/ristretto.svg" width="380" alt="Ristretto palette and icon colors"> |
| Rose Pine Dawn | Light | <img src="previews/rose-pine.svg" width="380" alt="Rose Pine Dawn palette and icon colors"> |
| Solitude | Dark | <img src="previews/solitude.svg" width="380" alt="Solitude palette and icon colors"> |
| Tokyo Night | Dark | <img src="previews/tokyo-night.svg" width="380" alt="Tokyo Night palette and icon colors"> |
| Vantablack | Dark | <img src="previews/vantablack.svg" width="380" alt="Vantablack palette and icon colors"> |
| White | Light | <img src="previews/white.svg" width="380" alt="White palette and icon colors"> |

</details>

## A matching app icon

Every theme file sets Ghostty's `custom-style` app icon in the theme's colors, along with a matching split divider:

```ini
macos-icon = custom-style
macos-icon-frame = plastic                  # aluminum for light themes
macos-icon-ghost-color = <cursor color>
macos-icon-screen-color = <background>,<selection>
split-divider-color = <accent>
```

Change `theme`, quit and reopen Ghostty, and the Dock icon follows. The palette previews above show simplified icon colors; Ghostty draws the real icon.

To keep the standard icon, add this to your own config, which always wins over the theme:

```ini
macos-icon = official
```

> [!NOTE]
> The `macos-icon-*` settings only work on macOS; the divider color works everywhere. Ghostty marks `custom-style` as experimental, so it may look different in future releases. Icon changes need a full restart, not just a reload. If your config already sets `macos-icon*` or `split-divider-color`, remove those lines to let the theme control them.

## Matching app themes

[`apps/<theme>/`](apps) has themes for other apps in the same colors:

| File | App | Made from |
|---|---|---|
| `neovim.lua` | Neovim ([LazyVim](https://www.lazyvim.org)) | The Omarchy theme's own file, or Omarchy's template |
| `btop.theme` | btop | The Omarchy theme's own file, or Omarchy's template |
| `bat.tmTheme` | bat (and delta) | Generated from the colors |
| `tmux.conf` | tmux | Generated from the colors |
| `colors.json` | Anything | The full resolved palette |

[oms](https://github.com/Mr-Sunglasses/oms) applies them for you: `oms apps on nvim btop bat tmux`.

## Regenerating from upstream

[`generate.py`](generate.py) (Python 3.11+, no dependencies) rebuilds `themes/`, `previews/` and `apps/` from the latest Omarchy. It resolves each palette with the same fallback rules as Omarchy's `omarchy-theme-color` and renders Omarchy's own templates, so new themes and template changes upstream come through automatically.

```sh
./generate.py                 # clones Omarchy into a temp folder
./generate.py ~/src/omarchy   # or uses a checkout you have
```

On macOS, [`screenshots.sh`](screenshots.sh) retakes the gallery by opening Ghostty with each theme and capturing the window. Your terminal needs Screen Recording permission.

```sh
./screenshots.sh                 # every theme
./screenshots.sh "Tokyo Night"   # just one
```

## Related

- [**oms**](https://github.com/Mr-Sunglasses/oms): apply these themes, matching wallpapers and app themes on macOS from one picker ([website](https://oms.kanishkk.xyz)).
- [**omarchy-wallpapers**](https://github.com/Mr-Sunglasses/omarchy-wallpapers): every Omarchy wallpaper, sorted by theme.

## Credits

Theme palettes come from [Omarchy](https://github.com/omacom/omarchy) by David Heinemeier Hansson and its contributors, and from the original theme authors (Catppuccin, Tokyo Night, Rosé Pine, Nord, Gruvbox, Everforest, Kanagawa, Flexoki and others). Released under the [MIT License](LICENSE).
