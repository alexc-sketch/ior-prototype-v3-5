Global Components Reference: https://alexc-sketch.github.io/ior-prototype-v3-5/00_Global_Components.html

# Builder Brief: Case Study Template v5

**Target File:** `CS_Template_v5.html`
**Base Template:** `IOR_Global_Template_Shell_v4.html` (Note: Case studies are marketing content, so they use the Global Shell, not the Utility Shell).

## 1. Overview & SEO
This file serves as the HTML/CSS template for single Case Study posts in WordPress. The builder must use the provided "Tin Can Bay Marina" dummy data to populate the template so it can be reviewed visually.

- **Meta Title:** Case Study: Modernising the Tin Can Bay Marina | IOR
- **Meta Description:** Modernising a 172-berth marina with new dispensing infrastructure and the Fuelcharge app, allowing the proprietor to generate 24/7 unmanned fuel sales.

## 2. Section Structure (Top to Bottom)

### Section 1: Case Study Hero
- **Background:** Full-bleed hero image (use a placeholder marina/boat image or a solid `var(--ior-navy)` if no image is available).
- **Eyebrow:** `CASE STUDY | MARINE & PORTS` (Maps to ACF: Industry Category).
- **H1:** `Modernising the Tin Can Bay Marina` (Maps to Post Title).
- **Layout:** Left-aligned text over the image. No CTA buttons required in the hero.

### Section 2: Fast Facts Bar (The "At a Glance" strip)
- **Layout:** A full-width strip immediately below the hero, using `var(--ior-blue)` background with white text.
- **Content:** A 3-column grid mapping to the ACF Fast Facts repeater.
  - Column 1: **172** | Marina Berths Serviced
  - Column 2: **24/7** | Unmanned Fuel Access
  - Column 3: **1** | Consolidated App (Fuelcharge)
- **Styling:** The number should be large and bold (e.g., 48px), with the label smaller below it.

### Section 3: Main Content Body (2-Column Layout)
- **Container:** Standard `max-width: var(--content-max)` container with generous top/bottom padding.
- **Left Column (Main Text - 70% width):**
  - **H2:** The Challenge
  - **Paragraph:** Tin Can Bay Marina is situated approximately 210 km north of Brisbane, at the southern end of the Great Sandy Strait. The marina currently services 172 short and long term berths, fishing charters, commercial and recreational boaters. In need of renovation and a technology update, Tin Can Bay Marina required a modernised fuel facility that could operate efficiently without requiring constant manual oversight from staff.
  - **H2:** The IOR Solution
  - **Paragraph:** IOR delivered a full turnkey solution to overhaul the marina’s infrastructure. We installed a new self-bunded diesel tank, tested and recertified the existing underground unleaded tank, and laid completely new underground piping and electrical controls. Most importantly, IOR integrated HyDip® fuel dispensing technology and the Fuelcharge app. This allows the marina to track fuel usage and sell fuel 24/7. Customers can now access fuel via a tag on their account or seamlessly through the Fuelcharge App, providing flexible access even when the site is unmanned.
- **Right Column (Sidebar - 30% width):**
  - **Box:** "Products Used" (Light grey background `var(--grey-50)`).
  - **Tags/Chips:** Fuelcharge, HyDip, Self-Bunded Tanks.

### Section 4: Testimonial Pull Quote
- **Background:** Full-width dark band using `var(--ior-navy)`.
- **Layout:** Centered, large italicized quote text in white.
- **Quote:** "I drive past the fuel dock on my day off and see customers using Fuelcharge to pay online. I can see the transactions and know that I'm making money even when the site is unmanned."
- **Attribution:** Chris Rippon (Bold) | Proprietor, Tin Can Bay Marina (Regular).

### Section 5: Related Case Studies (Grid)
- **Heading:** More Customer Stories
- **Layout:** Standard 3-column card grid (use the existing `.card-grid` component from the Global Shell).
- **Content:** Populate with 3 dummy cards (e.g., Flight Training Adelaide, MPC Kinetic).

### Section 6: Global Footer
- Standard 6-column footer from the Global Shell.

## 3. Golden Rules & Auditor Checklist
1. **R1:** `border-radius: 0` on all containers, cards, and images.
2. **R2:** No gradients. Solid colors only.
3. **R3:** No inline `style="..."` attributes in the HTML body.
4. **R4:** Hero must use `var(--ior-navy)` or a clean image overlay. No blue color-burn overlays.
5. **R7:** Global components (Header, Mobile Drawer, Footer) must remain exactly as they are in `IOR_Global_Template_Shell_v4.html`.
6. **R8:** Nav CTAs must use `.btn--pill`.

## 4. Dev Notes for WordPress/Elementor
- This HTML file is a static prototype for the Elementor Single Post Template.
- The "Fast Facts" section maps to an ACF Repeater field.
- The "Products Used" sidebar maps to an ACF Relationship or Taxonomy field.
- The Testimonial section should be built as a conditional Elementor block (only displays if the ACF Testimonial field is populated).
