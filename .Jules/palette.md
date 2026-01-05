## 2024-05-22 - Interactive Divs Accessibility
**Learning:** The application heavily relies on `div` elements with `onclick` handlers for critical interactions (Saved POs, Item Lists), rendering them inaccessible to keyboard users.
**Action:** When identifying interactive cards, always ensure they have `role="button"`, `tabindex="0"`, and `onkeydown` handlers for Enter/Space keys.
