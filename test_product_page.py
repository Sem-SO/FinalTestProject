import time
import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.locators import BasePageLocators
from .pages.login_page import LoginPage


@pytest.mark.parametrize("link", ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
                                               "/?promo=offer7", marks=pytest.mark.xfail),  # xfail на случай если
                                  # баг не собираютя чинить
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])


def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.check_success_messege_after_adding_to_shopping_basket()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.check_success_message_before_adding_to_shopping_basket()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.chech_success_message_disappeared_after_adding_to_shopping_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_page(*BasePageLocators.LOGIN_LINK, LoginPage)


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    basket_page = page.go_to_page(*BasePageLocators.BASKET_LINK, BasketPage)
    basket_page.should_be_basket_page()


@pytest.mark.registration
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        email = str(time.time()) + "@fakemail.org"
        page = LoginPage(browser, self.link)
        page.open()
        page.register_new_user(email, "123qwerty@#!")
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        product_page = ProductPage(browser, self.link)
        product_page.open()
        product_page.check_success_message_before_adding_to_shopping_basket()

    def test_user_can_add_product_to_basket(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        product_page = ProductPage(browser, self.link)
        product_page.open()
        product_page.add_to_shopping_basket()
