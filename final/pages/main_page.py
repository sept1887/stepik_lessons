from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def should_not_be_add_to_basket_btn(self):
        assert self.is_not_element_present(*MainPageLocators.ADD_TO_BASKET_BTN), \
            "Add to basket button is presented, but should not be"

    def should_be_welcome_text(self):
        assert self.is_element_present(*MainPageLocators.WELCOME_TXT), \
            "Welcome text is not presented"
