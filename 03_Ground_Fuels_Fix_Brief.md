# Builder Fix Brief: 03_Ground_Fuels.html

This brief outlines 10 specific fixes required on `03_Ground_Fuels.html` to resolve broken elements and align the page with the approved design system and global components.

## 1. Navigation Header
The current header is a static shell copied from `03a` and does not match the interactive production header from `01_Homepage.html`.
- **Action:** Replace the entire `<header role="banner">` block (lines ~1075–1130) with the exact production header markup from `01_Homepage.html`.
- **Requirement:** Ensure the mobile drawer markup and all interactive classes are included.

## 2. Hero Eyebrow
The hero eyebrow currently reads "Ground Fuels".
- **Action:** Change the text in `<p class="eyebrow">` (line ~1158) to **"Ground Fuel Solutions"**.

## 3. Hero Highlight
The H1 in the hero is missing the blue text highlight on the words "ground fuel network".
- **Action:** Wrap those words in the highlight span: `<h1>Australia's most trusted <span class="highlight">ground fuel network</span>.</h1>`

## 4. Quick Links Bar Position
The quick links bar is currently sitting between the header and the hero, and is configured as a sticky scroll-in bar (`.qlb--visible`). The client requires it to sit **above the stats and under the hero**.
- **Action:** Move the entire `<nav class="quick-links-bar">` block (lines ~1135–1145) so it sits immediately *after* the `</section>` of the hero-video and *before* the `<div class="stat-bar">`.
- **Action:** Remove the sticky JS logic for this specific bar if it interferes with its static placement, or ensure it renders statically in that position.

## 5. Stat Bar Values
The stat bar is currently showing 3 stats. It needs to show the 4 stats from the approved design.
- **Action:** Update the `<div class="stat-bar">` (lines ~1168–1175) to contain exactly these 4 items:
  1. **115+** / Network Sites Nationally
  2. **190M+** / Litres Storage Capacity
  3. **40+** / Years in Operation
  4. **24/7** / Automated Site Access
- **Action:** Ensure the CSS grid for `.stat-bar .container` is updated to `grid-template-columns: repeat(4, 1fr);` to accommodate the 4th stat.

## 6. FMT Accordion Functionality
The FMT accordion (product selector) is not functioning because the JavaScript that drives it is either missing or broken.
- **Action:** Ensure the script block at the bottom of the page correctly targets `.fmt-row` and `.fmt-accordion__img` to handle click events, active states, and image swapping. The script must be present and functional.

## 7. Steps Component Styling
The "Ready to power your business with IOR?" steps component is missing the correct background colour, card borders, and fill.
- **Action:** Ensure the `<section class="steps-section">` uses the exact CSS classes and structure from `00_Global_Components.html#steps`. The section background should be the correct template colour (e.g., `--ior-navy` or `--grey-50` depending on the global component spec), and the `.step-card` elements must have their borders and white backgrounds applied.

## 8. Missing Case Studies & Blog Containers
The page is missing the Case Studies and Blog sections that should sit between the form and the FAQs.
- **Action:** Insert the standard Case Study container and Blog container (using the global component patterns) immediately *after* the `#lead-capture` section and *before* the `.faq-section`.

## 9. Footer Hours
The footer is missing the operating hours or displaying them incorrectly.
- **Action:** Update the footer markup to match the exact production footer from `01_Homepage.html`, ensuring the operating hours are correctly formatted and displayed.

## 10. File Navigation Links
The navigation links back to the master index and design system are broken or missing from the proto-bar.
- **Action:** Ensure the `.proto-bar` at the very top of the page contains working links to:
  - `00_Master_Index.html` (Master Index)
  - `IOR_Design_System.html` (Design System)
  - `00_Global_Components.html` (Global Components)

---
**Auditor Note:** The builder must execute these 10 fixes in a single PR. No other files should be modified unless explicitly required to fix these specific issues on `03_Ground_Fuels.html`.
