## 2024-05-23 - Extending i18n for Accessibility Attributes
**Learning:** The existing `App.applyLanguage()` function only updated `innerText` and `placeholder`. This made it impossible to localize `aria-label` or `title` attributes on static HTML elements without writing custom JavaScript for each element.
**Action:** Extended the i18n system to support `data-i18n-aria-label` and `data-i18n-title`, allowing fully accessible and localized static UI components by simply adding these attributes to the HTML.

## 2024-05-24 - Retrofitting Keyboard Accessibility on Interactive Divs
**Learning:** The application heavily relies on `div` elements with `onclick` handlers for critical interactions (Home Logo, Item Cards), making them inaccessible to keyboard users.
**Action:** Implemented a standard pattern of adding `role="button"`, `tabindex="0"`, `onkeydown` (Enter/Space support), and `focus` styles to these elements to ensure full keyboard navigability without changing the visual design or HTML structure significantly.
