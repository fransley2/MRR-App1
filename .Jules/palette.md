## 2024-05-23 - Extending i18n for Accessibility Attributes
**Learning:** The existing `App.applyLanguage()` function only updated `innerText` and `placeholder`. This made it impossible to localize `aria-label` or `title` attributes on static HTML elements without writing custom JavaScript for each element.
**Action:** Extended the i18n system to support `data-i18n-aria-label` and `data-i18n-title`, allowing fully accessible and localized static UI components by simply adding these attributes to the HTML.

## 2024-10-24 - Accessible Interactive Divs
**Learning:** The application heavily utilizes `div` elements with `onclick` handlers for primary navigation and item selection (Saved POs, List Items). These components were completely inaccessible to keyboard-only users and screen readers, lacking roles, tabindex, and keyboard event handlers.
**Action:** Established a pattern for retrofitting these "clickable divs" by adding `role="button"`, `tabindex="0"`, `onkeydown` handlers (for Enter/Space), and Tailwind `focus:ring` classes for visual feedback.
