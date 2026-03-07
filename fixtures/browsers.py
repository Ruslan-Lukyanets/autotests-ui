import allure
import pytest
import os
from playwright.sync_api import Page, Playwright

from pages.authentication.registration_page import RegistrationPage
from _pytest.fixtures import SubRequest

@pytest.fixture
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        context.tracing.start(screenshots=True, snapshots=True, sources=True)

        yield browser.new_page()

        context.tracing.stop(path=f'./tracing/{request.node.name}.zip')
        browser.close()

        allure.attach.file(f'./tracing/{request.node.name}.zip', name='trace', extension='zip')

@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        registration_page = RegistrationPage(page=page)
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.registration_form.fill(email='user@gmail.com', username='username', password='password')
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.click_registration_button()

        parent_dir = os.path.dirname(os.path.abspath(__file__))
        root_dir = os.path.dirname(parent_dir)
        storage_state_path = os.path.join(root_dir, "browser-state.json")
        context.storage_state(path=storage_state_path)
        browser.close()

@pytest.fixture
def chromium_page_with_state(request: SubRequest, initialize_browser_state, playwright: Playwright):
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")
        context.tracing.start(screenshots=True, snapshots=True, sources=True)

        yield context.new_page()

        context.tracing.stop(path=f'./tracing/{request.node.name}.zip')
        browser.close()

        allure.attach.file(f'./tracing/{request.node.name}.zip', name='trace', extension='zip')