## 2024-05-23 - Extending i18n for Accessibility Attributes
**Learning:** The existing `App.applyLanguage()` function only updated `innerText` and `placeholder`. This made it impossible to localize `aria-label` or `title` attributes on static HTML elements without writing custom JavaScript for each element.
**Action:** Extended the i18n system to support `data-i18n-aria-label` and `data-i18n-title`, allowing fully accessible and localized static UI components by simply adding these attributes to the HTML.
