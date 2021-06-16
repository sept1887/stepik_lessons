from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME_IN_CART = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    BASKET_PREVIEW = (By.CLASS_NAME, "basket-mini")
    PRODUCT_NAME_IN_PRODUCT_PAGE = (By.TAG_NAME, "h1")
    PRICE_IN_PRODUCT_PAGE = (By.CLASS_NAME, "price_color")


