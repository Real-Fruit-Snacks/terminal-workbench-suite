# Changelog

All notable changes to Terminal Workbench Mono. Versioning is roughly semantic:
MAJOR for breaking metric/encoding changes, MINOR for new glyphs/features,
PATCH for fixes.

## [2.0.0] — 2026-07-11

### Changed
- **Renamed the family to Terminal Workbench Mono** — now the official
  typeface of the [Terminal Workbench design
  system](https://github.com/Real-Fruit-Snacks/terminal-workbench-design-system).
  Font metadata, file names (`TerminalWorkbenchMono-*`), the web CSS
  (`terminal-workbench-mono.css`), the Obsidian snippet, and the release
  archives all carry the new name. The GitHub repo is now
  `terminal-workbench-mono` (old URLs redirect).
- Specimen site rebuilt on the design system's `tokens.css` — graphite
  surfaces, mint/cyan/amber accents, and dark + light modes.
- OpenGraph card and favicon regenerated in the Terminal Workbench palette.

### Breaking
- The font family name, PostScript names, all file names, and the OFL
  Reserved Font Name changed. Update any CSS `font-family` rules, editor
  settings, and `@font-face` sources that referenced "Shellback Mono".

## [1.1.0] — 2026-06-12

### Added
- **Medium weight** (500) + **Medium Italic** — the family is now six styles,
  grouped under one typographic family for modern apps.
- **Terminal pack** — box-drawing (light/heavy/double/rounded), block elements,
  eighth blocks, shades (░▒▓), quadrants, and Powerline separators (E0B0–E0B3).
  Full-cell geometry that tiles seamlessly.
- **Latin-1 accented letters** (à á â ã ä å ç è é … Ñ Ö Ü Ý) plus dotless i,
  slashed o, and eszett.
- **Symbols** — © ® ™ € £ ¥ ¢ µ « » · § ¶ † ‡ ✓ ✗ ¿ ¡.
- **More ligatures** — `:: := === !==` join the existing set.
- **Dotted zero** behind the `ss01` stylistic set (the default zero stays slashed).
- **`gasp`** + **`prep`** tables for crisp grayscale rendering at small sizes.
- **`STAT`** table locating each style on the weight + italic axes.
- Interactive type tester, favicon and OpenGraph card on the specimen site.
- GitHub Actions: build-from-source + validate + fontbakery on every push;
  tagged releases ship archives, checksums, and **signed build provenance**.

### Fixed
- Redrawn `&` (was malformed) and `§`; tuned `@`.
- OS/2 code-page bits + Unicode ranges set, Win metrics cover the full ink box,
  Windows-only name records, head/name versions matched — passes fontbakery
  `universal` with 0 FAIL.

## [1.0.2] — 2026-06-11
- Obsidian snippet themes all of Obsidian (interface + notes + code).

## [1.0.1] — 2026-06-11
- Obsidian snippet is now a single self-contained file (fonts embedded as base64).

## [1.0.0] — 2026-06-11
- First release: Regular, Bold, Italic, Bold Italic; coding ligatures; slashed
  zero; full ASCII + typographic extras; TTF + WOFF2; SIL Open Font License 1.1.
