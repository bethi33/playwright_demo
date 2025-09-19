# from playwright.sync_api import sync_playwright
# def test_rajesh_user_new():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(channel='chrome', headless=False)
#         page = browser.new_page()
#         page.goto("http://www.google.com")
#         page.click('text=Gmail')
#         page.click('text=Create an account')
#         page.click('text=For my personal use')
#         page.wait_for_url("**accounts.google.com/**", timeout=60000)
#         assert "Create your Google account" in page.title()
#         browser.close()


# <a class="gb_X" aria-label="Gmail " data-pid="23" href="https://mail.google.com/mail/?authuser=0&amp;ogbl" target="_top">Gmail</a>
# <div slot="label" class="label-tracker" aria-label="Create an account" data-g-event="gmail_asw: global nav" data-g-action="create an account"></div><span class="link__label">
#                     For my personal use
#                   </span>

# import re
# # from socket import timeout
# from playwright.sync_api import expect

# def test_rajesh_user(page):
#     page.wait_for_timeout(3000)
#     page.goto("http://www.google.com/ncr")

#     try:
#         page.get_by_role("button", name="Accept all").click(timeout=5000)
#     except:
#         print("No popup to accept")
#         page.get_by_role("combobox", name="Search").fill("playwright Python")
#         page.keyboard.press("Enter")
#         expect(page).to_have_title(re.compile("playwright Python", re.IGNORECASE))

# from utils import config
# from playwright.sync_api import sync_playwright 

# def test_rajesh_user(page):
#     page.fill('input[name="username"]', config.USER_CREDENTIALS["valid_user"]["username"])
#     page.fill('input[name="password"]', config.USER_CREDENTIALS["valid_user"]["password"])
#     page.click('button[type="submit"]') # Assuming the login button is of type submit
#     assert page.locator('h6:has-text("Dashboard")').is_visible()
#     print("Login successful, Dashboard is visible.")

# from playwright.sync_api import Page, expect

# def test_example(page: Page) -> None:
#     page.goto("https://www.saucedemo.com/")
#     page.locator("[data-test=\"username\"]").click()
#     page.locator("[data-test=\"username\"]").fill("standard_user")
#     page.locator("[data-test=\"password\"]").click()
#     page.locator("[data-test=\"password\"]").fill("secret_sauce")
#     page.locator("[data-test=\"login-button\"]").click()
#     page.locator("[data-test=\"product-sort-container\"]").select_option("lohi")
#     page.locator("[data-test=\"add-to-cart-sauce-labs-onesie\"]").click()
#     page.locator("[data-test=\"shopping-cart-link\"]").click()
#     page.locator("[data-test=\"checkout\"]").click()
#     page.locator(".checkout_info").click()
#     page.locator("[data-test=\"lastName\"]").fill("Rakes")
#     page.locator("[data-test=\"firstName\"]").click()
#     page.locator("[data-test=\"firstName\"]").fill("Rakesh")
#     page.locator("[data-test=\"firstName\"]").press("Tab")
#     page.locator("[data-test=\"lastName\"]").fill("Data")
#     page.locator("[data-test=\"lastName\"]").press("Tab")
#     page.locator("[data-test=\"postalCode\"]").fill("421302")
#     page.locator("[data-test=\"continue\"]").click()
#     page.locator("[data-test=\"finish\"]").click()
#     page.locator("[data-test=\"back-to-products\"]").click()
#     page.wait_for_url("**/checkout-complete.html", timeout=10000)
#     expect(page.get_by_role("heading", name="Thank you for your order!")).to_be_visible()
