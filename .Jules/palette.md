# Palette's Journal

## 2024-05-22 - Missing ARIA Labels on Icon-Only Buttons
**Learning:** The application relies heavily on icon-only buttons (Phosphor icons) for critical actions like delete, edit, and print. These buttons often lack text content or `aria-label`s, making them inaccessible to screen reader users.
**Action:** Always verify icon-only buttons have an explicit `aria-label` describing the action. Add `title` attributes as well for mouse users to see tooltips.
