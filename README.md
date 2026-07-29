<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/cover-dark.svg" />
  <img alt="Terminal Workbench" src="docs/assets/cover-light.svg" width="820" />
</picture>

# Terminal Workbench Suite

One repo for the whole Terminal Workbench family: the design system
(spec + tokens), every editor/terminal/browser port, and the official
monospace typeface. Calm graphite surfaces, restrained ANSI-style accents,
mandatory dark **and** light modes, color spent only on signal.

**Live demo:** <https://real-fruit-snacks.github.io/terminal-workbench-suite/>

## Get the theme

| App | How to install |
|---|---|
| **Obsidian** | Settings → Appearance → Themes → browse for **Terminal Workbench** ([standalone repo](https://github.com/Real-Fruit-Snacks/terminal-workbench)) |
| **Vim** | Grab `terminal-workbench-vim.zip` from [Releases](https://github.com/Real-Fruit-Snacks/terminal-workbench-suite/releases), drop `colors/` + `autoload/` into `~/.vim/` — see [ports/vim](ports/vim) |
| **VS Code** | Download the `.vsix` from [Releases](https://github.com/Real-Fruit-Snacks/terminal-workbench-suite/releases), then `code --install-extension terminal-workbench-*.vsix` — see [ports/vscode](ports/vscode) |
| **Brave** | `terminal-workbench-brave.zip` from [Releases](https://github.com/Real-Fruit-Snacks/terminal-workbench-suite/releases), load unpacked via `brave://extensions` — see [ports/brave](ports/brave) |
| **Notepad++** | `terminal-workbench-notepad-plus-plus.zip` from [Releases](https://github.com/Real-Fruit-Snacks/terminal-workbench-suite/releases), XMLs into your `themes\` folder — see [ports/notepad-plus-plus](ports/notepad-plus-plus) |
| **Windows Terminal** | Merge [`terminal-workbench.json`](ports/windows-terminal/terminal-workbench.json) into `settings.json` — see [ports/windows-terminal](ports/windows-terminal) |
| **Font** | `terminal-workbench-mono.zip` from [Releases](https://github.com/Real-Fruit-Snacks/terminal-workbench-suite/releases) — TTFs + webfonts, see [font/](font) |
| **Neovim** | `terminal-workbench-neovim.zip` from [Releases](https://github.com/Real-Fruit-Snacks/terminal-workbench-suite/releases), drop `colors/` + `lua/twb/` into your Neovim config — see [ports/neovim](ports/neovim) |
| **Terminal emulators** (Ghostty · Alacritty · kitty · WezTerm · PuTTY · MobaXterm · GNOME Terminal · Konsole · foot · tmux) | `terminal-workbench-terminals.zip` from [Releases](https://github.com/Real-Fruit-Snacks/terminal-workbench-suite/releases), per-app config files — see [ports/terminals](ports/terminals) |
| **Sublime Text / bat / delta** | `terminal-workbench-tmtheme.zip` from [Releases](https://github.com/Real-Fruit-Snacks/terminal-workbench-suite/releases), drop the `.tmTheme` files into each tool's theme folder — see [ports/tmtheme](ports/tmtheme) |
| **Zed** | `terminal-workbench-zed.zip` from [Releases](https://github.com/Real-Fruit-Snacks/terminal-workbench-suite/releases), copy the theme JSON into `~/.config/zed/themes/` — see [ports/zed](ports/zed) |
| **Helix** | `terminal-workbench-helix.zip` from [Releases](https://github.com/Real-Fruit-Snacks/terminal-workbench-suite/releases), copy both `.toml` files into `~/.config/helix/themes/` — see [ports/helix](ports/helix) |
| **JetBrains IDEs** | `terminal-workbench-jetbrains.zip` from [Releases](https://github.com/Real-Fruit-Snacks/terminal-workbench-suite/releases), import the `.icls` files via **Editor → Color Scheme** — see [ports/jetbrains](ports/jetbrains) |
| **xterm.js** | `terminal-workbench-xtermjs.zip` from [Releases](https://github.com/Real-Fruit-Snacks/terminal-workbench-suite/releases), or import `index.mjs` as an `ITheme` — see [ports/xtermjs](ports/xtermjs) |
| **CodeMirror 6** | `terminal-workbench-codemirror.zip` from [Releases](https://github.com/Real-Fruit-Snacks/terminal-workbench-suite/releases), or copy `terminal-workbench.mjs` into your project — see [ports/codemirror](ports/codemirror) |
| **Firefox** | `terminal-workbench-firefox.zip` from [Releases](https://github.com/Real-Fruit-Snacks/terminal-workbench-suite/releases), load unpacked via `about:debugging#/runtime/this-firefox` — see [ports/firefox](ports/firefox) |
| **Wireshark** | `terminal-workbench-wireshark.zip` from [Releases](https://github.com/Real-Fruit-Snacks/terminal-workbench-suite/releases), drop the profile folders into your Wireshark `profiles/` directory — see [ports/wireshark](ports/wireshark) |
| **Shell prompt & CLI tools** (Oh My Posh · Starship · fzf · eza · btop) | `terminal-workbench-shell.zip` from [Releases](https://github.com/Real-Fruit-Snacks/terminal-workbench-suite/releases), per-tool config files — see [ports/shell](ports/shell) |
| **Slack** | Copy `terminal-workbench-dark.txt` or `-light.txt` into Slack's **Preferences → Themes → Custom Theme** field — see [ports/slack](ports/slack) |
| **Notesnook** | `terminal-workbench-notesnook.zip` from [Releases](https://github.com/Real-Fruit-Snacks/terminal-workbench-suite/releases), then **Settings → Appearance → Themes → Load from file** — see [ports/notesnook](ports/notesnook) |

## Build for the web

Drop the tokens into any page:

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/Real-Fruit-Snacks/terminal-workbench-suite@main/tokens/tokens.css">
```

Add [`tokens/fonts.css`](tokens/fonts.css) the same way for Terminal
Workbench Mono.

## Port it anywhere

[THEME-SPEC.md](THEME-SPEC.md) is the portable source of truth — philosophy,
token tables for both modes, typography, shape, motion, and component
patterns. Hand it to any tool (or AI) to reproduce the theme faithfully.

## Family map

- **This repo** — spec, tokens, demo, ports, font.
- [terminal-workbench](https://github.com/Real-Fruit-Snacks/terminal-workbench) — Obsidian theme (standalone for the community catalog).
- [terminal-workbench-pet](https://github.com/Real-Fruit-Snacks/terminal-workbench-pet) · [terminal-workbench-cursor](https://github.com/Real-Fruit-Snacks/terminal-workbench-cursor) — Obsidian companion plugins.

## Repository layout

```
THEME-SPEC.md   the portable spec (source of truth)
tokens/         drop-in CSS custom properties + font loader
index.html      live demo (GitHub Pages)
ports/          vim · vscode · brave · notepad-plus-plus · windows-terminal · neovim · terminals · tmtheme · zed · helix · jetbrains · xtermjs · codemirror · firefox · wireshark · shell · slack · notesnook
font/           Terminal Workbench Mono — parametric engine + built fonts
```

## License

MIT for everything except the typeface, which is licensed under the
[SIL Open Font License](font/OFL.txt).
