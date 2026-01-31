## 2024-05-23 - Extending i18n for Accessibility Attributes
**Learning:** The existing `App.applyLanguage()` function only updated `innerText` and `placeholder`. This made it impossible to localize `aria-label` or `title` attributes on static HTML elements without writing custom JavaScript for each element.
**Action:** Extended the i18n system to support `data-i18n-aria-label` and `data-i18n-title`, allowing fully accessible and localized static UI components by simply adding these attributes to the HTML.

## 2024-05-24 - File Upload Accessibility & UX
**Learning:** Wrapping a hidden file input (`class="hidden"`) in a label makes it accessible for mouse users but invisible to keyboard users (cannot focus).
**Action:** Use `.sr-only` class to hide the input visually while keeping it in the DOM for keyboard focus. Added `focus-within` ring to the parent label to provide visual focus indication when the invisible input is focused. Also added Drag & Drop support to the label for better UX.
