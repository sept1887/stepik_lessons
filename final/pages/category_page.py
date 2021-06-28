from .base_page import BasePage
from .locators import CategoryPageLocators

class CategoryPage(BasePage):
    def go_to_main_page(self):
        main_page_link = self.browser.find_element(*CategoryPageLocators.MAIN_PAGE_LINK)
        main_page_link.click()

    def go_to_next_page(self):
        next_page_link = self.browser.find_element(*CategoryPageLocators.NEXT_PAGE_LINK)
        next_page_link.click()

    def should_be_main_page_link(self):
        assert self.is_element_present(*CategoryPageLocators.MAIN_PAGE_LINK), \
            "Main page link is not presented"

    def should_be_previous_page_link(self):
        assert self.is_element_present(*CategoryPageLocators.PREVIOUS_PAGE_LINK), \
            "Previous page link is not presented"
