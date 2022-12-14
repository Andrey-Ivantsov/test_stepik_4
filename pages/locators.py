from selenium.webdriver.common.by import By


class BasePageLoctators():
    LOGIN_LINK = (By.ID, "login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn-default:nth-child(1)")
    USER_ICON = (By.CLASS_NAME, "icon-user")


class BasketPageLocators():
    ADDED_PRODUCT = (By.CLASS_NAME, "basket_summary")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD = (By.ID, "id_registration-password1")
    REGISTRATION_PASSWORD_REPEAT = (By.ID, "id_registration-password2")
    REGISTRATION_SUBMIT = (By.NAME, "registration_submit")


class MainPageLocators():
    pass


class ProductPageLocators():
    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    ADDED_BOOK_NAME = (
        By.CSS_SELECTOR, ".alert-success:nth-child(1) .alertinner strong")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ADDED_BOOK_PRICE = (
        By.CSS_SELECTOR, ".alert:nth-child(3) .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1)")
