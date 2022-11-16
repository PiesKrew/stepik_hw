from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_language_check(browser):
    browser.get(link)
    # time.sleep(30)
    basket_button = WebDriverWait(browser, 3).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "btn-add-to-basket")), "No add to cart button on page").text
    print(basket_button)
    assert basket_button == "Correct!", "PASS"




