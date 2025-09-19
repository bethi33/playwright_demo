# import pytest
# from utils.signup_helper import signup_new_user

# def test_signup_user_success(page):
#     page.goto("https://automationexercise.com")

#     email = signup_new_user(page, "TestUser")

#     assert page.locator('b:has-text("Enter Account Information")').is_visible()


# @pytest.mark.parametrize("name,email", [
#     ("", "valid@example.com"),          
#     ("TestUser", ""),                   
#     ("TestUser", "invalidemail"),       
# ])
# def test_signup_negative(page, name, email):
#     page.goto("https://automationexercise.com")
#     page.click('a[href="/login"]')

#     page.fill('input[name="name"]', name)
#     page.fill('input[data-qa="signup-email"]', email)
#     page.click('button[data-qa="signup-button"]')

#     assert not page.locator('b:has-text("Enter Account Information")').is_visible()
