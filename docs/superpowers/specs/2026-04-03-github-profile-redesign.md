# GitHub Profile Redesign Spec
Date: 2026-04-03

## Overview

Full redesign of the `yagami1997` GitHub profile README. The goal is to improve structure, reduce redundancy, and elevate the Projects section — while preserving the current visual identity and all existing contact content.

## Target Audience

- **B · AI tech people** — interested in agent-native workflows, open-source AI, builder mindset
- **C · Recruiters / potential employers** — evaluating execution capability and project track record

## Design Principles

- Keep the existing color scheme: dark background, teal/blue/gold (`#0f172a`, `#0f766e`, `#0ea5e9`, `#f59e0b`)
- No dynamic widgets (no GitHub stats, no streak graphs, no trophies) — anti-vanity-metric philosophy
- Consistent with "Systems Over Hype" brand: clean, direct, no decoration for decoration's sake

## Section-by-Section Decisions

### 1. Header Banner
**Keep as-is.** Capsule-render waving banner with current colors and text.

### 2. Badges (×3)
**Keep as-is.** Agent-Native Execution / Open-Source Pragmatist / Updated date.

### 3. Intro Text
**Light tightening only.** The heading and paragraph copy are solid. Minor cleanup for concision if needed, no structural change.

### 4. About (3-column table)
**Keep as-is.** Building / Shifting Toward / Choosing For — works well.

### 5. How I Work *(merged section)*
**Merge "From Chat to Agent" + "How I Build" → one section.**

The two existing 4-column tables are visually identical in structure and partially overlap in content. Merge into a single "How I Work" section using **Layout C (left-label list)**:

```
DESIGN      Make the task concrete enough to execute
DECOMPOSE   Break goals into units with clean boundaries
ASSIGN      Best-fit model, tool, or runtime per unit
VERIFY      Tests, outputs, and human judgment
```

Rationale: consistent with anti-show-off philosophy, stable across screen sizes, reads as confident and direct.

### 6. Current Stack (badges)
**Keep as-is.** Four `for-the-badge` style badges.

### 7. Selected Projects *(upgraded)*
**Upgrade to Layout C (single-column with depth).**

Each project gets: name + status label on one line, followed by 2-3 sentences covering what it does and *why it was built*. This is the most important section for both target audiences.

Layout format (exact copy to be finalized during implementation, based on current README descriptions):
```
Surgemac                                    ● Active Rebuild
Rebuilt from the ground up with cleaner architecture and tighter product discipline.
Represents how I currently think: remove noise, build for the long term.

TradeMind                                   ◆ AI Systems
Turns models into usable systems with structured workflows — not a chatbot,
a decision-support tool with operational value.

esimswap                                    ✓ Utility
Small, precise, practical. Exactly the kind of narrow-scope software that gets used.
```

Note: the above is draft copy derived from the existing README. Final wording stays close to this but can be polished during implementation.

### 8. Contact *(visual restructure, content unchanged)*
**All three elements must remain: Ko-fi, Patreon, GPG.** Restructured into three visually equal sub-sections:

1. **Support** — Ko-fi + Patreon as large `for-the-badge`-sized buttons (current size), side by side
2. **Secure Contact** — GPG button (same large size), with existing description text
3. **GitHub** — `@yagami1997` link as a smaller outlined badge, followed by footer text

The divider line (`---`) between each sub-section creates visual separation without implying hierarchy.

## What Does NOT Change

- Color scheme and brand identity
- Header banner
- Badges
- About section
- Current Stack section
- All contact content (Ko-fi, Patreon, GPG links and descriptions)
- The "Systems Over Hype" tagline and core copy

## Summary of Changes

| Section | Change |
|---------|--------|
| How I Work | Merge two 4-col tables → one left-label list |
| Projects | Upgrade from 3-col grid → single-column with "why I built it" |
| Contact | Visual restructure: 3 equal sub-sections, large support buttons |
