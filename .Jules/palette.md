## 2024-10-24 - Accessibility for Icon-Only Buttons
**Learning:** Standardized a pattern for localized accessible attributes on static elements. Extending `App.applyLanguage` to handle `data-i18n-title` and `data-i18n-aria-label` allows for declarative accessibility in HTML that respects the user's language preference.
**Action:** Use `data-i18n-title` and `data-i18n-aria-label` for any future static elements requiring localization, and `App.t()` for dynamic ones.
