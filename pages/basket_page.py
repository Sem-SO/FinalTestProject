from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def should_be_basket_page(self):
        self.check_basket_is_empty()
        self.check_message_about_basket_is_empty()


    def check_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT), "basket is not empty"

    def check_message_about_basket_is_empty(self):
        message = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE)
        assert message, "message 'basket is empty' is absent"

