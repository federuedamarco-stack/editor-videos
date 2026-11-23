---
name: ExoMov
description: "Design system for ExoMov, a Spanish start-up that brings wearable exoskeletons to people across Spain. New, innovative, close."
colors:
  primitives:
    lime:
      "50": "#f6f6e0"
      "100": "#ecebc2"
      "200": "#dcdb8a"
      "300": "#cdcc5c"
      "400": "#bebd39"
      "500": "#a3a22b"
      "600": "#828120"
      "700": "#5c5b16"
      "800": "#454414"
      "900": "#2c2b0e"
    stone:
      "0": "#ffffff"
      "50": "#f6f6f1"
      "100": "#ecece4"
      "200": "#dcdcd1"
      "300": "#c3c3b6"
      "400": "#a9a99e"
      "500": "#85857a"
      "600": "#5a5a51"
      "700": "#3a3b35"
      "800": "#262723"
      "900": "#1b1c19"
      "950": "#121311"
  light:
    bg: "#f6f6f1"
    surface: "#ffffff"
    surface-2: "#ecece4"
    border: "#dcdcd1"
    border-strong: "#a9a99e"
    text: "#121311"
    text-muted: "#5a5a51"
    accent: "#bebd39"
    accent-hover: "#cdcc5c"
    accent-border: "#828120"
    on-accent: "#121311"
    accent-text: "#5c5b16"
    accent-soft: "#ecebc2"
    on-accent-soft: "#2c2b0e"
    focus: "#5c5b16"
    inverse: "#121311"
    on-inverse: "#f6f6f1"
    success: "#2f7d4f"
    warning: "#9a5b00"
    danger: "#b3261e"
    info: "#2c5f8a"
  dark:
    bg: "#121311"
    surface: "#1b1c19"
    surface-2: "#262723"
    border: "#3a3b35"
    border-strong: "#5a5a51"
    text: "#f6f6f1"
    text-muted: "#a9a99e"
    accent: "#bebd39"
    accent-hover: "#cdcc5c"
    accent-border: "#bebd39"
    on-accent: "#121311"
    accent-text: "#cdcc5c"
    accent-soft: "#2c2b0e"
    on-accent-soft: "#ecebc2"
    focus: "#cdcc5c"
    inverse: "#f6f6f1"
    on-inverse: "#121311"
    success: "#6fcf97"
    warning: "#f2b35a"
    danger: "#f2867d"
    info: "#8cbbe6"
typography:
  families:
    display: "'Bebas Neue', 'Bebas Neue Cyrillic', Impact, 'Arial Narrow', sans-serif"
    body: "'Figtree', 'Segoe UI', system-ui, sans-serif"
    mono: "'JetBrains Mono', ui-monospace, 'SFMono-Regular', Menlo, monospace"
  display-xl:
    fontFamily: display
    fontSize: 96px
    lineHeight: 88px
    fontWeight: 400
    letterSpacing: "0.01em"
    textTransform: uppercase
  display:
    fontFamily: display
    fontSize: 64px
    lineHeight: 60px
    fontWeight: 400
    letterSpacing: "0.01em"
    textTransform: uppercase
  h1:
    fontFamily: display
    fontSize: 44px
    lineHeight: 44px
    fontWeight: 400
    letterSpacing: "0.015em"
    textTransform: uppercase
  h2:
    fontFamily: display
    fontSize: 32px
    lineHeight: 34px
    fontWeight: 400
    letterSpacing: "0.02em"
    textTransform: uppercase
  h3:
    fontFamily: body
    fontSize: 22px
    lineHeight: 28px
    fontWeight: 700
    letterSpacing: "-0.005em"
    textTransform: none
  h4:
    fontFamily: body
    fontSize: 18px
    lineHeight: 24px
    fontWeight: 700
    letterSpacing: "0"
    textTransform: none
  body-l:
    fontFamily: body
    fontSize: 18px
    lineHeight: 28px
    fontWeight: 400
    letterSpacing: "0"
    textTransform: none
  body:
    fontFamily: body
    fontSize: 16px
    lineHeight: 24px
    fontWeight: 400
    letterSpacing: "0"
    textTransform: none
  body-s:
    fontFamily: body
    fontSize: 14px
    lineHeight: 20px
    fontWeight: 400
    letterSpacing: "0"
    textTransform: none
  label:
    fontFamily: body
    fontSize: 13px
    lineHeight: 16px
    fontWeight: 700
    letterSpacing: "0.06em"
    textTransform: uppercase
  caption:
    fontFamily: body
    fontSize: 12px
    lineHeight: 16px
    fontWeight: 500
    letterSpacing: "0.01em"
    textTransform: none
  mono:
    fontFamily: mono
    fontSize: 13px
    lineHeight: 20px
    fontWeight: 400
    letterSpacing: "0"
    textTransform: none
