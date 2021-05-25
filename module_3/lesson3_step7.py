from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    x = browser.find_element(By.ID, "treasure").get_attribute("valuex")
    y = calc(x)
    browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(y)
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    browser.find_element_by_css_selector("button.btn-default").click()

finally:
    time.sleep(10)
    browser.quit()