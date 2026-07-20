# Terminal Workbench — Portable Design Spec

A platform-agnostic specification of the Terminal Workbench visual system. Hand this to any tool, framework, or designer to reproduce the theme's look in a terminal emulator, a website, a code editor, a dashboard, a slide deck — anywhere. It captures **what** the theme is (colors, type, shape, motion, the design philosophy) independent of Obsidian's specific CSS class names.

> Origin: distilled from the Terminal Workbench Obsidian theme v1.1.0. The Obsidian implementation lives in `theme.css`; this document is the reusable core.

---

## 1. Design philosophy

The one paragraph that governs every decision below:

> **A calm, dense, high-contrast working surface for people who live in panes, shells, logs, and code — not retro green-on-black novelty.** Graphite backgrounds, crisp typography, restrained ANSI-style accents, readable code, and chrome that feels close to a modern terminal. The interface stays quiet; signal (links, prompts, active elements, syntax) carries the color. When in doubt, remove the flourish.

Five principles that fall out of that:

1. **Quiet chrome, loud signal.** Backgrounds, borders, and inactive UI are near-monochrome graphite. Color is spent only on things that mean something: the active pane, a link, a syntax token, a status.
2. **Dense but breathable.** Tight vertical rhythm and small UI text, but generous line-height in prose (1.7) so long reading sessions don't fatigue.
3. **One accent family, used sparingly.** A single green primary + a cyan secondary + a warm amber. Never a rainbow. Semantic red/orange/violet exist only for meaning (error, value, keyword).
4. **Monospace as a UI voice, not just for code.** Structural labels (section headers, tab titles, breadcrumbs, metadata keys) use the mono font in small uppercase with wide tracking — the "terminal manifest" idiom. Prose and long-form body stay in a humanist sans/serif.
5. **Flat, not glassy.** No gradients as decoration, no drop shadows except functional elevation (menus, modals). Depth comes from layered flat surfaces and hairline borders.

---

## 2. Color system

The theme is built on **semantic tokens** that resolve to different raw values in dark and light mode. Always design against the token names; the raw hex is per-mode. This is the whole point of the system — a consumer wires up the token names once and gets both modes.

### 2.1 Accent ramp (mode-aware)

Three accents. In light mode they darken to stay legible on light surfaces.

| Token | Role | Dark | Light |
|---|---|---|---|
| `accent` (primary) | Prompts, active tab, primary action, H2, string literals, success | `#63f2ab` (mint green) | `#007a4d` |
| `accent-alt` (secondary) | Links, H3, metadata, functions, quiet highlights | `#6bdcff` (cyan) | `#006f9e` |
| `warm` | Warnings, text-highlight, H4, unresolved links, properties | `#f0c674` (amber) | `#a46600` |

Semantic hues (used only where they carry meaning — errors, syntax):

| Token | Dark | Light | Used for |
|---|---|---|---|
| `red` | `#ff6e7a` | `#c8324c` | Errors, cancelled state, code tags |
| `orange` | `#f7a35c` | `#b65800` | Code values / numbers |
| `violet` | `#b78cff` | `#7357b8` | Code keywords |

**Rule:** the primary accent should be derivable from / overridable by the host's own accent setting where one exists (e.g. an HSL triple), falling back to the mint green. Don't hard-clobber a user's accent choice.

### 2.2 Surfaces (graphite ramp)

Five background steps from deepest to lightest, plus borders. Depth = stepping through these, never shadows.

| Token | Dark | Light | Role |
|---|---|---|---|
| `bg-0` | `#090c0d` | `#f5f7f4` | Page / editor background (deepest dark / lightest light) |
| `bg-1` | `#0e1214` | `#edf2ee` | Sidebars, secondary panels, title/tab bar |
| `bg-2` | `#13191c` | `#e2eae5` | Form fields, code block body, table header |
| `bg-3` | `#182024` | `#d6e1db` | Hover states, active tab block, code header band |
| `bg-4` | `#202a2f` | `#c8d5cf` | Highest raised surface |
| `border` | `#2a363d` | `#bfcbc5` | Default hairline (1px) |
| `border-strong` | `#39484f` | `#9daea7` | Hover / emphasized dividers |

