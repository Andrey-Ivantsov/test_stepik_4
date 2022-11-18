from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math
import time


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(
            *ProductPageLocators.BASKET_BUTTON)
        add_to_basket_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            # alert_text = alert.text
            # print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_add_the_right_book(self):
        added_book_name = self.browser.find_element(
            *ProductPageLocators.ADDED_BOOK_NAME).text
        book_name = self.browser.find_element(
            *ProductPageLocators.BOOK_NAME).text
        assert added_book_name == book_name, "wrong book added"

        added_book_price = self.browser.find_element(
            *ProductPageLocators.ADDED_BOOK_PRICE).text
        book_price = self.browser.find_element(
            *ProductPageLocators.BOOK_PRICE).text
        assert added_book_price == book_price, "added price doesn't match book price"
