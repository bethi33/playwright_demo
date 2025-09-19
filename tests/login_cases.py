from playwright.sync_api import sync_playwright, expect
from conftest import browser 

def test_login_validata(): 
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context(viewport=None)    
        page = browser.new_page()
        page.goto("https://automationexercise.com", timeout=60000, wait_until="networkidle")
        assert page.locator('body').is_visible()

        page.click('a[href="/login"]')

        page.fill('input[name="name"]', 'fireai')
        page.fill('input[data-qa="login-email"]', 'fireai@gmail.com')
        page.fill('input[data-qa="login-password"]', 'fireai')
        page.click('button[data-qa="login-button"]')

        assert page.locator('a:has-text("Logged in as fireai")').is_visible()

        print("Login successful")

def test_incorrect_email_And_password():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context(viewport=None)
        page = browser.new_page()
        page.goto("https://automationexercise.com", timeout=60000, wait_until="networkidle")
        assert page.locator('body').is_visible()    
        page.click('a[href="/login"]')

        page.fill('input[data-qa="login-email"]', 'fir@gmail.com')
        page.fill('input[data-qa="login-password"]', 'aifire')
        page.click('button[data-qa="login-button"]')
        expect(page.locator('p').filter(has_text="Your email or password is incorrect!")).to_be_visible(timeout=10000)
        print("Incorrect email or password")

def test_valid_email_invalid_password():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context(viewport=None)
        page = browser.new_page()
        page.goto("https://automationexercise.com", timeout=60000, wait_until="networkidle")
        assert page.locator('body').is_visible()    
        page.click('a[href="/login"]')

        page.fill('input[data-qa="login-email"]', 'fireai@gmail.com')
        page.fill('input[data-qa="login-password"]', 'jfjsafjn')
        page.click('button[data-qa="login-button"]')
        assert page.locator('p:has-text("Your email or password is incorrect!")').is_visible()
        print("Invalid password")
        browser.close()

def test_valid_password_invalid_email():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context(viewport=None)
        page = browser.new_page()
        page.goto("https://automationexercise.com", timeout=60000, wait_until="networkidle")
        assert page.locator('body').is_visible()    
        page.click('a[href="/login"]')

        page.fill('input[data-qa="login-email"]', 'fire@gmail.com')
        page.fill('input[data-qa="login-password"]', 'fireai')
        page.click('button[data-qa="login-button"]')    
        assert page.locator('p:has-text("Your email or password is incorrect!")').is_visible()
        print("Invalid email")      

def test_empty_email_and_password():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context(viewport=None)
        page = browser.new_page()
        page.goto("https://automationexercise.com", timeout=60000, wait_until="networkidle")
        assert page.locator('body').is_visible()    
        page.click('a[href="/login"]')

        page.fill('input[data-qa="login-email"]', '')
        page.fill('input[data-qa="login-password"]', '')
        page.click('button[data-qa="login-button"]')

        assert page.locator('input[data-qa="login-email"]:invalid').is_visible()
        assert page.locator('input[data-qa="login-password"]:invalid').is_visible()

        print("Email and password fields are empty")

def test_empty_mail_valid_password():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context(viewport=None)
        page = browser.new_page()
        page.goto("https://automationexercise.com", timeout=60000, wait_until="networkidle")
        assert page.locator('body').is_visible()    
        page.click('a[href="/login"]')

        page.fill('input[data-qa="login-email"]', '')
        page.fill('input[data-qa="login-password"]', 'fireai')
        page.click('button[data-qa="login-button"]')

        assert page.locator('input[data-qa="login-email"]:invalid').is_visible()

        print("Email field is empty")

def test_empty_password_valid_email():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context(viewport=None)
        page = browser.new_page()
        page.goto("https://automationexercise.com", timeout=60000, wait_until="networkidle")
        assert page.locator('body').is_visible()    
        page.click('a[href="/login"]')

        page.fill('input[data-qa="login-email"]', 'fire@gmail.com')
        page.fill('input[data-qa="login-password"]', '')
        page.click('button[data-qa="login-button"]')

        assert page.locator('input[data-qa="login-password"]:invalid').is_visible()

        print("Password field is empty")

def test_empty_email_and_password():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context(viewport=None)
        page = browser.new_page()
        page.goto("https://automationexercise.com", timeout=60000, wait_until="networkidle")
        assert page.locator('body').is_visible()    
        page.click('a[href="/login"]')

        page.fill('input[data-qa="login-email"]', '')
        page.fill('input[data-qa="login-password"]', '')
        page.click('button[data-qa="login-button"]')

        assert page.locator('input[data-qa="login-email"]:invalid').is_visible()
        assert page.locator('input[data-qa="login-password"]:invalid').is_visible()

        print("Email and password fields are empty")
        browser.close()

