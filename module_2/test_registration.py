from selenium import webdriver
from sys import argv
import time

script_name, link = argv

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    name = browser.find_element_by_xpath("//div[@class='first_block']/div[1]/input")
    input_name = name.send_keys("Ivan")
    last_name = browser.find_element_by_xpath("//div[@class='first_block']/div[2]/input")
    input_last_name = last_name.send_keys("Ivanov")
    email = browser.find_element_by_xpath("//div[@class='first_block']/div[3]/input")
    input_email = email.send_keys("ivanov1@mail.ru")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    # time.sleep(1)

    # Находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # С помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # Ожидание чтобы визуально оценить результаты прохождения скрипта
    # time.sleep(10)

    # Закрываем браузер после всех манипуляций
    browser.quit()