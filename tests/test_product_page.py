from playwright.sync_api import sync_playwright, expect
from conftest import browser

def open_page():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(viewport=None)
    page = context.new_page()
    page.goto("https://automationexercise.com", timeout=60000, wait_until="networkidle")
    return p, browser, context, page

def do_product_search(page, search_query):
    page.fill('input[name="search"]', search_query)
    page.click('button[type="submit"]')

def test_product_search():
    p, browser, context, page = open_page()
    try:
        do_product_search(page, "Dress")
        expect(page.locator('h2:has-text("Search Results")')).to_be_visible()
        print("Product search successful")
    finally:
        browser.close()
        p.stop()

def test_product_search_no_results():
    p, browser, context, page = open_page()
    try:
        do_product_search(page, "NonExistentProduct123")
        expect(page.locator('p:has-text("No products found")')).to_be_visible()
        print("No products found as expected")
    finally:
        browser.close()
        p.stop()

def test_navigate_to_product_details():
    p, browser, context, page = open_page()
    try:
        do_product_search(page, "Dress")
        expect(page.locator('h2:has-text("Search Results")')).to_be_visible()
        page.click('a:has-text("View Product")')
        expect(page.locator('h2:has-text("Product Details")')).to_be_visible()
        print("Navigated to product details successfully")
    finally:
        browser.close()
        p.stop()

def test_add_product_to_cart():
    p, browser, context, page = open_page()
    try:
        do_product_search(page, "Dress")
        expect(page.locator('h2:has-text("Search Results")')).to_be_visible()
        page.click('a:has-text("View Product")')
        expect(page.locator('h2:has-text("Product Details")')).to_be_visible()
        page.click('button:has-text("Add to cart")')
        expect(page.locator('div:has-text("Product added to cart")')).to_be_visible()
        print("Product added to cart successfully")
    finally:
        browser.close()
        p.stop()
    
def test_view_cart():
    p, browser, context, page = open_page()
    try:
        do_product_search(page, "Dress")
        expect(page.locator('h2:has-text("Search Results")')).to_be_visible()
        page.click('a:has-text("View Product")')
        expect(page.locator('h2:has-text("Product Details")')).to_be_visible()
        page.click('button:has-text("Add to cart")')
        expect(page.locator('div:has-text("Product added to cart")')).to_be_visible()
        page.click('a:has-text("View Cart")')
        expect(page.locator('h2:has-text("Shopping Cart")')).to_be_visible()
        print("Viewed cart successfully")
    finally:
        browser.close()
        p.stop()

    def test_cart_persistence_after_navigation():
        p, browser, context, page = open_page()
        try:
            do_product_search(page, "Dress")
            expect(page.locator('h2:has-text("Search Results")')).to_be_visible()
            page.click('a:has-text("View Product")')
            expect(page.locator('h2:has-text("Product Details")')).to_be_visible()
            page.click('button:has-text("Add to cart")')
            expect(page.locator('div:has-text("Product added to cart")')).to_be_visible()
            page.click('a:has-text("View Cart")')
            expect(page.locator('h2:has-text("Shopping Cart")')).to_be_visible()
            page.click('a:has-text("Continue Shopping")')
            expect(page.locator('h2:has-text("Search Results")')).to_be_visible()
            page.click('a:has-text("View Cart")')
            expect(page.locator('h2:has-text("Shopping Cart")')).to_be_visible()
            print("Cart persistence after navigation successful")
        finally:
            browser.close()
            p.stop()

def test_remove_product_from_cart():
    p, browser, context, page = open_page()
    try:
        do_product_search(page, "Dress")
        expect(page.locator('h2:has-text("Search Results")')).to_be_visible()
        page.click('a:has-text("View Product")')
        expect(page.locator('h2:has-text("Product Details")')).to_be_visible()
        page.click('button:has-text("Add to cart")')
        expect(page.locator('div:has-text("Product added to cart")')).to_be_visible()
        page.click('a:has-text("View Cart")')
        expect(page.locator('h2:has-text("Shopping Cart")')).to_be_visible()
        page.click('button:has-text("Remove")')
        expect(page.locator('p:has-text("Your cart is empty")')).to_be_visible()
        print("Product removed from cart successfully")
    finally:
        browser.close()
        p.stop()

