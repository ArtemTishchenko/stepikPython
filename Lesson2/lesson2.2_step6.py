from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)
    x = browser.find_element_by_id("input_value").text
    result = calc(x)
    time.sleep(1)

    # проскролить вниз на 150 px
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("window.scrollBy(0, 150);", button)

    # ввести ответ
    resultField = browser.find_element_by_id("answer")
    resultField.send_keys(result)

    # найти checkbox
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    # найти radiobutton
    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()

    # отправить форму
    button.click()



finally:
    time.sleep(5)
    browser.quit()
