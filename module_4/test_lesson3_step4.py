import unittest
from selenium import webdriver
from sys import argv
import time

# script_name, link = argv


class TestForms(unittest.TestCase):
    def test_registration_from_1(self):
        browser = webdriver.Chrome()

        try:
            browser.get("http://suninjuly.github.io/registration1.html")

            # Ваш код, который заполняет обязательные поля
            name = browser.find_element_by_xpath("//div[@class='first_block']/div[1]/input")
            name.send_keys("Ivan")
            last_name = browser.find_element_by_xpath("//div[@class='first_block']/div[2]/input")
            last_name.send_keys("Ivanov")
            email = browser.find_element_by_xpath("//div[@class='first_block']/div[3]/input")
            email.send_keys("ivanov1@mail.ru")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # Находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # С помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

        finally:
            # Ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)

            # Закрываем браузер после всех манипуляций
            browser.quit()

    def test_registration_from_2(self):
        browser = webdriver.Chrome()

        try:
            browser = webdriver.Chrome()
            browser.get("http://suninjuly.github.io/registration2.html")

            # Ваш код, который заполняет обязательные поля
            name = browser.find_element_by_xpath("//div[@class='first_block']/div[1]/input")
            name.send_keys("Ivan")
            last_name = browser.find_element_by_xpath("//div[@class='first_block']/div[2]/input")
            last_name.send_keys("Ivanov")
            email = browser.find_element_by_xpath("//div[@class='first_block']/div[3]/input")
            email.send_keys("ivanov1@mail.ru")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # Находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # С помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

        finally:
            # Ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)

            # Закрываем браузер после всех манипуляций
            browser.quit()


if __name__ == "__main__":
    unittest.main()