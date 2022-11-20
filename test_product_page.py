from .pages.product_page import ProductPage

import time
import pytest


@pytest.mark.parametrize('links', [  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    #     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    #     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    #     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    #     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    #     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    #     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    #     pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
    #                      marks=pytest.mark.xfail(reason="bug on this link")),
    #     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, links):
    link = f"{links}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_add_the_right_book()


@pytest.mark.xfail(reason="test guest should see success message after adding product to basket")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/#"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/#"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="test message shouldn't disappear after adding product to basket")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/#"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_disappear_success_message()
