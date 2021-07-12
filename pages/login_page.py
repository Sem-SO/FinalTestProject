from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):  # проверка наличия подстроки login в url
        assert "login" in self.browser.current_url, "login not in url"

    def should_be_login_form(self):  # проверка наличия на странице формы для логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self): # проверка наличия на странице формы для регистрации
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not present"
