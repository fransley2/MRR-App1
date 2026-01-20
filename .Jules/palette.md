## 2024-05-22 - [Hidden Interactive Controls]
**Learning:** Elements hidden with `opacity-0` and shown on `group-hover:opacity-100` are invisible to keyboard users even when focused.
**Action:** Always add `focus:opacity-100` to these elements to ensure they become visible when a keyboard user tabs to them.
