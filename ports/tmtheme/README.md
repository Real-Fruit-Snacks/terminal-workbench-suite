# Terminal Workbench for TextMate-theme consumers

Dark and light `.tmTheme` files implementing the Terminal Workbench design
system, for any tool that reads the TextMate color scheme format: [Sublime
Text](#sublime-text), [bat](#bat), and [delta](#delta). Generated from the
same palette as the rest of the suite.

See the [suite root README](../../README.md) for an overview of every port,
and [`THEME-SPEC.md`](../../THEME-SPEC.md) for the full portable design
specification these themes implement.

## Contents

```
tmtheme/
├── Terminal Workbench Dark.tmTheme
└── Terminal Workbench Light.tmTheme
```

## Install

### Sublime Text

Files: [`Terminal Workbench Dark.tmTheme`](<Terminal Workbench Dark.tmTheme>), [`Terminal Workbench Light.tmTheme`](<Terminal Workbench Light.tmTheme>)

1. Open **Preferences → Browse Packages…** to reveal your `Packages` folder, then open the `User` subfolder.
2. Copy both `.tmTheme` files into `Packages/User/`.
3. Open **Preferences → Color Scheme…** and pick **Terminal Workbench Dark** or **Terminal Workbench Light** from the picker.

### bat

Files: [`Terminal Workbench Dark.tmTheme`](<Terminal Workbench Dark.tmTheme>), [`Terminal Workbench Light.tmTheme`](<Terminal Workbench Light.tmTheme>)

1. Copy both files into bat's theme directory: `~/.config/bat/themes/` (find yours with `bat --config-dir`).
2. Rebuild bat's theme cache:
   ```sh
   bat cache --build
   ```
3. Use the theme directly:
   ```sh
   bat --theme="Terminal Workbench Dark" somefile.rs
   ```
   or set it as the default in `~/.config/bat/config`:
   ```
   --theme="Terminal Workbench Dark"
   ```
   (swap in `"Terminal Workbench Light"` for the light variant).

### delta

Files: [`Terminal Workbench Dark.tmTheme`](<Terminal Workbench Dark.tmTheme>), [`Terminal Workbench Light.tmTheme`](<Terminal Workbench Light.tmTheme>)

delta reuses bat's syntax-theme registry, so install into bat's themes folder first:

1. Copy both files into `~/.config/bat/themes/` and run `bat cache --build` (see [bat](#bat) above).
2. In your `.gitconfig`, add:
   ```ini
   [delta]
       syntax-theme = Terminal Workbench Dark
   ```
   or `Terminal Workbench Light` for the light variant.

## License

Released under the [MIT License](../../LICENSE).