**Layering rule (important for panels):** a nested panel steps to the next lighter surface in dark mode and the next *darker* surface in light mode — the ordinal always means "further from the page." A code block is a good test case: page → body one step in → header band one step further. Keep at least ~1.1:1 luminance contrast between adjacent layers or they blur together (this is the exact bug that made the light-mode code block look flat before being deepened).

### 2.3 Text

| Token | Dark | Light | Role |
|---|---|---|---|
| `text-normal` | `#dce4df` | `#17201d` | Primary body text |
| `text-soft` | `#b4c3bd` | `#34443f` | Secondary text, code default |
| `text-muted` | `#879994` | `#60706a` | Labels, inactive tabs, captions |
| `text-faint` | `#63736f` | `#81918a` | Separators, icons, placeholder, glyphs |
| `text-on-accent` | `#07100d` | `#f9fbf8` | Text sitting on an accent fill |

**Contrast:** target WCAG AA (4.5:1) for body and small text. Note that a bright dark-mode accent (e.g. mint on near-black) often needs to be *darkened* — not lightened — for light mode to keep small-text contrast; the light accents above are chosen for exactly this. Verify small colored text (tags, labels) specifically, not just body.

### 2.4 Derived tints

Translucent tints are generated from the accents rather than hand-picked, so they track a changed accent automatically. Pattern: `mix(accent, transparent, N%)`.

| Purpose | Recipe |
|---|---|
| Selection background | `accent` @ ~20% (dark) / ~17% (light) |
| Active-line / row highlight | `accent-alt` @ ~7.5% |
| Nav item active background | `accent` @ ~10.5% |
| Blockquote background | `accent` @ ~7% |
| Tag background / border | `accent` @ 13% fill, 28% border |
| Text highlight (mark) | `warm` @ ~22% |
| Focus ring | `accent` @ ~18%, as a 2px outline |

Provide static fallbacks where the mixing function may be unsupported (old engines): a flat pre-mixed hex for the load-bearing ones (selection, hover, glow).

---

## 3. Typography

Three font roles. The consumer supplies actual families; these are the defaults and the *usage rules* matter more than the specific fonts.

| Role | Default stack | Used for |
|---|---|---|
| `font-mono` | Berkeley Mono → JetBrains Mono → Cascadia Code → IBM Plex Mono → SFMono-Regular → Consolas → monospace | Code, and all "manifest" UI labels |
| `font-ui` | Inter → SF Pro Text → Segoe UI → system-ui → sans-serif | Interface chrome, nav, prose (interface) |
| `font-text` | same as mono here (editor is monospace by design) | Editor / reading body |

**Respect host font settings:** if the platform lets a user pick fonts, the theme's stacks should be a *fallback layer*, not an override. Users' choices win.

### The "terminal manifest" label idiom

This is the theme's signature UI move — reuse it for any structural label:

```
font: var(--font-mono);
font-size: 10.5px;          /* 9.5–11px depending on prominence */
font-weight: 600–700;
letter-spacing: 0.06–0.09em;
text-transform: uppercase;
color: text-muted;          /* or text-faint for the quietest */
```

Applied to: section/property headings ("PROPERTIES"), code-block language labels, tab titles, breadcrumb segments. It's what makes disparate UI regions feel like one system.

### Prose type scale

| Element | Size | Weight | Color | Notes |
|---|---|---|---|---|
| Body | 15px | 400 | text-normal | line-height 1.7 |
| Inline title / H1 | 2.1em / 1.72em | 760 | text-normal | H1/H2 get a fading underline rule |
| H2 | 1.38em | 740 | **accent** | |
| H3 | 1.16em | 720 | **accent-alt** | |
| H4 | 1.04em | 700 | **warm** | |
| H5–H6 | 0.95em | 700 | text-muted | uppercase, wide tracking |
| Inline code | 0.92em | — | code-default on bg-2, hairline border, pill radius | mono |

Line-height: `1.7` normal (prose), `1.45` tight (UI), `1.62` code.

---

## 4. Shape, spacing, motion

