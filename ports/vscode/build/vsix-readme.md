<div align="center">


A calm, dense, high-contrast theme for people who live in panes, shells, logs, and code.

<br/>

[![CI](https://github.com/Real-Fruit-Snacks/terminal-workbench-vscode/actions/workflows/ci.yml/badge.svg)](https://github.com/Real-Fruit-Snacks/terminal-workbench-vscode/actions/workflows/ci.yml)
&nbsp;[![License: MIT](https://img.shields.io/badge/License-MIT-f0c674?style=flat-square)](LICENSE)
&nbsp;[![Release](https://img.shields.io/github/v/release/Real-Fruit-Snacks/terminal-workbench-vscode?style=flat-square&color=6bdcff&label=release)](https://github.com/Real-Fruit-Snacks/terminal-workbench-vscode/releases)
&nbsp;![VS Code](https://img.shields.io/badge/VS%20Code-1.85%2B-63f2ab?style=flat-square)

[Website](https://real-fruit-snacks.github.io/terminal-workbench-vscode/) · [Changelog](CHANGELOG.md) · [Report an issue](https://github.com/Real-Fruit-Snacks/terminal-workbench-vscode/issues)

</div>

---

## Overview

Port of the [Terminal Workbench Obsidian theme](https://github.com/Real-Fruit-Snacks/terminal-workbench). Graphite surfaces, restrained ANSI-style accents, and chrome that stays quiet so the signal (syntax, links, active elements) carries the color. Ships two color themes — Terminal Workbench (dark) and Terminal Workbench Light — plus Terminal Workbench Icons, a matching file icon theme.

## Install

From a `.vsix`:

1. Build or download the latest `terminal-workbench-<version>.vsix`
2. In VS Code: Extensions panel → `…` menu → **Install from VSIX…**

Or from source:

    git clone https://github.com/Real-Fruit-Snacks/terminal-workbench-vscode
    cd terminal-workbench-vscode
    npx --yes @vscode/vsce package --no-dependencies --readme-path build/vsix-readme.md
    code --install-extension terminal-workbench-0.2.0.vsix

## Recommended settings

The theme controls color only. For the full Terminal Workbench feel, pair it with a mono font you like:

    {
      "editor.fontFamily": "'Berkeley Mono', 'JetBrains Mono', 'Cascadia Code', Consolas, monospace",
      "editor.lineHeight": 1.62,
      "workbench.colorTheme": "Terminal Workbench"
    }

## Icons

The extension also ships Terminal Workbench Icons, a matching file icon theme: file types render as small uppercase type chips in the theme's tag style, and folders stay quiet monoline glyphs (the open folder carries the accent). Enable it alongside either color theme:

    {
      "workbench.iconTheme": "terminal-workbench-icons"
    }

## Development

The token tables live once in `build/tokens.js`; both color themes and the file icon set are generated from them:

    node build/build.js   # regenerates themes/ and icons/ and prints a WCAG contrast report
    node --test           # test suite

Design system: see [THEME-SPEC.md](THEME-SPEC.md). Never edit `themes/*.json` or `icons/*.svg` by hand — change tokens or mappings and rebuild.

## License

MIT
