<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Real-Fruit-Snacks/terminal-workbench-windows-terminal/main/docs/assets/cover-dark.svg" />
  <img alt="Terminal Workbench for Windows Terminal" src="https://raw.githubusercontent.com/Real-Fruit-Snacks/terminal-workbench-windows-terminal/main/docs/assets/cover-light.svg" width="820" />
</picture>

<br/>

A calm, dense, high-contrast theme for Windows Terminal — graphite backgrounds, restrained ANSI-style accents, and matching window chrome in dark and light modes.

<br/>

[![License: MIT](https://img.shields.io/badge/License-MIT-f0c674?style=flat-square)](LICENSE)
&nbsp;[![Release](https://img.shields.io/github/v/release/Real-Fruit-Snacks/terminal-workbench-windows-terminal?style=flat-square&color=63f2ab&label=release)](https://github.com/Real-Fruit-Snacks/terminal-workbench-windows-terminal/releases/latest)
&nbsp;![Windows Terminal](https://img.shields.io/badge/Windows%20Terminal-1.16%2B-6bdcff?style=flat-square)

[Website](https://real-fruit-snacks.github.io/terminal-workbench-windows-terminal/) · [Download](https://github.com/Real-Fruit-Snacks/terminal-workbench-windows-terminal/releases/latest) · [Report an issue](https://github.com/Real-Fruit-Snacks/terminal-workbench-windows-terminal/issues)

</div>

---

## Overview

The interface stays quiet; color is spent only on signal. Terminal Workbench is a port of the [Terminal Workbench](https://github.com/Real-Fruit-Snacks/terminal-workbench) Obsidian theme and follows its [portable design specification](https://github.com/Real-Fruit-Snacks/terminal-workbench/blob/main/docs/THEME-SPEC.md).

## Contents

[`terminal-workbench.json`](terminal-workbench.json) provides four entries:

| Entry | Type | Description |
|---|---|---|
| Terminal Workbench | Color scheme | Dark palette: graphite surfaces, mint primary accent |
| Terminal Workbench Light | Color scheme | Light palette with darkened accents for contrast |
| Terminal Workbench | Window theme | Dark tab row and window chrome |
| Terminal Workbench Light | Window theme | Light tab row and window chrome |

## Installation

1. Open Windows Terminal, go to Settings (<kbd>Ctrl</kbd>+<kbd>,</kbd>), and select **Open JSON file**.
2. Copy both entries from the `schemes` array of [`terminal-workbench.json`](terminal-workbench.json) into the `schemes` array of your `settings.json`.
3. Copy both entries from the `themes` array into the top-level `themes` array of your `settings.json`, creating the array if it does not exist.
4. Activate the theme:

```jsonc
{
    "theme": "Terminal Workbench",
    "profiles":
    {
        "defaults":
        {
            "colorScheme": "Terminal Workbench"
        }
    }
}
```

Color schemes apply to open tabs immediately. The window theme applies after Windows Terminal is closed and reopened.

### Light mode

Replace both names with their light counterparts:

```jsonc
"theme": "Terminal Workbench Light",
"colorScheme": "Terminal Workbench Light"
```

## Palette

### Dark

| Slot | Hex | | Slot | Hex |
|---|---|---|---|---|
| background | `#090C0D` | | foreground | `#DCE4DF` |
| black | `#202A2F` | | brightBlack | `#63736F` |
| red | `#FF6E7A` | | brightRed | `#FF7F8A` |
| green | `#63F2AB` | | brightGreen | `#76F4B5` |
| yellow | `#F0C674` | | brightYellow | `#F2CD85` |
| blue | `#74A8FF` | | brightBlue | `#85B2FF` |
| purple | `#B78CFF` | | brightPurple | `#C09AFF` |
| cyan | `#6BDCFF` | | brightCyan | `#7DE0FF` |
| white | `#B4C3BD` | | brightWhite | `#DCE4DF` |
| cursor | `#63F2AB` | | selection | `#1B3A2D` |

### Light

| Slot | Hex | | Slot | Hex |
|---|---|---|---|---|
| background | `#F5F7F4` | | foreground | `#17201D` |
| black | `#17201D` | | brightBlack | `#60706A` |
| red | `#C8324C` | | brightRed | `#B42D44` |
| green | `#007A4D` | | brightGreen | `#006E45` |
| yellow | `#A46600` | | brightYellow | `#945C00` |
| blue | `#2E62B8` | | brightBlue | `#2958A6` |
| purple | `#7357B8` | | brightPurple | `#684EA6` |
| cyan | `#006F9E` | | brightCyan | `#00648E` |
| white | `#C8D5CF` | | brightWhite | `#F5F7F4` |
| cursor | `#007A4D` | | selection | `#CBE2D8` |

## Design notes

- Normal ANSI colors are the specification's exact accent tokens. Bright variants are the same hues lifted approximately 12% in dark mode and deepened approximately 10% in light mode, keeping bold text distinguishable without expanding the palette.
- The ANSI blue slot, the one color the specification does not define, uses a steel blue positioned between the cyan accent and the violet keyword color.
- The dark selection color is deliberately quiet (primary accent at roughly 20% over the background). For a more visible selection, set `selectionBackground` to `#204836`.
- Foreground-on-background contrast is 15.4:1 in dark mode and approximately 13:1 in light mode, meeting WCAG AA for body text in both.

## Hosting the site

The project page at [real-fruit-snacks.github.io/terminal-workbench-windows-terminal](https://real-fruit-snacks.github.io/terminal-workbench-windows-terminal/) is a static site served from [`docs/`](docs) with no build step.

- **GitHub Pages** — serve `main` : `/docs` (this repository's configuration).
- **GitLab Pages** — the included [`.gitlab-ci.yml`](.gitlab-ci.yml) publishes the same site; push the repository to GitLab and Pages deploys on the default branch.
- **Anywhere else** — copy the contents of `docs/` to any static file server.

Each release attaches a bundle with everything needed to host.

## Related projects

- [Terminal Workbench for Obsidian](https://github.com/Real-Fruit-Snacks/terminal-workbench) — the original theme and its design specification.

## License

Released under the [MIT License](LICENSE).
