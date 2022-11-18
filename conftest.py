import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as OptionsChrome
from selenium.webdriver.firefox.options import Options as OptionsFirefox


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store',
                     default="chrome", help="Choose browser: Chrome or Firefox")
    parser.addoption('--language', action='store',
                     default="ru", help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    browser = None

    options_chrome = OptionsChrome()
    options_chrome.add_experimental_option(
        'prefs', {'intl.accept_languages': language})

    options_firefox = OptionsFirefox()
    options_firefox.set_preference("intl.accept_languages", language)

    if browser_name == "chrome":
        print("start chrome")
        browser = webdriver.Chrome(options=options_chrome)
    elif browser_name == "firefox":
        print("start firefox")
        browser = webdriver.Firefox(options=options_firefox)
    else:
        raise pytest.UsageError("browser hasn't been chosen")
    yield browser
    browser.quit()
