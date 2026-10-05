<div align="center">

# Omarchy themes for Ghostty

All 22 [Omarchy](https://github.com/omacom/omarchy) themes for the [Ghostty](https://ghostty.org) terminal, on macOS and Linux.

[![Themes](https://img.shields.io/badge/themes-22-7aa2f7)](#themes) [![License](https://img.shields.io/github/license/Mr-Sunglasses/ghostty-omarchy-themes?color=bb9af7)](LICENSE)

<img src="screenshots/hero.png" alt="Tokyo Night, Catppuccin Latte, Gruvbox and Rose Pine Dawn in Ghostty" width="820">

</div>

## Install

```sh
curl -fsSL https://raw.githubusercontent.com/Mr-Sunglasses/ghostty-omarchy-themes/main/install.sh | bash
```

Then set a theme in `~/.config/ghostty/config` and reload Ghostty (<kbd>Cmd</kbd> <kbd>Shift</kbd> <kbd>,</kbd> on macOS, <kbd>Ctrl</kbd> <kbd>Shift</kbd> <kbd>,</kbd> on Linux):

```ini
theme = Omarchy Tokyo Night
```

To switch with your system's light and dark mode:

```ini
theme = light:Omarchy Catppuccin Latte,dark:Omarchy Tokyo Night
```

> [!TIP]
> On a Mac, [**oms**](https://github.com/Mr-Sunglasses/oms) lets you browse these themes with a live preview and sets a matching wallpaper too.

## Themes

Use any of these as `theme = Omarchy <name>`.

<table>
<tr>
<td align="center" width="50%"><img src="screenshots/catppuccin-latte.png" alt="Catppuccin Latte"><br><b>Catppuccin Latte</b> <sub>light</sub></td>
<td align="center" width="50%"><img src="screenshots/catppuccin.png" alt="Catppuccin Mocha"><br><b>Catppuccin Mocha</b> <sub>dark</sub></td>
</tr>
<tr>
<td align="center" width="50%"><img src="screenshots/ethereal.png" alt="Ethereal"><br><b>Ethereal</b> <sub>dark</sub></td>
<td align="center" width="50%"><img src="screenshots/everforest.png" alt="Everforest"><br><b>Everforest</b> <sub>dark</sub></td>
</tr>
<tr>
<td align="center" width="50%"><img src="screenshots/flexoki-light.png" alt="Flexoki Light"><br><b>Flexoki Light</b> <sub>light</sub></td>
<td align="center" width="50%"><img src="screenshots/gruvbox.png" alt="Gruvbox"><br><b>Gruvbox</b> <sub>dark</sub></td>
</tr>
<tr>
<td align="center" width="50%"><img src="screenshots/hackerman.png" alt="Hackerman"><br><b>Hackerman</b> <sub>dark</sub></td>
<td align="center" width="50%"><img src="screenshots/kanagawa.png" alt="Kanagawa"><br><b>Kanagawa</b> <sub>dark</sub></td>
</tr>
<tr>
<td align="center" width="50%"><img src="screenshots/last-horizon.png" alt="Last Horizon"><br><b>Last Horizon</b> <sub>dark</sub></td>
<td align="center" width="50%"><img src="screenshots/lumon.png" alt="Lumon"><br><b>Lumon</b> <sub>dark</sub></td>
</tr>
<tr>
<td align="center" width="50%"><img src="screenshots/lupine.png" alt="Lupine"><br><b>Lupine</b> <sub>light</sub></td>
<td align="center" width="50%"><img src="screenshots/matte-black.png" alt="Matte Black"><br><b>Matte Black</b> <sub>dark</sub></td>
</tr>
<tr>
<td align="center" width="50%"><img src="screenshots/miasma.png" alt="Miasma"><br><b>Miasma</b> <sub>dark</sub></td>
<td align="center" width="50%"><img src="screenshots/nord.png" alt="Nord"><br><b>Nord</b> <sub>dark</sub></td>
</tr>
<tr>
<td align="center" width="50%"><img src="screenshots/osaka-jade.png" alt="Osaka Jade"><br><b>Osaka Jade</b> <sub>dark</sub></td>
<td align="center" width="50%"><img src="screenshots/retro-82.png" alt="Retro 82"><br><b>Retro 82</b> <sub>dark</sub></td>
</tr>
<tr>
<td align="center" width="50%"><img src="screenshots/ristretto.png" alt="Ristretto"><br><b>Ristretto</b> <sub>dark</sub></td>
<td align="center" width="50%"><img src="screenshots/rose-pine.png" alt="Rose Pine Dawn"><br><b>Rose Pine Dawn</b> <sub>light</sub></td>
</tr>
<tr>
<td align="center" width="50%"><img src="screenshots/solitude.png" alt="Solitude"><br><b>Solitude</b> <sub>dark</sub></td>
<td align="center" width="50%"><img src="screenshots/tokyo-night.png" alt="Tokyo Night"><br><b>Tokyo Night</b> <sub>dark</sub></td>
</tr>
<tr>
<td align="center" width="50%"><img src="screenshots/vantablack.png" alt="Vantablack"><br><b>Vantablack</b> <sub>dark</sub></td>
<td align="center" width="50%"><img src="screenshots/white.png" alt="White"><br><b>White</b> <sub>light</sub></td>
</tr>
</table>

## Extras

**Matching Dock icon (macOS).** Each theme also recolors Ghostty's app icon to match. Quit and reopen Ghostty to see it. To keep the normal icon, add `macos-icon = official` to your config.

**Matching app themes.** [`apps/`](apps) has the same themes for Neovim, btop, bat and tmux.

**Wallpapers.** Every Omarchy wallpaper, sorted by theme, is in [omarchy-wallpapers](https://github.com/Mr-Sunglasses/omarchy-wallpapers).

## Contributing

Everything in `themes/`, `apps/` and `previews/` is generated from [Omarchy](https://github.com/omacom/omarchy), so please don't edit those files by hand. Change [`generate.py`](generate.py) instead and run it:

```sh
./generate.py                 # fetches the latest Omarchy and rebuilds every theme
./generate.py ~/src/omarchy   # or use a local Omarchy checkout
```

It needs Python 3.11 or newer and nothing else. When Omarchy adds a theme, running it is all it takes.

To refresh the screenshots on a Mac, run `./screenshots.sh` (or `./screenshots.sh "Tokyo Night"` for one). It opens Ghostty, so your terminal needs Screen Recording permission.

Issues and pull requests are welcome.

## Credits

The themes come from [Omarchy](https://github.com/omacom/omarchy) and the original theme authors (Catppuccin, Tokyo Night, Rosé Pine, Nord, Gruvbox, Everforest, Kanagawa, Flexoki and more). [MIT License](LICENSE).
