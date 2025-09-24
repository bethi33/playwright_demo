from playwright.sync_api import sync_playwright, expect

def open_page():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(viewport=None)
    page = context.new_page()
    page.goto("https://automationexercise.com", timeout=60000, wait_until="networkidle")
    return p, browser, context, page

def do_login(page, email, password):
    page.click('a[href="/login"]')
    page.fill('input[data-qa="login-email"]', email)
    page.fill('input[data-qa="login-password"]', password)
    page.click('button[data-qa="login-button"]')

def test_login_valid():
    p = None 
    browser = None
    try:
        p, browser, context, page = open_page()
        do_login(page, "fireai@gmail.com", "fireai")
        assert page.locator('a:has-text("Logged in as fireai")').is_visible()
        print("Login successful")
    finally:
        if browser is not None:
            browser.close()
        if p is not None:
            p.stop()

def test_incorrect_email_and_password():
    try:
        p, browser, context, page = open_page()
        do_login(page, "fir@gmail.com", "aifire")
        expect(page.locator('p').filter(has_text="Your email or password is incorrect!")).to_be_visible()
        print("Incorrect email or password")
    finally:
        browser.close()
        p.stop()

def test_valid_email_invalid_password():
    try:
        p, browser, context, page = open_page()
        do_login(page, "fireai@gmail.com", "jfjsafjn")
        assert page.locator('p:has-text("Your email or password is incorrect!")').is_visible()
        print("Invalid password")
    finally:
        browser.close()
        p.stop()

def test_valid_password_invalid_email():
    try:
        p, browser, context, page = open_page()
        do_login(page, "fire@gmail.com", "fireai")
        assert page.locator('p:has-text("Your email or password is incorrect!")').is_visible()
        print("Invalid email")
    finally:
        browser.close()
        p.stop()

def test_empty_email_and_password():
    try:
        p, browser, context, page = open_page()
        do_login(page, "", "")
        assert page.locator('input[data-qa="login-email"]:invalid').is_visible()
        assert page.locator('input[data-qa="login-password"]:invalid').is_visible()
        print("Email and password fields are empty")
    finally:
        browser.close()
        p.stop()

def test_empty_mail_valid_password():
    try:
        p, browser, context, page = open_page()
        do_login(page, "", "fireai")
        assert page.locator('input[data-qa="login-email"]:invalid').is_visible()
        print("Email field is empty")
    finally:
        browser.close()
        p.stop()

def test_empty_password_valid_email():
    try:
        p, browser, context, page = open_page()
        do_login(page, "fire@gmail.com", "")
        assert page.locator('input[data-qa="login-password"]:invalid').is_visible()
        print("Password field is empty")
    finally:
        browser.close()
        p.stop()