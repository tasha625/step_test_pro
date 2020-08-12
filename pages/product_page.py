from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    # def should_be_product_page(self):
    #     self.should_be_login_url()
    #     self.should_be_login_form()

    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRICE).text

    def check_success_added_alert(self, book_name):
        success_added_alerts = self.browser.find_elements(*ProductPageLocators.ADDED_ALERTS)
        assert book_name == success_added_alerts[0].text, f"{book_name} is absent in success message"

    def check_basket_price(self, book_price):
        price_in_bascket_alert = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET_ALERT).text
        assert book_price in price_in_bascket_alert, f"{book_price} is absent in message"
        price_in_bascket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET).text
        assert book_price in price_in_bascket, f"{book_price} is absent in basket"
