from .pages.product_page import ProductPage
import time


link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"


class TestMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.test_guest_can_add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.check_product_name_in_cart()
        page.check_price_in_cart()
        time.sleep(100)
