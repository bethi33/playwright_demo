# import pytest
# from playwright.sync_api import sync_playwright
# from utils import config

# @pytest.fixture(scope="session")
# def browser():
#     with sync_playwright() as p:
#         browser = getattr(p.config.Browser).launch(
#             headless=p.config.HEADLESS,
#             slow_mo=p.config.SLOW_MO
#         )
#         yield browser
#         browser.close()

# @pytest.fixture
# def page(browser):
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto(config.BASE_URL)
#     yield page
#     page.close()
#     context.close()

import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context(viewport=None)
    page = context.new_page()
    yield page
    context.close()
