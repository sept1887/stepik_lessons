from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def test_guest_can_add_product_to_basket(self):
        self.check_add_to_cart_btn()
        self.add_to_cart_from_product_page()

    def check_add_to_cart_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BTN), "Add to cart button is not resented"

    def add_to_cart_from_product_page(self):
        add_to_cart_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BTN)
        add_to_cart_btn.click()

    def check_product_name_in_cart(self):
        act_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_CART).text
        exp_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_PRODUCT_PAGE).text
        assert exp_product_name == act_product_name, \
            f'Expected product name is "{exp_product_name}", but actual product name is "{act_product_name}"'

    def check_price_in_cart(self):
        act_price_in_cart = self.browser.find_element(*ProductPageLocators.BASKET_PREVIEW).text
        exp_price_in_cart = self.browser.find_element(*ProductPageLocators.PRICE_IN_PRODUCT_PAGE).text
        assert exp_price_in_cart in act_price_in_cart, "Wrong price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MSG), \
            "Success message is presented, but should not be"

    def success_msg_should_disappeared(self):
        assert self.is_disappeared(**ProductPageLocators.SUCCESS_MSG), \
            "Success message should disappeared, but it's not"








