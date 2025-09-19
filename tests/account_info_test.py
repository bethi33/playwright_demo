from playwright.sync_api import sync_playwright, expect
from conftest import browser

def test_signup_user_success():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context(viewport=None)
        page = browser.new_page()

        page.goto("https://automationexercise.com", timeout=60000, wait_until="networkidle")

        assert page.locator('body').is_visible()

        page.click('a[href="/login"]')

        assert page.locator('h2:has-text("New User Signup!")').is_visible()

        page.fill('input[name="name"]', 'Test33User')
        page.fill('input[data-qa="signup-email"]', 'tet333us232er123@example.com')

        page.click('button[data-qa="signup-button"]')

        page.wait_for_selector('b:has-text("Enter Account Information")', timeout=30000)

        page.check('input[id="id_gender1"]') 
        page.fill('input[id="password"]', 'Test@1234')
        page.select_option('select[id="days"]', '10')
        page.select_option('select[id="months"]', '5')
        page.select_option('select[id="years"]', '1990')

        page.check('input[id="newsletter"]')

        page.check('input[id="optin"]')

        page.fill('input[id="first_name"]', 'Test')
        page.fill('input[id="last_name"]', 'User')
        page.fill('input[id="company"]', 'TestCompany')
        page.fill('input[id="address1"]', '123 Test Street')
        page.fill('input[id="address2"]', 'Suite 456')
        page.select_option('select[id="country"]', 'Canada')
        page.fill('input[id="state"]', 'Ontario')
        page.fill('input[id="city"]', 'Toronto')
        page.fill('input[id="zipcode"]', 'M4B1B3')
        page.fill('input[id="mobile_number"]', '1234567890')

        page.click('button[data-qa="create-account"]')

        page.wait_for_selector('b:has-text("Account Created!")', timeout=30000)

        page.click('a[data-qa="continue-button"]')

        assert page.locator('a:has-text("Logged in as Test33User")').is_visible()

        print("User signup successful")
        print("User: Test33User")
        browser.close()