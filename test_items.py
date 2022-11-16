from selenium.webdriver.common.by import By
# import time


link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_language_check(browser):
    browser.get(link)
    # time.sleep(30)
    basket_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")

    assert basket_button, 'No button here!'
