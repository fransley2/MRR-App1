## 2024-05-23 - Extending i18n for Accessibility Attributes
**Learning:** The existing `App.applyLanguage()` function only updated `innerText` and `placeholder`. This made it impossible to localize `aria-label` or `title` attributes on static HTML elements without writing custom JavaScript for each element.
**Action:** Extended the i18n system to support `data-i18n-aria-label` and `data-i18n-title`, allowing fully accessible and localized static UI components by simply adding these attributes to the HTML.

## 2024-05-24 - Accessible Hover-Only Controls
**Learning:** The application uses `opacity-0 group-hover:opacity-100` for secondary actions (like delete buttons) to reduce clutter. However, this pattern makes controls completely invisible and inaccessible to keyboard users, even when focused.
**Action:** Always pair `group-hover:opacity-100` with `focus:opacity-100` on the button itself. This ensures that when a keyboard user tabs to the control, it becomes visible, preserving the "clean on idle" aesthetic while maintaining accessibility.
