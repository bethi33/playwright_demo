from playwright.sync_api import sync_playwright, expect
from conftest import browser

def open_page():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(viewport=None)
    page = context.new_page()
    page.goto("https://automationexercise.com", timeout=90000, wait_until="networkidle")
    return p, browser, context, page

def test_click_on_product_button():
    p, browser, context, page = open_page()
    try:
        page.click('a[href="/products"]')
        expect(page.locator('h2:has-text("All Products")')).to_be_visible()
        print("Navigated to Products page successfully")
    finally:
        browser.close()
        p.stop()

def test_click_on_first_product_view_button():
    p, browser, context, page = open_page()
    try:
        page.click('a[href="/products"]')
        expect(page.locator('h2:has-text("All Products")')).to_be_visible()
        page.click('a[href="/product_details/1"]')
        expect(page.locator('h2:has-text("Blue Top")')).to_be_visible()
        print("Navigated to first product details page successfully")
    finally:
        browser.close()
        p.stop()

def test_verify_product_details():
    p, browser, context, page = open_page()
    try:
        page.click('a[href="/products"]')
        expect(page.locator('h2:has-text("All Products")')).to_be_visible()
        page.click('a[href="/product_details/1"]')
        expect(page.locator('h2:has-text("Blue Top")')).to_be_visible()
        expect(page.locator('p:has-text("Category: Women > Tops")')).to_be_visible()
        expect(page.get_by_text("Rs. 500", exact=True)).to_be_visible()
        expect(page.locator('b:has-text("Availability:")')).to_be_visible()
        print("Product details verified successfully")
    finally:
        browser.close()
        p.stop()

def test_add_product_to_cart():
    p, browser, context, page = open_page()
    try:
        page.click('a[href="/products"]')
        expect(page.locator('h2:has-text("All Products")')).to_be_visible()
        page.click('a[href="/product_details/1"]')
        expect(page.locator('h2:has-text("Blue Top")')).to_be_visible()
        page.fill('input[id="quantity"]', '4')
        page.click('button:has-text("Add to cart")')
        page.wait_for_selector('div#cartModal', timeout=30000)
        expect(page.locator('div#cartModal')).to_be_visible()
        print("Product added to cart successfully")
    finally:
        browser.close()
        p.stop()

def test_view_cart_after_adding_product():
    p, browser, context, page = open_page()
    try:
        page.click('a[href="/products"]')
        expect(page.locator('h2:has-text("All Products")')).to_be_visible()
        page.click('a[href="/product_details/1"]')
        expect(page.locator('h2:has-text("Blue Top")')).to_be_visible()
        page.fill('input[id="quantity"]', '4')
        page.click('button:has-text("Add to cart")')
        page.wait_for_selector('div#cartModal', timeout=30000)
        expect(page.locator('div#cartModal')).to_be_visible()
        page.click('a:has-text("View Cart")')
        # expect(page.locator('h2:has-text("Shopping Cart")')).to_be_visible()
        page.click('a:has-text("Proceed To Checkout")')
        page.click('a:has-text("Register / Login")')
        expect(page.locator('input[data-qa="login-email"]')).to_be_visible()
        expect(page.locator('input[data-qa="login-password"]')).to_be_visible()
        page.fill('input[data-qa="login-email"]', 'fireai@gmail.com')
        page.fill('input[data-qa="login-password"]', 'fireai')
        page.click('button[type="submit"]')
        expect(page.locator('a:has-text("Logged in as fireai")')).to_be_visible()
        page.click('a[href="/view_cart"]')
        page.click('a:has-text("proceed to checkout")')
        expect(page.locator('h2:has-text("Address Details")')).to_be_visible()
        expect(page.locator('h2:has-text("Review Your Order")')).to_be_visible()
        page.click('a[href="/payment"]')
        expect(page.locator('h2:has-text("Payment")')).to_be_visible()

        page.fill('input[name="name_on_card"]', 'Fire AI')
        page.fill('input[name="card_number"]', '4111111111111111')
        page.fill('input[name="cvc"]', '123')
        page.fill('input[name="expiry_month"]', '12')
        page.fill('input[name="expiry_year"]', '2026')

        page.click('button:has-text("Pay and Confirm Order")')
        expect(page.locator('p:has-text("Congratulations! Your order has been confirmed!")')).to_be_visible()
        print("Order placed successfully!")
    finally:
        browser.close()
        p.stop()
