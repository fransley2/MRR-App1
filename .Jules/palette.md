## 2024-05-23 - Extending i18n for Accessibility Attributes
**Learning:** The existing `App.applyLanguage()` function only updated `innerText` and `placeholder`. This made it impossible to localize `aria-label` or `title` attributes on static HTML elements without writing custom JavaScript for each element.
**Action:** Extended the i18n system to support `data-i18n-aria-label` and `data-i18n-title`, allowing fully accessible and localized static UI components by simply adding these attributes to the HTML.

## 2024-05-24 - Centralized Modal Management
**Learning:** The application uses distributed `onclick` handlers to toggle `hidden` classes for modals, with no central state management. This makes implementing global behaviors like "Close on Escape" difficult without manually checking the DOM state of every possible modal.
**Action:** Implemented a centralized `keydown` listener in `App.init` that checks modal visibility in Z-index priority order. Future modals must be added to this list to be accessible via keyboard.
