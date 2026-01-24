## 2026-01-24 - Static HTML Translation Pattern
**Learning:** This SPA uses a mix of static HTML and dynamic JS rendering. While JS can use `${App.t()}`, static HTML elements (like modal close buttons) need a `data-i18n` attribute system. The existing system only supported text content and placeholders.
**Action:** Extended `App.applyLanguage` to support `data-i18n-aria-label` and `data-i18n-title` to allow accessible labels on static icon-only buttons without refactoring to JS rendering.
