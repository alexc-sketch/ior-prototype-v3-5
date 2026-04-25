# Design Audit & Improvement Brief: Find a Location v5

## 1. Executive Summary

The current prototype for `11d_Find_Locationv5.html` successfully implements the functional requirements (Storepoint map, PDF downloads, FAQ) but feels overly utilitarian and visually flat compared to the existing live site. As a high-value conversion page (driving fleet account applications and Fuelcharge app usage), it needs to feel more engaging, dynamic, and "fun" while strictly adhering to the v5 Golden Rules (no rounded corners, no gradients, `var(--ior-navy)` hero).

This brief outlines specific design interventions to elevate the page from a simple utility tool to a high-value brand touchpoint.

## 2. Visual Comparison: Live Site vs Prototype

### The Existing Live Site (What works well)
- **Visual Impact:** Uses a full-bleed photographic hero background (a modern IOR diesel stop at dusk) which immediately establishes context and scale.
- **Iconography:** Uses a large, friendly line-art icon (fuel bowser) next to the introductory text, breaking up the typography.
- **Whitespace:** Generous padding around the map and text elements makes the page feel breathable.

### The Current Prototype (What needs improvement)
- **Hero Section:** The solid `var(--ior-navy)` hero is compliant with the Utility Shell rules, but for a high-value page, it feels too heavy and corporate. It lacks visual context (no imagery of the actual network).
- **Map Integration:** The Storepoint map is dropped into a grey container with no visual transition from the hero. It feels like an embedded widget rather than an integrated part of the page.
- **Utility Cards:** The "Pay at the Pump" and "Open a Fleet Account" cards are functional but lack visual flair (no icons, no imagery).
- **Download Strip:** The dark navy download strip is heavy and interrupts the flow before the FAQ section.

## 3. Recommended Design Interventions

To make the page more engaging and "fun" without violating the v5 design system, the builder should implement the following changes:

### Intervention 1: Elevate the Hero Section (The "Hybrid" Hero)
While the Utility Shell dictates a solid `var(--ior-navy)` background, we can introduce visual interest by adding a **cut-out or overlapping image element** on the right side of the hero container (e.g., a high-quality, sharp-edged photo of an IOR truck stop or an isometric render of a fuel tank). 
- **Action:** Convert the hero to a 2-column layout (text left, image right). Keep the background solid navy, but use a striking, sharp-edged image to add depth.

### Intervention 2: Add "Fast Facts" Statistics Bar
Before the user interacts with the map, remind them of the scale of the network. This adds authority and visual interest.
- **Action:** Insert a full-width `var(--ior-blue)` strip immediately below the hero (above the map) with 3 large statistics:
  - **115+** Diesel Stops
  - **32+** Airport Locations
  - **24/7** Unmanned Access

### Intervention 3: Enhance the Utility Cards with Iconography
The two utility cards below the map ("Pay at the Pump" and "Open a Fleet Account") are currently text-only.
- **Action:** Add large, high-contrast line-art icons (using `var(--ior-blue)`) to the top of each card. 
  - Card 1 (Fuelcharge): A smartphone/app icon.
  - Card 2 (Fleet Account): A truck or card icon.
- **Action:** Add a subtle hover state to the cards (e.g., a slight Y-axis translation or a `var(--ior-blue)` bottom border reveal) to make them feel interactive.

### Intervention 4: Redesign the Download Strip
The current dark navy download strip is too heavy.
- **Action:** Change the background of the download strip to `var(--grey-50)` or white. Use a 2-column grid where each column features a stylized PDF document icon or a thumbnail of the directory cover, alongside the download button. This makes the assets feel tangible.

### Intervention 5: Map Container Styling
Make the map feel less like an iframe and more like a premium feature.
- **Action:** Ensure the map container has a sharp, high-contrast border (e.g., 2px solid `var(--ior-navy)`) and a subtle drop shadow to lift it off the page.

## 4. Compliance Check

All recommended interventions comply with the v5 Golden Rules:
- **R1:** All new elements (cards, images, map container) must retain `border-radius: 0`.
- **R2:** No gradients are used; depth is achieved through overlapping elements and solid colors.
- **R4:** The hero background remains solid `var(--ior-navy)`.

## 5. Next Steps for the Builder

1. Review this brief and the proposed interventions.
2. Source appropriate sharp-edged imagery for the hero section and icons for the utility cards.
3. Implement the changes on the `feature/find-location-v5` branch (or a new enhancement branch) and submit a PR for review.
