<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)"
    srcset="docs/assets/cover-dark.svg" />
  <img alt="twb.vim"
    src="docs/assets/cover-light.svg"
    width="820" />
</picture>

<br/>

Two classic-Vim colorschemes — <code>twb-dark</code> and <code>twb-light</code> — porting the
<a href="https://github.com/Real-Fruit-Snacks/terminal-workbench-design-system">Terminal Workbench design system</a>:
calm graphite surfaces, restrained ANSI-style accents, quiet chrome with color reserved for signal.

<br/><br/>

<a href="https://github.com/Real-Fruit-Snacks/terminal-workbench-suite/releases"><img src="https://img.shields.io/github/v/release/Real-Fruit-Snacks/terminal-workbench-suite?style=flat-square&color=63f2ab" alt="Release"></a>
<img src="https://img.shields.io/badge/license-MIT-6bdcff?style=flat-square" alt="License: MIT">
<img src="https://img.shields.io/badge/vim-8%2B-b78cff?style=flat-square" alt="Vim 8+">

<a href="https://real-fruit-snacks.github.io/terminal-workbench-suite/ports/vim/docs/">Live Preview</a> ·
<a href="https://github.com/Real-Fruit-Snacks/terminal-workbench-suite/releases">Releases</a> ·
<a href="https://github.com/Real-Fruit-Snacks/terminal-workbench-suite/issues">Issues</a>

</div>

## Install

Both the `colors/` and `autoload/` directories are required (the colorschemes
share an engine in `autoload/twb.vim`).

**Vim 8 packages:**

    git clone https://github.com/Real-Fruit-Snacks/terminal-workbench-suite
    ln -s "$(pwd)/terminal-workbench-suite/ports/vim" ~/.vim/pack/themes/start/twb.vim

(Windows: create a junction into `~\vimfiles\pack\themes\start\twb.vim`, or just copy `ports\vim` there.)

**vim-plug:**

    Plug 'Real-Fruit-Snacks/terminal-workbench-suite', { 'rtp': 'ports/vim' }

**Release package:** each [release](https://github.com/Real-Fruit-Snacks/terminal-workbench-suite/releases)
ships a complete archive of the theme, the demo site (`docs/`), and a
`.gitlab-ci.yml` — push the tree to GitLab and the demo site publishes itself
on GitLab Pages.

## Use

    " true color (recommended, needs a true-color terminal or gVim)
    set termguicolors
    colorscheme twb-dark    " or twb-light

Without `termguicolors` the theme falls back to hand-picked xterm-256
approximations automatically.

## Notes

- Requires Vim 8+. Loads in Neovim too, but has no Treesitter/LSP-specific
  highlighting.
- No italics are used anywhere; spell checking uses undercurls in
  GUI/true-color and plain underline in 256-color terminals.
- Vim's built-in `:terminal` gets a matching ANSI palette
  (`g:terminal_ansi_colors`).
- Switch themes with `:colorscheme twb-dark` / `:colorscheme twb-light`, not
  `:set background` (single-background schemes re-source themselves and will
  undo the change).

## Development

Run the headless test suite (needs `vim` on PATH):

    pwsh -File test/run.ps1

## License

MIT, same as the source design system.
