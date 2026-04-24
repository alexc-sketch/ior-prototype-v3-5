# Copywriting Feedback Brief: IOR Enhanced Copy Updates

**Project:** IOR Prototype v3.5
**Target Document:** `IOR_Enhanced_Copy_All_Pages.docx`
**Author:** Manus AI
**Date:** April 2026

This brief outlines required updates to the master copy document to align with recent structural, UX, and design system pivots. The copywriting bot must process the entire document and apply these structural changes to every page template.

---

## 1. The Lead Capture Pivot (Consolidating Forms & Assets)

The dedicated `/download/` landing page pattern has been cancelled. The client has built smart HubSpot forms capable of handling both general enquiries and gated asset requests simultaneously from a single form on the page.

### 1.1 Collapse the "Gated Asset" and "HubSpot Form" Blocks
Currently, the copy document features two separate blocks at the base of most spoke pages:
1. `### Gated Asset Download` (Card layout, IOR blue background)
2. `### HubSpot Form Embed` (Full-width, light grey background, centred layout)

**Action:** These must be collapsed into a single `### Lead Capture Block`.
- **Design Note Update:** Replace the old design notes with: `[DESIGN NOTE] Split-layout lead capture block. Left column: Contextual messaging and 3 minimalistic callouts. Right column: HubSpot form. Wrapper uses dynamic silo theming (e.g., IOR Blue border for Ground Fuels, Aviation Gold for Aviation).`

### 1.2 Dynamic Contextual Messaging
The form titles are currently generic (e.g., "Talk to an aviation fuel specialist" or "Get a quote for your site"). The new pattern requires the headline and sub-copy to dynamically reference **both** the general enquiry context and the specific gated asset for that page.

**Action:** Rewrite the `[Form Title H2]` and `[Form Subtitle]` for every page to combine the asset offer with the enquiry prompt.
- **Example (Aviation Network):**
  - *Old:* "Set up your aviation fuel account."
  - *New:* "Get the Aviation Network Directory + talk to our team."
  - *New Subtitle:* "Download the complete directory of 32+ IOR airport locations and speak with an aviation specialist about setting up your fleet account."

### 1.3 Add Minimalistic Callouts
The left side of the new split-layout lead capture block requires a maximum of three short, single-line callouts detailing what the user gets by submitting the form.

**Action:** Add a `[Callouts]` section to the new Lead Capture Block for every page.
- **Example (Diesel Network):**
  - `[Callout 1]` Full network directory and site coordinates
  - `[Callout 2]` RFID and fleet account setup guide
  - `[Callout 3]` Site facilities and B-Double access info

### 1.4 Update CTA Destinations
All "Download the Brochure →" or "Download the Directory →" CTAs higher up the page currently imply a separate action or page load.

**Action:** Update the destination of these CTAs to indicate an anchor link to the form section at the bottom of the page.
- **Example:** Change `[CTA] Download the Brochure → /download/diesel-network-brochure/` to `[CTA] Download the Brochure ↓ #lead-capture`.

---

## 2. Hero Pattern Updates

The copy document currently specifies a "Full-bleed background image" for every hero section. This conflicts with the newly established canonical pattern for network/coverage pages.

**Action:** Update the `[DESIGN NOTE]` for the hero section on specific pages.
- **Network Pages (03a Diesel Network, 04a Aviation Network):** Change the design note to: `[DESIGN NOTE] Abstract SVG Australia map hero with pulsing network dots and 4 callout grid. No background image.`
- **All Other Pages:** Retain the image hero, but ensure the design note explicitly prohibits gradients: `[DESIGN NOTE] Full-bleed background image. No gradients permitted on hero imagery.`

---

## 3. Silo Theming & Colour Cues

The design system enforces strict silo theming. Ground Fuels uses IOR Blue (`#0355A3`), while Aviation uses Aviation Gold (`#D98300` / `--av-gold`).

**Action:** Audit all `[DESIGN NOTE]` references to colour across the Aviation pages (04 to 04d).
- Change any mention of "IOR blue background" (e.g., on Quick Links Bars, Pre-Footer CTA Strips, or Testimonial Cards) to "Aviation Gold background" or "Dark Navy background with Aviation Gold accents" as appropriate for the Aviation silo.

---

## 4. Tone of Voice & Submit Buttons

The brand's tone of voice must remain professional, innovative, reliable, and 'adult'.

**Action:** Review the `[Submit CTA]` labels on the new Lead Capture Blocks.
- "Submit Enquiry" feels formal and dated. Update these to be more action-oriented and specific to the page's dual purpose.
- **Examples:** "Download Directory & Enquire", "Get the Brochure", or "Request Supply & Download".

---

## Summary Checklist for the Copywriting Bot

1. [ ] Replace all separate Gated Asset and HubSpot Form blocks with a single `### Lead Capture Block`.
2. [ ] Rewrite Lead Capture headlines/subtitles to reference both the asset and the enquiry.
3. [ ] Add 3 minimalistic callouts to every Lead Capture Block.
4. [ ] Update all download/enquiry CTA destinations to `#lead-capture`.
5. [ ] Update hero design notes for Network pages (abstract map) and prohibit gradients on image heroes.
6. [ ] Correct colour references in Aviation design notes to reflect Aviation Gold theming.
7. [ ] Sharpen `[Submit CTA]` labels to be action-oriented.
