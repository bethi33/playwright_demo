def login_user(page, email, password):
    page.click('a[href="/login"]')
    page.fill('input[data-qa="login-email"]', email)
    page.fill('input[data-qa="login-password"]', password)
    page.click('button[data-qa="login-button"]')
