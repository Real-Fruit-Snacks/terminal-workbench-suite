# Terminal Workbench for terminal emulators

Dark and light Terminal Workbench color schemes for ten terminal emulators and multiplexers: [Ghostty](#ghostty), [Alacritty](#alacritty), [kitty](#kitty), [WezTerm](#wezterm), [PuTTY](#putty), [MobaXterm](#mobaxterm), [GNOME Terminal](#gnome-terminal), [Konsole](#konsole), [foot](#foot), and [tmux](#tmux). Each app gets its own subfolder with a dark and a light config file, generated from the same palette as the rest of the suite.

See the [suite root README](../../README.md) for an overview of every port, and [`THEME-SPEC.md`](../../THEME-SPEC.md) for the full portable design specification these configs implement.

## Contents

```
terminals/
├── ghostty/terminal-workbench-dark, terminal-workbench-light
├── alacritty/terminal-workbench-dark.toml, terminal-workbench-light.toml
├── kitty/terminal-workbench-dark.conf, terminal-workbench-light.conf
├── wezterm/Terminal Workbench Dark.toml, Terminal Workbench Light.toml
├── putty/terminal-workbench-dark.reg, terminal-workbench-light.reg
├── mobaxterm/terminal-workbench-dark.ini, terminal-workbench-light.ini
├── gnome-terminal/terminal-workbench-dark.dconf, terminal-workbench-light.dconf
├── konsole/TerminalWorkbenchDark.colorscheme, TerminalWorkbenchLight.colorscheme
├── foot/terminal-workbench-dark.ini, terminal-workbench-light.ini
└── tmux/terminal-workbench-dark.tmux, terminal-workbench-light.tmux
```

## Install

### Ghostty

Files: [`ghostty/terminal-workbench-dark`](ghostty/terminal-workbench-dark), [`ghostty/terminal-workbench-light`](ghostty/terminal-workbench-light)

1. Copy both files into `~/.config/ghostty/themes/`.
2. In `~/.config/ghostty/config`, set:
   ```
   theme = terminal-workbench-dark
   ```
   or `terminal-workbench-light` for the light variant.

### Alacritty

Files: [`alacritty/terminal-workbench-dark.toml`](alacritty/terminal-workbench-dark.toml), [`alacritty/terminal-workbench-light.toml`](alacritty/terminal-workbench-light.toml)

1. Copy both files next to your `alacritty.toml` (or anywhere on disk).
2. Import the one you want in `alacritty.toml`:
   ```toml
   [general]
   import = ["/path/to/terminal-workbench-dark.toml"]
   ```
   Swap in `terminal-workbench-light.toml` for the light variant, or merge the `[colors.*]` tables directly into your existing config.

### kitty

Files: [`kitty/terminal-workbench-dark.conf`](kitty/terminal-workbench-dark.conf), [`kitty/terminal-workbench-light.conf`](kitty/terminal-workbench-light.conf)

1. Copy both files into `~/.config/kitty/`.
2. In `kitty.conf`, add:
   ```
   include terminal-workbench-dark.conf
   ```
   or `terminal-workbench-light.conf` for the light variant.
3. Reload with <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>F5</kbd> or restart kitty.

### WezTerm

Files: [`wezterm/Terminal Workbench Dark.toml`](<wezterm/Terminal Workbench Dark.toml>), [`wezterm/Terminal Workbench Light.toml`](<wezterm/Terminal Workbench Light.toml>)

1. Copy both files into `~/.config/wezterm/colors/`.
2. In `wezterm.lua`, set:
   ```lua
   config.color_scheme = "Terminal Workbench Dark"
   ```
   or `"Terminal Workbench Light"` for the light variant.

### PuTTY

Files: [`putty/terminal-workbench-dark.reg`](putty/terminal-workbench-dark.reg), [`putty/terminal-workbench-light.reg`](putty/terminal-workbench-light.reg)

1. Double-click the `.reg` file (or right-click → Merge) to import it into the registry. This creates a saved session named **Terminal Workbench** (or **Terminal Workbench Light**) under `HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions`.
2. Open PuTTY, load the **Terminal Workbench** session, and either launch it directly or copy its colour settings into your own saved session via **Load → Save**.

### MobaXterm

Files: [`mobaxterm/terminal-workbench-dark.ini`](mobaxterm/terminal-workbench-dark.ini), [`mobaxterm/terminal-workbench-light.ini`](mobaxterm/terminal-workbench-light.ini)

1. Close MobaXterm and open your `MobaXterm.ini` (in the MobaXterm install/portable folder, or `Documents\MobaXterm` for the installed version).
2. Replace the existing `[Colors]` section with the contents of the file for the mode you want (everything below `[Colors]` up to the next `[Section]`).
3. Save and restart MobaXterm.

### GNOME Terminal

Files: [`gnome-terminal/terminal-workbench-dark.dconf`](gnome-terminal/terminal-workbench-dark.dconf), [`gnome-terminal/terminal-workbench-light.dconf`](gnome-terminal/terminal-workbench-light.dconf)

Each file is a dconf keyfile for one profile, keyed to a fixed UUID so the load command is reproducible:

- Dark: `4f2a1c60-9e3b-4c71-8d5a-b90a2f61ce01`
- Light: `5a3b2d71-af4c-4d82-9e6b-ca1b3a72df12`

1. Load the profile:
   ```sh
   dconf load /org/gnome/terminal/legacy/profiles:/:4f2a1c60-9e3b-4c71-8d5a-b90a2f61ce01/ < terminal-workbench-dark.dconf
   ```
   (use the light UUID and file for the light variant.)
2. Add the UUID to the profile list so GNOME Terminal picks it up:
   ```sh
   dconf write /org/gnome/terminal/legacy/profiles:/list \
     "$(dconf read /org/gnome/terminal/legacy/profiles:/list | sed "s/]$/, '4f2a1c60-9e3b-4c71-8d5a-b90a2f61ce01']/;s/^@as \[\]$/['4f2a1c60-9e3b-4c71-8d5a-b90a2f61ce01']/")"
   ```
3. Select **Terminal Workbench** (or **Terminal Workbench Light**) under **Preferences → Profiles**.

### Konsole

Files: [`konsole/TerminalWorkbenchDark.colorscheme`](konsole/TerminalWorkbenchDark.colorscheme), [`konsole/TerminalWorkbenchLight.colorscheme`](konsole/TerminalWorkbenchLight.colorscheme)

1. Copy both files into `~/.local/share/konsole/`.
2. Open Konsole's **Settings → Edit Current Profile → Appearance**, and select **Terminal Workbench Dark** or **Terminal Workbench Light** from the color scheme list.

### foot

Files: [`foot/terminal-workbench-dark.ini`](foot/terminal-workbench-dark.ini), [`foot/terminal-workbench-light.ini`](foot/terminal-workbench-light.ini)

1. Copy both files into `~/.config/foot/`.
2. In `~/.config/foot/foot.ini`, add:
   ```ini
   include=~/.config/foot/terminal-workbench-dark.ini
   ```
   or `terminal-workbench-light.ini` for the light variant.

### tmux

Files: [`tmux/terminal-workbench-dark.tmux`](tmux/terminal-workbench-dark.tmux), [`tmux/terminal-workbench-light.tmux`](tmux/terminal-workbench-light.tmux)

1. Copy both files anywhere on disk (e.g. `~/.config/tmux/`).
2. In `~/.tmux.conf`, add:
   ```
   source-file ~/.config/tmux/terminal-workbench-dark.tmux
   ```
   or `terminal-workbench-light.tmux` for the light variant.
3. Reload with `tmux source-file ~/.tmux.conf` or `prefix` + <kbd>:</kbd> `source-file ~/.tmux.conf`.

## License

Released under the [MIT License](../../LICENSE).
