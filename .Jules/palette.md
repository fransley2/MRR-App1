## 2024-05-22 - Accessibility Patterns in Vanilla JS SPA
**Learning:** Interactive elements are frequently implemented as `div`s with `onclick` handlers, requiring manual addition of `role="button"`, `tabindex="0"`, and `onkeydown` handlers for keyboard accessibility.
**Action:** Always check for `onclick` on non-button elements and upgrade them to semantic buttons or add ARIA roles.

## 2024-05-22 - Focus Visibility for Hidden Controls
**Learning:** UI controls hidden by default (e.g., using `opacity-0 group-hover:opacity-100`) must explicitly include `focus:opacity-100` to ensure visibility during keyboard navigation.
**Action:** Audit all `group-hover:opacity-100` usages and append `focus:opacity-100`.
