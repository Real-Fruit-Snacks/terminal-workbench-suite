# twb.vim — Terminal Workbench for Vim

Two classic-Vim colorschemes — `twb-dark` and `twb-light` — porting the
[Terminal Workbench design system](https://github.com/Real-Fruit-Snacks/terminal-workbench-design-system):
calm graphite surfaces, restrained ANSI-style accents, quiet chrome with
color reserved for signal.

**[Live preview →](https://real-fruit-snacks.github.io/terminal-workbench-vim/)**

## Install

Both the `colors/` and `autoload/` directories are required (the colorschemes
share an engine in `autoload/twb.vim`).

**Vim 8 packages:**

    git clone https://github.com/Real-Fruit-Snacks/terminal-workbench-vim ~/.vim/pack/themes/start/twb.vim

(Windows: clone into `~\vimfiles\pack\themes\start\twb.vim`.)

**vim-plug:**

    Plug 'Real-Fruit-Snacks/terminal-workbench-vim'

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
