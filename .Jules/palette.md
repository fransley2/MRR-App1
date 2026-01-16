## 2024-05-22 - Hidden Controls Accessibility
**Learning:** Controls hidden with `opacity-0` and shown on hover (`group-hover:opacity-100`) are invisible to keyboard users.
**Action:** Always add `focus:opacity-100` (or `focus-within`) when using hover-reveal patterns for interactive elements.
