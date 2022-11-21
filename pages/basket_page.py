from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_added_product(self):
        assert self.is_not_element_present(
            *BasketPageLocators.ADDED_PRODUCT), "There shouldn't be any product for test guest"

    def should_be_empty_basket(self):
        assert self.browser.find_element(
            *BasketPageLocators.EMPTY_BASKET_TEXT), "There is no text, that basket is empty"
