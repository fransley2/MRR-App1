## 2024-05-22 - Icon-Only Buttons and Keyboard Focus
**Learning:** This app relies heavily on `opacity-0 group-hover:opacity-100` for action buttons (like delete) on cards. This pattern completely hides functionality from keyboard users. Adding `focus:opacity-100` is critical for keyboard accessibility.
**Action:** Always check `group-hover:opacity-100` patterns and ensure a corresponding `focus` or `focus-within` state exists.