rounded:
  none: 0px
  sm: 4px
  md: 8px
  lg: 14px
  xl: 20px
  pill: 999px
spacing:
  "0": 0px
  "1": 4px
  "2": 8px
  "3": 12px
  "4": 16px
  "5": 24px
  "6": 32px
  "7": 48px
  "8": 64px
  "9": 96px
  "10": 128px
components:
  button-primary:
    backgroundColor: "{colors.light.accent}"
    textColor: "{colors.light.on-accent}"
    borderColor: "{colors.light.accent-border}"
    rounded: "{rounded.pill}"
    height: "48px"
    padding: "0 24px"
    typography: "{typography.label}"
  button-secondary:
    backgroundColor: "{colors.light.inverse}"
    textColor: "{colors.light.on-inverse}"
    rounded: "{rounded.pill}"
    height: "48px"
    padding: "0 24px"
    typography: "{typography.label}"
  button-outline:
    backgroundColor: "transparent"
    textColor: "{colors.light.text}"
    borderColor: "{colors.light.border-strong}"
    rounded: "{rounded.pill}"
    height: "48px"
    padding: "0 24px"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.light.accent-text}"
    rounded: "{rounded.pill}"
    height: "48px"
    padding: "0 16px"
  tag:
    backgroundColor: "{colors.light.surface-2}"
    textColor: "{colors.light.text}"
    rounded: "{rounded.pill}"
    height: "28px"
    padding: "0 12px"
    typography: "{typography.caption}"
  tag-accent:
    backgroundColor: "{colors.light.accent-soft}"
    textColor: "{colors.light.on-accent-soft}"
    rounded: "{rounded.pill}"
  input:
    backgroundColor: "{colors.light.surface}"
    textColor: "{colors.light.text}"
    borderColor: "{colors.light.border-strong}"
    rounded: "{rounded.md}"
    height: "48px"
    padding: "0 16px"
    typography: "{typography.body}"
  card:
    backgroundColor: "{colors.light.surface}"
    borderColor: "{colors.light.border}"
    rounded: "{rounded.lg}"
    padding: "24px"
  nav-item-active:
    backgroundColor: "{colors.light.accent-soft}"
    textColor: "{colors.light.on-accent-soft}"
    rounded: "{rounded.pill}"
---
# ExoMov Design System

## Overview

ExoMov brings wearable exoskeletons to people in Spain: for walking, work, hiking and rehabilitation. The system has to feel **new**, **innovative** and **close**. Technology is shown as something that helps a real person move, not as a lab object. It should not feel like a generic tech start-up, a cold medical catalogue or a sports-supplement brand.

The look is built from three things the brand already uses on social media: Bebas Neue in capitals, white, and the lime `#bebd39`. Around them sit warm stone neutrals, a near-black ink, plain Figtree body text and generous spacing. Product copy is in Spanish and addresses the reader as "tú".

Rules: no emoji, no gradients, no filler copy, no invented figures. Every value in this file matches the reference site and the CSS export.

## Colors

Lime `#bebd39` is the single brand accent. It is light (contrast 1.99:1 on white), so it is used as a **fill** carrying dark ink text (`#121311` on lime = 9.34:1), never as text or a thin line on light backgrounds. For lime-colored text on light surfaces use `accent-text` `#5c5b16` (7.09:1 on white). On dark surfaces lime and lime 300 work as text (10.1:1 on `#1b1c19`).

Lime scale: 50 `#f6f6e0` · 100 `#ecebc2` · 200 `#dcdb8a` · 300 `#cdcc5c` · 400 `#bebd39` · 500 `#a3a22b` · 600 `#828120` · 700 `#5c5b16` · 800 `#454414` · 900 `#2c2b0e`

