from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, ".basket-mini")
    PRICE_IN_BASKET_ALERT = (By.CSS_SELECTOR, ".alert-info strong")
    ADDED_ALERTS = (By.CSS_SELECTOR, ".alert-success strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
