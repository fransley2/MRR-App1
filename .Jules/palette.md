## 2024-05-22 - Invisible Hover Controls
**Learning:** Interactive elements that are only visible on hover (opacity-0 group-hover:opacity-100) are inaccessible to keyboard users as they remain invisible when focused.
**Action:** Always add `focus:opacity-100` (or similar focus visibility) alongside hover effects for controls that are hidden by default.

## 2024-05-22 - Icon-Only Buttons
**Learning:** Icon-only buttons are rampant in this codebase. They often lack `aria-label` or `title`, making them mystery meat navigation for screen readers.
**Action:** Ensure every icon-only button has an `aria-label` describing its action.