Stone scale: 0 `#ffffff` · 50 `#f6f6f1` · 100 `#ecece4` · 200 `#dcdcd1` · 300 `#c3c3b6` · 400 `#a9a99e` · 500 `#85857a` · 600 `#5a5a51` · 700 `#3a3b35` · 800 `#262723` · 900 `#1b1c19` · 950 `#121311`

### Theme roles

| Role | Light | Dark |
|---|---|---|
| `bg` | `#f6f6f1` | `#121311` |
| `surface` | `#ffffff` | `#1b1c19` |
| `surface-2` | `#ecece4` | `#262723` |
| `border` | `#dcdcd1` | `#3a3b35` |
| `border-strong` | `#a9a99e` | `#5a5a51` |
| `text` | `#121311` | `#f6f6f1` |
| `text-muted` | `#5a5a51` | `#a9a99e` |
| `accent` | `#bebd39` | `#bebd39` |
| `accent-hover` | `#cdcc5c` | `#cdcc5c` |
| `accent-border` | `#828120` | `#bebd39` |
| `on-accent` | `#121311` | `#121311` |
| `accent-text` | `#5c5b16` | `#cdcc5c` |
| `accent-soft` | `#ecebc2` | `#2c2b0e` |
| `on-accent-soft` | `#2c2b0e` | `#ecebc2` |
| `focus` | `#5c5b16` | `#cdcc5c` |
| `inverse` | `#121311` | `#f6f6f1` |
| `on-inverse` | `#f6f6f1` | `#121311` |
| `success` | `#2f7d4f` | `#6fcf97` |
| `warning` | `#9a5b00` | `#f2b35a` |
| `danger` | `#b3261e` | `#f2867d` |
| `info` | `#2c5f8a` | `#8cbbe6` |

Usage:
- One lime element per view that matters most (main call to action, active state, key figure). Everything else is ink, stone and white.
- Light primary buttons carry a 1px `accent-border` `#828120` so the shape holds 3:1 against the page.
- Status colors are for status only (stock, order state, form errors), always paired with a word, never color alone.

## Typography

- **Display: Bebas Neue** (Bebas Neue Cyrillic on social media). Always uppercase, only at 32px and above: headlines, section titles, big numbers. Never for paragraphs, buttons smaller than 13px labels, or form text.
- **Body: Figtree.** Friendly, very legible, full Spanish accent support. Used for everything people read or tap.
- **Mono: JetBrains Mono.** Only for codes, order numbers, tokens and spec values.

| Token | Family | Size | Line height | Weight | Tracking | Transform |
|---|---|---|---|---|---|---|
| `display-xl` | Bebas Neue | 96px | 88px | 400 | 0.01em | uppercase |
| `display` | Bebas Neue | 64px | 60px | 400 | 0.01em | uppercase |
| `h1` | Bebas Neue | 44px | 44px | 400 | 0.015em | uppercase |
| `h2` | Bebas Neue | 32px | 34px | 400 | 0.02em | uppercase |
| `h3` | Figtree | 22px | 28px | 700 | -0.005em | none |
| `h4` | Figtree | 18px | 24px | 700 | 0 | none |
| `body-l` | Figtree | 18px | 28px | 400 | 0 | none |
| `body` | Figtree | 16px | 24px | 400 | 0 | none |
| `body-s` | Figtree | 14px | 20px | 400 | 0 | none |
| `label` | Figtree | 13px | 16px | 700 | 0.06em | uppercase |
| `caption` | Figtree | 12px | 16px | 500 | 0.01em | none |
| `mono` | JetBrains Mono | 13px | 20px | 400 | 0 | none |

Load: `https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Figtree:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap`

Measure 60–72 characters for body copy. Headlines are short: 2–6 words.

## Layout

- 4px base unit. Spacing scale: `space-0` 0px, `space-1` 4px, `space-2` 8px, `space-3` 12px, `space-4` 16px, `space-5` 24px, `space-6` 32px, `space-7` 48px, `space-8` 64px, `space-9` 96px, `space-10` 128px.
- Content max width 1200px, gutter 24px, 12-column grid on desktop, 4 columns on phone.
- Section rhythm: 96px between page sections on desktop, 64px on phone. 24px inside cards.
- Breakpoints: `sm` 480px, `md` 768px, `lg` 1024px, `xl` 1280px.
- Radii: `none` 0px, `sm` 4px, `md` 8px, `lg` 14px, `xl` 20px, `pill` 999px. Buttons and tags are pills (a soft, human shape); cards use `lg` 14px; inputs use `md` 8px; images inside cards use `md`.

