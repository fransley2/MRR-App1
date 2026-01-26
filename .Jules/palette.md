## 2024-05-22 - Icon-Only Button Accessibility
**Learning:** The application heavily relies on Phosphor icons for actions (delete, edit, duplicate) without text labels. These are often implemented as `<button>` with an `<i>` inside, lacking `aria-label` or `title`. Additionally, hover-only actions (using `opacity-0 group-hover:opacity-100`) are invisible to keyboard users.
**Action:** Always add `aria-label` and `title` to icon-only buttons. For hover-reveal actions, ensure `focus:opacity-100` is added to the class list to support keyboard navigation.
