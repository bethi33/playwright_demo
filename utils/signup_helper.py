import time

def signup_new_user(page, name="TestUser"):
    unique_email = f"{name}_{int(time.time())}@example.com"
    page.click('a[href="/login"]')
    page.fill('input[name="name"]', name)
    page.fill('input[data-qa="signup-email"]', unique_email)
    page.click('button[data-qa="signup-button"]')
    return unique_email
