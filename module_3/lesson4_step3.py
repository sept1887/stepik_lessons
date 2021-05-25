from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    x = browser.find_element(By.ID, "num1").text
    y = browser.find_element(By.ID, "num2").text
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(int(x) + int(y)))
    browser.find_element_by_css_selector("button.btn-default").click()

finally:
    time.sleep(10)
    browser.quit()