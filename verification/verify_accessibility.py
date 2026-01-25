from playwright.sync_api import sync_playwright

def verify(page):
    page.goto("http://localhost:8080")
    page.wait_for_load_state("networkidle")

    # 1. Verify Header Buttons
    # Language Toggle
    lang_btn = page.locator("button[data-i18n-aria-label='change_language']")
    assert lang_btn.get_attribute("aria-label") == "Change Language"
    print("Language toggle aria-label verified")

    # History Button
    hist_btn = page.locator("button[data-i18n-aria-label='history']")
    assert hist_btn.get_attribute("aria-label") == "History"
    print("History button aria-label verified")

    # User Profile Button
    user_btn = page.locator("button[data-i18n-aria-label='user_settings']")
    assert user_btn.get_attribute("aria-label") == "User Profile"
    print("User Profile button aria-label verified")

    # 2. Verify Search Input
    search_input = page.locator("#searchInput")
    assert search_input.get_attribute("aria-label") == "Search"
    print("Search input aria-label verified")

    # 3. Verify Dynamic Content (Saved POs - Mocking data injection if possible, or checking if empty state has issues)
    # Since we don't have data, we can't easily check dynamic buttons without injecting data.
    # However, we can check if the 'renderSavedPOs' function string in the page source contains the correct aria-label template.

    # Take screenshot of the main page
    page.screenshot(path="verification/main_page.png")
    print("Screenshot taken")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            verify(page)
        except Exception as e:
            print(f"Verification failed: {e}")
            page.screenshot(path="verification/error.png")
        finally:
            browser.close()
