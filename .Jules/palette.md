## 2024-05-22 - Vanilla JS Architecture
**Learning:** The application logic is inside a `type="module"` script, meaning internal classes like `Core` and `DB` are not globally accessible. `window.App` is the only exposed interface.
**Action:** When writing verification scripts or testing console commands, use `window.App` methods or native browser APIs (like `indexedDB`) instead of trying to access internal classes directly.
