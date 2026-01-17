## 2024-10-24 - Interactive Divs Accessibility
**Learning:** This app frequently uses `div`s with `onclick` handlers for main interactive elements (e.g., Saved PO cards, Item cards) without keyboard support. This makes core functionality inaccessible to keyboard users.
**Action:** When identifying such patterns, explicitly add `role="button"`, `tabindex="0"`, `onkeydown` handlers (for Enter/Space), and visible focus indicators (e.g., `focus:ring`) to ensure keyboard accessibility.
