import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_add_option(parser):
    parser.add_option('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")
    parser.add_option('--language', action='store', default="None", help="Choose language to select")


@pytest.fixture(scope="function")
def browser(request):

    browser_name = request.config.getoption("browser_name")
    chosen_language = request.config.getoption("language")

    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': chosen_language})
        options.add_experimental_option('w3c', False)
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", chosen_language)
        browser = webdriver.Firefox(firefox_profile=fp)

    yield browser

    browser.quit()

