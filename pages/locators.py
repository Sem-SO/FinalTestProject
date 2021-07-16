from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info>div.alertinner>p>strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    BUY_MESSAGE = (By.CSS_SELECTOR, "div#messages .alert:nth-child(1)>div>strong")