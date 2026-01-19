## 2026-01-19 - Vanilla JS Single File Repo
**Learning:** This repository is a vanilla JavaScript SPA contained primarily in `index.html` without a package manager or build step. Standard commands like `pnpm lint` or `pnpm test` are not applicable.
**Action:** When working on this repo, rely on careful manual code editing and verification via reading files, as automated linting/testing tools are absent. Ensure all changes are self-contained within `index.html`.

## 2026-01-19 - Playwright Verification of Vanilla JS
**Learning:** Verified frontend changes in a vanilla JS app without a build step by loading `index.html` via `file://` protocol in Playwright. Drove the UI state programmatically (e.g., creating items via forms) to reach deep UI states (modals) instead of mocking complex internal state.
**Action:** Use this pattern for future verifications: Drive the UI to generate state rather than trying to inject state into internal variables which might be inaccessible.
