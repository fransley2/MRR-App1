## 2024-05-22 - Missing I18n for Attributes
**Learning:** The custom translation system (`App.applyLanguage`) only supported `innerText` and `placeholder`. This left accessibility attributes like `aria-label` and `title` hardcoded or missing on static elements, and made dynamic elements inconsistent.
**Action:** Extended `App.applyLanguage` to support `data-i18n-title` and `data-i18n-aria-label` attributes, enabling fully accessible and localized UI elements.
