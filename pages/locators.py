from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group>a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_FORM_EMAIL_ADRESS = (By.CSS_SELECTOR, "input#id_registration-email")
    REGISTRATION_FORM_PASSWORD = (By.CSS_SELECTOR, "input#id_registration-password1")
    REGISTRATION_FORM_PASSWORD_REPEAT = (By.CSS_SELECTOR, "input#id_registration-password2")
    REGISTRATION_BUTON = (By.CSS_SELECTOR, "[name=registration_submit]")
    TO_BOOKS = (By.CSS_SELECTOR, "li.dropdown-submenu>a")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info>div.alertinner>p>strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    BUY_MESSAGE = (By.CSS_SELECTOR, "div#messages .alert:nth-child(1)>div>strong")


class BasketPageLocators():
    BASKET_IS_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p")
    BASKET_PRODUCT = (By.CSS_SELECTOR, "h2.col-sm-6.h3")
