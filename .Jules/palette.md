## 2024-05-22 - Interactive Cards & Icon Buttons
**Learning:** This application relies heavily on `div` elements with `onclick` handlers for core interactions (opening POs, selecting items) and icon-only buttons for actions. This makes the app inaccessible to keyboard and screen reader users.
**Action:** When creating interactive cards, always wrap them in semantic buttons or add `role="button"`, `tabindex="0"`, and `onkeydown` handlers. For icon-only buttons, always ensure `aria-label` and `title` attributes are present.
