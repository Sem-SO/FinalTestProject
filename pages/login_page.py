from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    """Проверка наличия подстроки 'login' в url страницы"""

    def should_be_login_url(self):  # проверка наличия подстроки login в url
        assert "login" in self.browser.current_url, "login not in url"

    """Проверка наличия формы для логина"""

    def should_be_login_form(self):  # проверка наличия на странице формы для логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    """Проверка наличия формы для регистрации"""

    def should_be_register_form(self):  # проверка наличия на странице формы для регистрации
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not present"

    """Метод, регистрирующий нового пользователя"""

    def register_new_user(self, email, password):
        email_form = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_EMAIL_ADRESS)
        password_form = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_PASSWORD)
        password_form_repeat = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_PASSWORD_REPEAT)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTON)
        email_form.send_keys(email)
        password_form.send_keys(password)
        password_form_repeat.send_keys(password)
        registration_button.click()
