from playwright.sync_api import sync_playwright

def signup_valid_data():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context(viewport=None)
        page = browser.new_page()

        page.goto("https://automationexercise.com", timeout=60000, wait_until="networkidle")

        assert page.locator('body').is_visible()

        page.click('a[href="/login"]')

        assert page.locator('h2:has-text("New User Signup!")').is_visible()

        page.fill('input[name="name"]', 'uefhniof')
        page.fill('input[data-qa="signup-email"]', 'john123@gmail.com')
        page.click('button[data-qa="signup-button"]')
        assert page.locator('b:has-text("Enter Account Information")').is_visible()
        print("User registered successfully")

def test_signup_with_existing_email():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context(viewport=None)
        page = browser.new_page()

        page.goto("https://automationexercise.com", timeout=60000, wait_until="networkidle")

        assert page.locator('body').is_visible()

        page.click('a[href="/login"]')

        assert page.locator('h2:has-text("New User Signup!")').is_visible()

        page.fill('input[name="name"]', 'fireai')
        page.fill('input[data-qa="signup-email"]', 'fireai@gmail.com')
        page.click('button[data-qa="signup-button"]')
        assert page.locator('p:has-text("Email Address already exist!")').is_visible()
        print("Email already exists")

def test_empty_name_and_email():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context(viewport=None)
        page = browser.new_page()

        page.goto("https://automationexercise.com", timeout=60000, wait_until="networkidle")

        assert page.locator('body').is_visible()

        page.click('a[href="/login"]')

        assert page.locator('h2:has-text("New User Signup!")').is_visible()

        page.fill('input[name="name"]', '')
        page.fill('input[data-qa="signup-email"]', '')
        page.click('button[data-qa="signup-button"]')

        assert page.locator('input[name="name"]:invalid').is_visible()
        assert page.locator('input[data-qa="signup-email"]:invalid').is_visible()

        print("Name and email fields are empty")
        
def test_empty_name_valid_email():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context(viewport=None)
        page = browser.new_page()

        page.goto("https://automationexercise.com", timeout=60000, wait_until="networkidle")

        assert page.locator('body').is_visible()

        page.click('a[href="/login"]')

        assert page.locator('h2:has-text("New User Signup!")').is_visible()

        page.fill('input[name="name"]', '')
        page.fill('input[data-qa="signup-email"]', 'fireai@gmail.com')
        page.click('button[data-qa="signup-button"]')   
        assert page.locator('input[name="name"]:invalid').is_visible()  
        print("Name field is empty")

def test_empty_email_valid_name():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context(viewport=None)
        page = browser.new_page()

        page.goto("https://automationexercise.com", timeout=60000, wait_until="networkidle")

        assert page.locator('body').is_visible()

        page.click('a[href="/login"]')

        assert page.locator('h2:has-text("New User Signup!")').is_visible()

        page.fill('input[name="name"]', 'uefhniof')
        page.fill('input[data-qa="signup-email"]', '')
        page.click('button[data-qa="signup-button"]')   
        assert page.locator('input[data-qa="signup-email"]:invalid').is_visible()  
        print("Email field is empty")
        browser.close()