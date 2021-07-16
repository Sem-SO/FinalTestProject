from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.check_shoping_basket()

    def add_to_shopping_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()
        self.solve_quiz_and_get_code()

    def check_shoping_basket(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        self.add_to_shopping_basket()
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        buy_message = self.browser.find_element(*ProductPageLocators.BUY_MESSAGE).text

        assert book_price == basket_price, "prices are not equal"
        print("Цены това и корзины совпадают")
        assert buy_message, "message is missed"
        print("Присутствует сообщение о добавлении товара в корзину")
        assert book_name == buy_message, "books name are not equal"
        print("Названия книг соответствуют")

    def check_success_messege_after_adding_to_shopping_basket(self):
        self.add_to_shopping_basket()
        assert self.is_not_element_present(*ProductPageLocators.BUY_MESSAGE), "Success message is presented, but should not be"

    def check_success_message_before_adding_to_shopping_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.BUY_MESSAGE), "Success message is presented, but should not be"

    def chech_success_message_disappeared_after_adding_to_shopping_basket(self):
        self.add_to_shopping_basket()
        assert self.is_disappeared(*ProductPageLocators.BUY_MESSAGE), "Success message is not disappeared, but should be"






