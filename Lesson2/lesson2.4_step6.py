from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
    # найти значение элемента по ID
    correctPrice = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element_by_id("book")
    button.click()
    # скролл окна браузера до футера
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # найти значение x
    x = browser.find_element_by_id("input_value").text
    # результат функции занести в переменную result
    result = calc(x)
    # ввести результат в текстовое поле
    resultField = browser.find_element_by_id("answer")
    resultField.send_keys(result)
    # отправить форму
    button = browser.find_element_by_id("solve")
    button.click()


finally:
    time.sleep(30)
    browser.quit()