def test_update_product_quantity_in_cart():
    p, browser, context, page = open_page()
    try:
        do_product_search(page, "Dress")
        expect(page.locator('h2:has-text("Search Results")')).to_be_visible()
        page.click('a:has-text("View Product")')
        expect(page.locator('h2:has-text("Product Details")')).to_be_visible()
        page.click('button:has-text("Add to cart")')
        expect(page.locator('div:has-text("Product added to cart")')).to_be_visible()
        page.click('a:has-text("View Cart")')
        expect(page.locator('h2:has-text("Shopping Cart")')).to_be_visible()
        page.fill('input[name="quantity"]', '2')
        page.click('button:has-text("Update")')
        expect(page.locator('td:has-text("2")')).to_be_visible()
        print("Product quantity updated in cart successfully")
    finally:
        browser.close()
        p.stop()

def test_checkout_process():
    p, browser, context, page = open_page()
    try:
        do_product_search(page, "Dress")
        expect(page.locator('h2:has-text("Search Results")')).to_be_visible()
        page.click('a:has-text("View Product")')
        expect(page.locator('h2:has-text("Product Details")')).to_be_visible()
        page.click('button:has-text("Add to cart")')
        expect(page.locator('div:has-text("Product added to cart")')).to_be_visible()
        page.click('a:has-text("View Cart")')
        expect(page.locator('h2:has-text("Shopping Cart")')).to_be_visible()
        page.click('a:has-text("Proceed to Checkout")')
        expect(page.locator('h2:has-text("Checkout")')).to_be_visible()
        print("Checkout process initiated successfully")
    finally:
        browser.close()
        p.stop()
    
def test_apply_coupon_code():
    p, browser, context, page = open_page()
    try:
        do_product_search(page, "Dress")
        expect(page.locator('h2:has-text("Search Results")')).to_be_visible()
        page.click('a:has-text("View Product")')
        expect(page.locator('h2:has-text("Product Details")')).to_be_visible()
        page.click('button:has-text("Add to cart")')
        expect(page.locator('div:has-text("Product added to cart")')).to_be_visible()
        page.click('a:has-text("View Cart")')
        expect(page.locator('h2:has-text("Shopping Cart")')).to_be_visible()
        page.fill('input[name="coupon_code"]', 'DISCOUNT2024')
        page.click('button:has-text("Apply Coupon")')
        expect(page.locator('div:has-text("Coupon applied successfully")')).to_be_visible()
        print("Coupon code applied successfully")
    finally:
        browser.close()
        p.stop()    

def test_empty_search():
    p, browser, context, page = open_page()
    try:
        do_product_search(page, "")
        expect(page.locator('h2:has-text("All Products")')).to_be_visible()
        print("Empty search shows all products")
    finally:
        browser.close()
        p.stop()

def test_special_characters_search():
        p, browser, context, page = open_page()
        try:
            do_product_search(page, "@#$%^&*")
            expect(page.locator('p:has-text("No products found")')).to_be_visible()
            print("Special characters search handled correctly")
        finally:
            browser.close()
            p.stop()

def test_view_product_images():
    p, browser, context, page = open_page()
    try:
        do_product_search(page, "Dress")
        expect(page.locator('h2:has-text("Search Results")')).to_be_visible()
        page.click('a:has-text("View Product")')
        expect(page.locator('h2:has-text("Product Details")')).to_be_visible()
        expect(page.locator('img.product-image')).to_be_visible()
        print("Product images are visible")
    finally:
        browser.close()
        p.stop()

def test_details_of_multiple_products():
    p, browser, context, page = open_page()
    try:
        do_product_search(page, "Dress")
        expect(page.locator('h2:has-text("Search Results")')).to_be_visible()
        product_links = page.locator('a:has-text("View Product")').all()
        for link in product_links[:3]:  # Test first 3 products
            link.click()
            expect(page.locator('h2:has-text("Product Details")')).to_be_visible()
            page.go_back()
        print("Details of multiple products viewed successfully")
    finally:
        browser.close()
        p.stop()

def test_add_multiple_products_to_cart():
    p, browser, context, page = open_page()
    try:
        do_product_search(page, "Dress")
        expect(page.locator('h2:has-text("Search Results")')).to_be_visible()
        product_links = page.locator('a:has-text("View Product")').all()
        for link in product_links[:2]:  # Add first 2 products to cart
            link.click()
            expect(page.locator('h2:has-text("Product Details")')).to_be_visible()
            page.click('button:has-text("Add to cart")')
            expect(page.locator('div:has-text("Product added to cart")')).to_be_visible()
            page.click('a:has-text("Continue Shopping")')
        page.click('a:has-text("View Cart")')
        expect(page.locator('h2:has-text("Shopping Cart")')).to_be_visible()
        cart_items = page.locator('tr.cart_item').count()
        assert cart_items == 2
        print("Multiple products added to cart successfully")
    finally:
        browser.close()
        p.stop()