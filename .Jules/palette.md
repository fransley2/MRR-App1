## 2024-05-22 - [Accessibility] Icon-Only Button Pattern
**Learning:** This SPA heavily relies on icon-only buttons (Phosphor icons) which consistently lacked accessible names (`aria-label` or `title`). The existing translation system (`data-i18n`) only supported text content and placeholders, missing attributes.
**Action:** Implemented a system-wide enhancement to `App.applyLanguage` to support `data-i18n-aria-label` and `data-i18n-title`, allowing for accessible, localized names for all icon buttons without complex refactoring.
