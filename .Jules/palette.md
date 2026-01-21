## 2024-05-22 - [I18N A11y Pattern]
**Learning:** This vanilla JS app manages translations via manual DOM querySelectorAll calls. To support accessibility, extending this mechanism to handle `data-i18n-aria-label` and `data-i18n-title` allows for localizable accessible names on icon-only buttons without cluttering the JS logic significantly.
**Action:** Use `data-i18n-aria-label` for static HTML elements and `App.t('key')` for dynamic template strings to ensure consistent accessibility.
