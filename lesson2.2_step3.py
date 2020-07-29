from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/selects1.html"
    browser.get(link)

    # нахождение значений
    numberOne = browser.find_element_by_id("num1").text
    print(numberOne)
    numberTwo = browser.find_element_by_id("num2").text
    print(numberTwo)

    # подсчет суммы
    result: str = str(int(numberOne) + int(numberTwo))
    print(result)

    # нахождеие выпадающего текста
    dropdown = Select(browser.find_element_by_id("dropdown"))
    dropdown.select_by_visible_text(result)

    # найти и нажать кнопку
    submitButton = browser.find_element_by_css_selector(".btn")
    submitButton.click()


finally:
    time.sleep(20)
    browser.quit()
