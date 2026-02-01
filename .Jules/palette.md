## 2024-05-23 - Extending i18n for Accessibility Attributes
**Learning:** The existing `App.applyLanguage()` function only updated `innerText` and `placeholder`. This made it impossible to localize `aria-label` or `title` attributes on static HTML elements without writing custom JavaScript for each element.
**Action:** Extended the i18n system to support `data-i18n-aria-label` and `data-i18n-title`, allowing fully accessible and localized static UI components by simply adding these attributes to the HTML.

## 2024-10-24 - File Input Accessibility
**Learning:** Wrapping a `hidden` file input in a label makes it inaccessible to keyboard users because `display: none` removes it from the accessibility tree.
**Action:** Use `sr-only` (visually hidden but accessible) for the input and apply `focus-within` styles to the parent label to provide a focus indicator.
