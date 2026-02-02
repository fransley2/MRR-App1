## 2024-05-23 - Extending i18n for Accessibility Attributes
**Learning:** The existing `App.applyLanguage()` function only updated `innerText` and `placeholder`. This made it impossible to localize `aria-label` or `title` attributes on static HTML elements without writing custom JavaScript for each element.
**Action:** Extended the i18n system to support `data-i18n-aria-label` and `data-i18n-title`, allowing fully accessible and localized static UI components by simply adding these attributes to the HTML.

## 2024-05-24 - Accessible Custom File Inputs
**Learning:** The custom file upload area used `display: none` (via `.hidden`) on the file input, making it inaccessible to keyboard users. The parent label was not focusable by default.
**Action:** Replaced `.hidden` with `.opacity-0 .absolute .inset-0 .w-full .h-full .cursor-pointer` on the input to keep it in the tab order but invisible. Added `.relative` and `.focus-within:ring-*` to the parent label to provide visual focus feedback when the invisible input is focused.