| Property | Value | Notes |
|---|---|---|
| Corner radius (base) | 6px | `radius-s` = 4px, `radius-m` = 6px, `radius-l` = 8px |
| Pill radius | 999px | toggles, slider thumbs |
| Tag / chip radius | 4px (`radius-s`) | tags, small chips — square with rounded corners, not oval |
| Checkbox radius | 4px | |
| Border width | 1px hairline everywhere | the primary way surfaces are defined |
| Border on single-sided accents | 0 radius | rounded corners only with full borders |
| Pane shadow | `0 20px 60px rgba(0,0,0,0.22)` | menus/modals/popovers only — the one place shadows are allowed |
| Optional "soft neon" glow | `0 0 18px mix(accent, transparent, 28%)` | opt-in accent glow on active elements; off by default |

**Motion:** transitions only on interactive state changes (background, color, border, box-shadow), ~120ms ease. **Gate all motion behind `prefers-reduced-motion`** — no animation for users who opt out.

**Density:** offer a compact mode that tightens UI font sizes and control heights (~15% smaller) without touching prose readability.

---

## 5. Component patterns

How the tokens compose into recurring UI, described behaviorally so they port to any widget system:

- **Active pane/tab:** solid `bg-3` block fill + accent-colored mono uppercase label. Seated flush in its bar (no detached floating outline). Optional top accent line + glow when "soft neon" is on.
- **Inactive tab/nav item:** transparent background, `text-muted` label; on hover → subtle `bg` hover tint + brighter text; active nav item gets an inset accent left-bar (2px).
- **Panels (code blocks, callouts, embeds, metadata):** hairline border, `radius-m`, background one surface-step from the page. Structural header uses the manifest label idiom, separated by a faded hairline.
- **Callouts:** tinted from the callout's semantic color — `mix(color, page, ~9%)` fill, `mix(color, border, ~34%)` border, 3px solid color left-bar, no shadow.
- **Inputs:** `bg` field, hairline border, `radius`; focus = accent border + 2px accent-tint ring, no glow.
- **Primary button:** accent fill, `text-on-accent`, weight 650. Hover lightens the accent.
- **Tables:** collapsed hairline grid, `radius-m` outer, header on `bg-2`, alternating row tint at ~2.5–3% opacity, hover row tint from `accent-alt` @ ~7%.
- **Tags/chips:** accent tint fill + border, `radius-s` (square with rounded corners), small; hover inverts to solid accent + `text-on-accent`. Reserve the full pill radius for toggles and slider thumbs.
- **Checkboxes/states:** drive fill and border from a single `checkbox-color` variable so per-state variants (done/cancelled/deferred/important → accent/red/cyan/amber) just reassign that one variable rather than restyling the control. This is the cleanest way to expose stateful color.
- **Scrollbars:** thin (10px), transparent track, thumb = `text-faint` @ ~46% with a transparent border via background-clip so it reads as inset.

---

## 6. Both modes are mandatory

Every token above has a dark and light value. Design and verify in both. Common pitfalls this theme hit and fixed:

- A dark-mode accent usually must **darken** (not lighten) for light mode to keep contrast.
- Layered surfaces need enough luminance gap in *both* modes — light mode is where panels tend to collapse into the page.
- If the platform applies its own dark-mode filter to embedded content (Obsidian pixel-inverts Mermaid, for example), account for it rather than fighting it with a counter-filter.

Provide `color-scheme: dark` / `light` (or the platform equivalent) so native controls (scrollbars, form widgets) match.

---

## 7. What to hand a tool

When asking another system to "make this theme," give it:

1. **Section 1** (philosophy) verbatim — it resolves ambiguous judgment calls.
2. **Section 2** color tables — the token→value map for both modes.
3. **Section 3** the three font roles + the manifest label idiom.
4. **Sections 4–5** for shape/motion and the component behaviors relevant to that platform.
5. A note on which surfaces exist in the target (a terminal has far fewer than an editor) so it maps tokens to what's actually there.

The deliverable from any consumer should be checkable against Section 6: does it work in both modes, with adequate contrast, quiet chrome, and color spent only on signal?
