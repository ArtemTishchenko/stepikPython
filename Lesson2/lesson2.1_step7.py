from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/get_attribute.html"
    browser.get(link)
    # поиск атрибута картинки
    image = browser.find_element_by_css_selector("h2 > img")
    imageAttribute = image.get_attribute("valuex")
    # подсчет формулы
    x = imageAttribute
    result = calc(x)
    # найти поле и ввести ответ
    resultFild = browser.find_element_by_id("answer")
    resultFild.send_keys(result)
    # найти чекбокс
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    # найти radiobutton
    radioButton = browser.find_element_by_id("robotsRule")
    radioButton.click()
    # найти кнопку
    submitButton = browser.find_element_by_css_selector(".btn")
    submitButton.click()

finally:
    time.sleep(5)
    browser.quit()