## Elevation

The system is mostly flat: surfaces separate by color and a 1px `border`. Shadows are used sparingly and only in light mode; in dark mode elevation is shown by moving one step up the surface ladder (`bg` → `surface` → `surface-2`).

- `shadow-1`: `0 1px 2px rgba(18,19,17,0.08)`
- `shadow-2`: `0 6px 20px rgba(18,19,17,0.10)`
- `shadow-3`: `0 16px 40px rgba(18,19,17,0.14)`

- `shadow-1`: cards on hover, sticky top bar.
- `shadow-2`: menus, popovers, the product configurator.
- `shadow-3`: modals and the WhatsApp contact sheet.

## Motion

"Assist, don't push": motion follows the user and settles gently, like the device it represents.

- Durations: `fast` 120ms, `base` 200ms, `slow` 320ms, `assist` 480ms.
- Easing:
- `standard`: `cubic-bezier(0.2, 0, 0, 1)`
- `enter`: `cubic-bezier(0, 0, 0, 1)`
- `exit`: `cubic-bezier(0.3, 0, 1, 1)`
- `assist`: `cubic-bezier(0.3, 0, 0.1, 1)`
- Hover and press: `fast` + `standard`. Panels and menus: `base` + `enter` / `exit`. Progress, meters and step changes: `assist`.
- Respect `prefers-reduced-motion`: replace movement with a 0ms change or a short opacity fade.

## Components

Defined in the YAML front matter and shown live, in light and dark, on the reference site.

- **Buttons**: Primary (lime fill, ink text), Secondary (ink fill), Outline, Ghost, Danger. Height 48px (40px small). Label in Figtree 700, uppercase, tracking 0.06em. One primary per view. Focus ring: 2px `focus` with 2px offset.
- **Tags**: pills 28px tall for categories (joint, use), status tags with a colored dot plus word (En stock, Agotado, Oferta).
- **Inputs**: 48px tall, 8px radius, 1px `border-strong`, label above, help text below, error text in `danger` with the field border in `danger`. Checkbox, radio and switch share the lime fill when on.
- **Cards**: product card (image area, joint tag, name, price, CTA), info card, contact card. 14px radius, 1px border, 24px padding.
- **Data**: spec table (label / value in mono), price block (regular price struck through when on offer), stat block (Bebas number + Figtree label), progress/stepper for orders.
- **Navigation**: top bar (wordmark, links, WhatsApp CTA), tabs (underline in lime 3px), breadcrumbs, segmented filters (pill group), pagination.

## Imagery

No reference images were supplied, so no locked image styles exist yet. Until they do:
- Show real people using the devices in everyday Spanish settings (street, home, workplace, trail), at eye level, in natural light.
- Product shots on a flat stone `#ecece4` or ink `#121311` background, no gradients, no glow.
- No stock "futuristic" renders, no blue holograms, no hospital-ward clichés.

When reference images are added, each becomes a numbered locked style (Style 01, Style 02...) with a rules table and a copy-paste prompt (one subject sentence plus a fixed style block).

## Responsive Behavior

- Sidebar or top navigation collapses to a wrapped row of links below 768px.
- Grids drop from 3 or 4 columns to 2 at `md` and 1 at `sm`.
- Display sizes step down below 768px: `display-xl` 96→56px, `display` 64→44px, `h1` 44→36px. Body sizes stay the same.
- Touch targets at least 44×44px; buttons go full width in forms on phones.
- Wide tables scroll inside their own box; they never push the page sideways.

## Known Gaps

- No logo file was supplied: the reference uses a plain Bebas Neue "EXOMOV" wordmark as a stand-in.
- Bebas Neue Cyrillic (used on social) is not on Google Fonts; the web uses Bebas Neue, which covers Latin and Spanish. Use the Cyrillic cut where Cyrillic text is needed.
- No example imagery was supplied, so the Imagery section has no locked styles.
- Product specifications (weight, battery, assistance torque) were not available; pattern screens show [DATO] placeholders where real specs belong. Prices shown are those listed on exomov.com on 2026-11-20 and must be checked before reuse.
- The "should not feel like" answer was left blank; the system assumes: not a generic tech start-up and not a cold clinical catalogue.
- Lime on light backgrounds fails text contrast; follow the rules in Colors.
