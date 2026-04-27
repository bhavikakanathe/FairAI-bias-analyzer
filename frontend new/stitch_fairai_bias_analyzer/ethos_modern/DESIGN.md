---
name: Ethos Modern
colors:
  surface: '#f8f9ff'
  surface-dim: '#cbdbf5'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e5eeff'
  surface-container-high: '#dce9ff'
  surface-container-highest: '#d3e4fe'
  on-surface: '#0b1c30'
  on-surface-variant: '#45464d'
  inverse-surface: '#213145'
  inverse-on-surface: '#eaf1ff'
  outline: '#76777d'
  outline-variant: '#c6c6cd'
  surface-tint: '#565e74'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#131b2e'
  on-primary-container: '#7c839b'
  inverse-primary: '#bec6e0'
  secondary: '#0058be'
  on-secondary: '#ffffff'
  secondary-container: '#2170e4'
  on-secondary-container: '#fefcff'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#00201d'
  on-tertiary-container: '#0c9488'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2fd'
  primary-fixed-dim: '#bec6e0'
  on-primary-fixed: '#131b2e'
  on-primary-fixed-variant: '#3f465c'
  secondary-fixed: '#d8e2ff'
  secondary-fixed-dim: '#adc6ff'
  on-secondary-fixed: '#001a42'
  on-secondary-fixed-variant: '#004395'
  tertiary-fixed: '#89f5e7'
  tertiary-fixed-dim: '#6bd8cb'
  on-tertiary-fixed: '#00201d'
  on-tertiary-fixed-variant: '#005049'
  background: '#f8f9ff'
  on-background: '#0b1c30'
  surface-variant: '#d3e4fe'
typography:
  display:
    fontFamily: Inter
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 44px
    letterSpacing: -0.02em
  h1:
    fontFamily: Inter
    fontSize: 30px
    fontWeight: '600'
    lineHeight: 38px
    letterSpacing: -0.01em
  h2:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  h3:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
    letterSpacing: '0'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
    letterSpacing: '0'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
    letterSpacing: '0'
  label-md:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
  code:
    fontFamily: monospace
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
    letterSpacing: '0'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 40px
  xl: 64px
  gutter: 24px
  margin: 32px
---

## Brand & Style

The brand personality of this design system is rooted in **Precise Accountability**. It balances the rigor of academic research with the efficiency of cutting-edge AI technology. The target audience—data scientists, policy makers, and engineers—requires a UI that conveys stability and objectivity.

The design style follows a **Corporate Modern** approach with **Minimalist** execution. It prioritizes clarity over decoration, using ample whitespace to reduce cognitive load during complex data analysis. Visual elements are structured to feel engineered and intentional, evoking a sense of "unbiased transparency."

## Colors

The palette is anchored by **Deep Navy** to establish authority and trust. **Professional Blues** are used for primary actions and interactive states, ensuring a familiar SaaS feel. 

**Teal** is reserved exclusively for "success" metrics, algorithmic growth, and fairness improvements, acting as a positive visual reinforcer. Conversely, **Subtle Oranges and Reds** are used sparingly for highlighting bias, warning thresholds, and high-risk data points. This creates a clear semantic distinction between safe and concerning metrics. The background utilizes cool grays to maintain a clinical, focused environment.

## Typography

This design system utilizes **Inter** for all interface elements to leverage its exceptional legibility in data-heavy contexts. The type hierarchy is strictly defined to help users navigate complex information architectures. 

- **Headlines:** Use tighter letter spacing and semi-bold weights to create a strong visual anchor.
- **Body Text:** Standard weights with generous line heights to ensure long-form reports are readable.
- **Labels:** Uppercase styles are used for secondary metadata and chart axes to differentiate them from actionable content.
- **Tabular Figures:** Ensure `tnum` (tabular figures) OpenType features are enabled for all data tables to keep numeric values aligned and comparable.

## Layout & Spacing

This design system employs a **Fluid Grid** model based on a 12-column system. It is designed to maximize the utility of wide-screen monitors common in data science workflows.

- **Rhythm:** An 8px baseline grid governs all vertical and horizontal spacing.
- **Density:** The layout supports "High Density" views for data exploration and "Standard" views for executive summaries. 
- **Containers:** Content is housed in flexible containers that snap to gutter-defined boundaries, ensuring mathematical alignment across the entire dashboard.

## Elevation & Depth

To maintain an academic and minimalist aesthetic, this design system avoids heavy shadows. Instead, it uses **Tonal Layers** and **Low-Contrast Outlines**.

1.  **Level 0 (Background):** The lowest surface, typically a very light cool gray.
2.  **Level 1 (Cards/Panels):** Pure white surfaces with a 1px border (#E2E8F0). This is the primary work surface.
3.  **Level 2 (Dropdowns/Modals):** Subtle, highly diffused ambient shadows (0px 4px 20px rgba(15, 23, 42, 0.08)) to indicate temporary interaction.

This "flat-plus" approach keeps the interface feeling lightweight and focuses the user's eye on the data visualizations rather than the UI chrome.

## Shapes

The shape language is **Soft (0.25rem)**. This slight rounding provides a modern touch without sacrificing the "serious" feel of a professional tool. 

- **Standard Components:** Buttons, input fields, and tags use the base 4px radius.
- **Large Components:** Cards and main layout panels may use `rounded-lg` (8px) to softly frame large datasets.
- **Data Points:** In visualizations, markers should remain sharp or use minimal rounding to preserve the precision of the coordinate mapping.

## Components

### Buttons
Primary buttons use the Deep Navy background with white text for maximum contrast. Secondary buttons are outlined with a 1px slate border. Ghost buttons are used for tertiary actions like "Cancel" or "Reset Filters."

### Cards
Minimalist card structures are the primary vessel for data. They feature a 1px border and no shadow. Headers within cards should be separated by a subtle horizontal rule to distinguish the title from the visualization.

### Data Visualizations
Charts must use the semantic color palette:
- **Trend Lines:** Professional Blue.
- **Parity/Fairness Zones:** Teal fills with low opacity.
- **Bias Indicators:** Orange or Red strokes.
- **Axes:** Light gray lines with `label-md` typography.

### Input Fields & Controls
Form controls use a "High-Tech" functional style: sharp focus states using the Professional Blue, and clear error states using the Error Red. Toggle switches for AI parameters use the Teal color when enabled to signify active "growth/fairness" features.

### Chips & Tags
Used for filtering datasets and indicating model status. Success tags use a light teal background with dark teal text; warning tags use a light orange background with dark orange text.