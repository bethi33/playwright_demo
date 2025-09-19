# from xml.sax.xmlreader import Locator
# from multiprocessing import context
# from playwright.sync_api import sync_playwright

# from utils.config import SLOW_MO 

# def test_signup_user_success():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False, slow_mo=1000)
#         context = browser.new_context(viewport=None)
#         page = browser.new_page()

#         page.goto("https://automationexercise.com", timeout=60000, wait_until="networkidle")

#         assert page.locator('body').is_visible()

#         page.click('a[href="/login"]')

#         assert page.locator('h2:has-text("New User Signup!")').is_visible()

#         page.fill('input[name="name"]', 'Test33User')
#         page.fill('input[data-qa="signup-email"]', 'tet333us222er123@example.com')

#         page.click('button[data-qa="signup-button"]')

#         page.wait_for_selector('b:has-text("Enter Account Information")', timeout=30000)

#         page.check('input[id="id_gender1"]') 
#         page.fill('input[id="password"]', 'Test@1234')
#         page.select_option('select[id="days"]', '10')
#         page.select_option('select[id="months"]', '5')
#         page.select_option('select[id="years"]', '1990')

#         page.check('input[id="newsletter"]')

#         page.check('input[id="optin"]')

#         page.fill('input[id="first_name"]', 'Test')
#         page.fill('input[id="last_name"]', 'User')
#         page.fill('input[id="company"]', 'TestCompany')
#         page.fill('input[id="address1"]', '123 Test Street')
#         page.fill('input[id="address2"]', 'Suite 456')
#         page.select_option('select[id="country"]', 'Canada')
#         page.fill('input[id="state"]', 'Ontario')
#         page.fill('input[id="city"]', 'Toronto')
#         page.fill('input[id="zipcode"]', 'M4B1B3')
#         page.fill('input[id="mobile_number"]', '1234567890')

#         page.click('button[data-qa="create-account"]')

#         page.wait_for_selector('b:has-text("Account Created!")', timeout=30000)

#         page.click('a[data-qa="continue-button"]')

#         assert page.locator('a:has-text("Logged in as Test33User")').is_visible()

#         # browser.close()

# def test_signup_user_failure_email():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False, slow_mo=1000)
#         context = browser.new_context(viewport=None)
#         page = browser.new_page()

#         page.goto("https://automationexercise.com", timeout=60000, wait_until="networkidle")

#         assert page.locator('body').is_visible()

#         page.click('a[href="/login"]')

#         assert page.locator('h2:has-text("New User Signup!")').is_visible()

#         page.fill('input[name="name"]', 'uefhniof')
#         page.fill('input[data-qa="signup-email"]', 'checkwrongemail')

#         page.click('button[data-qa="signup-button"]')

#         assert page.locator('input[data-qa="signup-email"]:invalid').is_visible()

#         # browser.close()

# def test_wrong_password_login():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False, slow_mo=1000)
#         context = browser.new_context(viewport=None)
#         page = browser.new_page()

#         page.goto("https://automationexercise.com", timeout=60000, wait_until="networkidle")

#         assert page.locator('body').is_visible()

#         page.click('a[href="/login"]')

#         assert page.locator('h2:has-text("Login to your account")').is_visible()

#         page.fill('input[data-qa="login-email"]', 'fireai@gmail.com')
#         page.fill('input[data-qa="login-password"]', 'aifire123')  
#         page.click('button[data-qa="login-button"]')

#         assert page.locator('p:has-text("Your email or password is incorrect!")').is_visible()

#         # browser.close()

# def test_register_user_with_same_email():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False, slow_mo=1000)
#         context = browser.new_context(viewport=None)
#         page = browser.new_page()

#         page.goto("https://automationexercise.com", timeout=60000, wait_until="networkidle")

#         assert page.locator('body').is_visible()

#         page.click('a[href="/login"]')

#         assert page.locator('h2:has-text("New User Signup!")').is_visible()

#         page.fill('input[name="name"]', 'fireai')
#         page.fill('input[data-qa="signup-email"]', 'fireai@gmail.com')
#         page.click('button[data-qa="signup-button"]')
#         assert page.locator('p:has-text("Email Address already exist!")').is_visible()
#         # browser.close()

# def test_incorrect_email_id_and_password():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False, slow_mo=1000)
#         context = browser.new_context(viewport=None)
#         page = browser.new_page()
#         page.goto("https://automationexercise.com", timeout=60000, wait_until="networkidle")
#         assert page.locator('body').is_visible()
#         page.click('a[href="/login"]')
#         assert page.locator('h2:has-text("Login to your account")').is_visible()
#         page.fill('input[data-qa="login-email"]', 'firei@gmail.com')
#         page.fill('input[data-qa="login-password"]', 'fire123')
#         page.click('button[data-qa="login-button"]')
#         assert page.locator('p:has-text("Your email or password is incorrect!")').is_visible()
#         # browser.close()

# def test_verify_test_case():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False, slow_mo=1000)
#         context =  browser.new_context(viewport=None)
#         page = browser.new_page()
#         page.goto("https://automationexercise.com", timeout=60000, wait_until="networkidle")
#         assert page.locator('body').is_visible()
#         page.click('a[href="/test_cases"]')
#         assert page.locator('h2:has-text("Test Cases")').is_visible()
#         browser.close()

# def test_verify_products_page():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False, slow_mo=1000)
#         context = browser.new_context(viewport=None)
#         page = browser.new_page()
#         page.goto("https://automationexercise.com", timeout=60000, wait_until="networkidle")
#         assert page.locator('body').is_visible()
#         page.click('a[href="/products"]')
#         assert page.locator('h2:has-text("ALL PRODUCTS")').is_visible()
#         page.click('a[href="/product_details/1"]')
#         assert page.locator('h2:has-text(Blue Top)').is_visible()
#         assert page.locator('b:has-text("Category:")').is_visible()
#         assert page.locator('p:has-text("Rs. 500")').is_visible()
#         assert page.locator('p:has-text("Availability:")').is_visible() 
#         assert page.locator('p:has-text("Condition:")').is_visible()
#         assert page.locator('p:has-text("Brand:")').is_visible()    
#         print(page.locator('div[class="product-information"]').text_content())
#         print(page.locator('div[class="product-details"]').text_content())
#         browser.close()

