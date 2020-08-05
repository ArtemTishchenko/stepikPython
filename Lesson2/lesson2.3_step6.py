from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    trollButton = browser.find_element_by_class_name("trollface")
    trollButton.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_id("input_value").text
    result = calc(x)
    print(result)

    resultField = browser.find_element_by_id("answer")
    resultField.send_keys(result)

    button = browser.find_element_by_tag_name("button")
    button.click()


finally:
    time.sleep(5)
    browser.quit()