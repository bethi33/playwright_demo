# from playwright.sync_api import sync_playwright, expect
# from conftest import browser 

# def test_login_validata(): 
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False, slow_mo=1000)
#         context = browser.new_context(viewport=None)    
#         page = browser.new_page()
#         page.goto("https://automationexercise.com", timeout=60000, wait_until="networkidle")
#         assert page.locator('body').is_visible()

#         page.click('a[href="/login"]')

#         page.fill('input[name="name"]', 'fireai')
#         page.fill('input[data-qa="login-email"]', 'fireai@gmail.com')
#         page.fill('input[data-qa="login-password"]', 'fireai')
#         page.click('button[data-qa="login-button"]')

#         assert page.locator('a:has-text("Logged in as fireai")').is_visible()
#         print()
#         print("Login successful")

# def test_incorrect_email_And_password():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False, slow_mo=1000)
#         context = browser.new_context(viewport=None)
#         page = browser.new_page()
#         page.goto("https://automationexercise.com", timeout=60000, wait_until="networkidle")
#         assert page.locator('body').is_visible()    
#         page.click('a[href="/login"]')

#         page.fill('input[data-qa="login-email"]', 'fir@gmail.com')
#         page.fill('input[data-qa="login-password"]', 'aifire')
#         page.click('button[data-qa="login-button"]')
#         expect(page.locator('p').filter(has_text="Your email or password is incorrect!")).to_be_visible(timeout=10000)
#         print("Incorrect email or password")

# def test_valid_email_invalid_password():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False, slow_mo=1000)
#         context = browser.new_context(viewport=None)
#         page = browser.new_page()
#         page.goto("https://automationexercise.com", timeout=60000, wait_until="networkidle")
#         assert page.locator('body').is_visible()    
#         page.click('a[href="/login"]')

#         page.fill('input[data-qa="login-email"]', 'fireai@gmail.com')
#         page.fill('input[data-qa="login-password"]', 'jfjsafjn')
#         page.click('button[data-qa="login-button"]')
#         assert page.locator('p:has-text("Your email or password is incorrect!")').is_visible()
#         print("Invalid password")
#         browser.close()

# def test_valid_password_invalid_email():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False, slow_mo=1000)
#         context = browser.new_context(viewport=None)
#         page = browser.new_page()
#         page.goto("https://automationexercise.com", timeout=60000, wait_until="networkidle")
#         assert page.locator('body').is_visible()    
#         page.click('a[href="/login"]')

#         page.fill('input[data-qa="login-email"]', 'fire@gmail.com')
#         page.fill('input[data-qa="login-password"]', 'fireai')
#         page.click('button[data-qa="login-button"]')    
#         assert page.locator('p:has-text("Your email or password is incorrect!")').is_visible()
#         print("Invalid email")      

# def test_empty_email_and_password():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False, slow_mo=1000)
#         context = browser.new_context(viewport=None)
#         page = browser.new_page()
#         page.goto("https://automationexercise.com", timeout=60000, wait_until="networkidle")
#         assert page.locator('body').is_visible()    
#         page.click('a[href="/login"]')

#         page.fill('input[data-qa="login-email"]', '')
#         page.fill('input[data-qa="login-password"]', '')
#         page.click('button[data-qa="login-button"]')

#         assert page.locator('input[data-qa="login-email"]:invalid').is_visible()
#         assert page.locator('input[data-qa="login-password"]:invalid').is_visible()

#         print("Email and password fields are empty")

# def test_empty_mail_valid_password():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False, slow_mo=1000)
#         context = browser.new_context(viewport=None)
#         page = browser.new_page()
#         page.goto("https://automationexercise.com", timeout=60000, wait_until="networkidle")
#         assert page.locator('body').is_visible()    
#         page.click('a[href="/login"]')

#         page.fill('input[data-qa="login-email"]', '')
#         page.fill('input[data-qa="login-password"]', 'fireai')
#         page.click('button[data-qa="login-button"]')

#         assert page.locator('input[data-qa="login-email"]:invalid').is_visible()

#         print("Email field is empty")

# def test_empty_password_valid_email():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False, slow_mo=1000)
#         context = browser.new_context(viewport=None)
#         page = browser.new_page()
#         page.goto("https://automationexercise.com", timeout=60000, wait_until="networkidle")
#         assert page.locator('body').is_visible()    
#         page.click('a[href="/login"]')

#         page.fill('input[data-qa="login-email"]', 'fire@gmail.com')
#         page.fill('input[data-qa="login-password"]', '')
#         page.click('button[data-qa="login-button"]')

#         assert page.locator('input[data-qa="login-password"]:invalid').is_visible()

#         print("Password field is empty")

# def test_empty_email_and_password():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False, slow_mo=1000)
#         context = browser.new_context(viewport=None)
#         page = browser.new_page()
#         page.goto("https://automationexercise.com", timeout=60000, wait_until="networkidle")
#         assert page.locator('body').is_visible()    
#         page.click('a[href="/login"]')

#         page.fill('input[data-qa="login-email"]', '')
#         page.fill('input[data-qa="login-password"]', '')
#         page.click('button[data-qa="login-button"]')

#         assert page.locator('input[data-qa="login-email"]:invalid').is_visible()
#         assert page.locator('input[data-qa="login-password"]:invalid').is_visible()

#         print("Email and password fields are empty")
#         browser.close()


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
    p, browser, context, page = open_page()
    try:
        do_login(page, "fireai@gmail.com", "fireai")
        assert page.locator('a:has-text("Logged in as fireai")').is_visible()
        print("Login successful")
    finally:
        browser.close()
        p.stop()

def test_incorrect_email_and_password():
    p, browser, context, page = open_page()
    try:
        do_login(page, "fir@gmail.com", "aifire")
        expect(page.locator('p').filter(has_text="Your email or password is incorrect!")).to_be_visible()
        print("Incorrect email or password")
    finally:
        browser.close()
        p.stop()

def test_valid_email_invalid_password():
    p, browser, context, page = open_page()
    try:
        do_login(page, "fireai@gmail.com", "jfjsafjn")
        assert page.locator('p:has-text("Your email or password is incorrect!")').is_visible()
        print("Invalid password")
    finally:
        browser.close()
        p.stop()

def test_valid_password_invalid_email():
    p, browser, context, page = open_page()
    try:
        do_login(page, "fire@gmail.com", "fireai")
        assert page.locator('p:has-text("Your email or password is incorrect!")').is_visible()
        print("Invalid email")
    finally:
        browser.close()
        p.stop()

def test_empty_email_and_password():
    p, browser, context, page = open_page()
    try:
        do_login(page, "", "")
        assert page.locator('input[data-qa="login-email"]:invalid').is_visible()
        assert page.locator('input[data-qa="login-password"]:invalid').is_visible()
        print("Email and password fields are empty")
    finally:
        browser.close()
        p.stop()

def test_empty_mail_valid_password():
    p, browser, context, page = open_page()
    try:
        do_login(page, "", "fireai")
        assert page.locator('input[data-qa="login-email"]:invalid').is_visible()
        print("Email field is empty")
    finally:
        browser.close()
        p.stop()

def test_empty_password_valid_email():
    p, browser, context, page = open_page()
    try:
        do_login(page, "fire@gmail.com", "")
        assert page.locator('input[data-qa="login-password"]:invalid').is_visible()
        print("Password field is empty")
    finally:
        browser.close()
        p.stop()