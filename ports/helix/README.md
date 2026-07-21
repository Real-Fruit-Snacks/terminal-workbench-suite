# Terminal Workbench for Helix

Dark and light `.toml` themes implementing the [Terminal Workbench design
system](https://github.com/Real-Fruit-Snacks/terminal-workbench-suite) for
the [Helix](https://helix-editor.com) editor: calm graphite surfaces,
restrained ANSI-style accents, quiet chrome with color reserved for
signal. Covers core editor UI, tree-sitter syntax scopes, diagnostics, and
a mode-aware statusline, with a `[palette]` table backing every color
reference.

## Files

```
terminal-workbench-dark.toml    dark theme
terminal-workbench-light.toml   light theme
```

## Install

Requires Helix 23.05 or newer (palette-referencing theme syntax).

**Manual copy:** clone the suite, then copy both files into Helix's themes
directory (`~/.config/helix/themes/` on Linux/macOS,
`%AppData%\helix\themes\` on Windows):

    git clone https://github.com/Real-Fruit-Snacks/terminal-workbench-suite
    mkdir -p ~/.config/helix/themes
    cp terminal-workbench-suite/ports/helix/terminal-workbench-*.toml ~/.config/helix/themes/

**Release package:** each [release](https://github.com/Real-Fruit-Snacks/terminal-workbench-suite/releases)
ships `terminal-workbench-helix.zip`, an archive of both theme files and
this README.

Then set the theme in `~/.config/helix/config.toml`:

```toml
theme = "terminal-workbench-dark"
```

or `"terminal-workbench-light"` for the light variant. Reload with
`:config-reload` or restart Helix.

## Notes

- Insert/normal/select statusline colors are drawn from the suite's accent
  family (mint, cyan, violet) rather than ad hoc colors.
- Every scope and UI key resolves through the file's own `[palette]`
  table — no bare hex codes outside it.

## See also

- [Suite root README](../../README.md) — overview of every port.
- [`THEME-SPEC.md`](../../THEME-SPEC.md) — the full portable design
  specification these themes implement.

## License

Released under the [MIT License](../../LICENSE).
