from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//*[@id='default']/header/div[1]/div/div[2]/span/a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    EMPTY_BASKET_MSG = (By.ID, "content_inner")
    ITEM_IN_BASKET = (By.CLASS_NAME, "basket-items")

class CategoryPageLocators:
    MAIN_PAGE_LINK = (By.XPATH, "//a[contains(text(), 'Home')]")
    NEXT_PAGE_LINK = (By.XPATH, "//a[contains(text(), 'next')]")
    PREVIOUS_PAGE_LINK = (By.XPATH, "//a[contains(text(), 'previous')]")


class MainPageLocators:
    ADD_TO_BASKET_BTN = (By.XPATH, "//button[contains(text(), 'Add to basket')]")
    WELCOME_TXT = (By.XPATH, "//h2[contains(text(), 'Welcome!')]")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_NAME = (By.NAME, "login-username")
    LOGIN_PASSWORD = (By.NAME, "login-password")
    LOGIN_BTN = (By.NAME, "login_submit")


class ProductPageLocators:
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME_IN_CART = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    BASKET_PREVIEW = (By.CLASS_NAME, "basket-mini")
    PRODUCT_NAME_IN_PRODUCT_PAGE = (By.TAG_NAME, "h1")
    PRICE_IN_PRODUCT_PAGE = (By.CLASS_NAME, "price_color")
    SUCCESS_MSG = (By.XPATH, "//*[@id='messages']/div[1]/div")


