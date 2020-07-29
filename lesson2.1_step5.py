from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    xElement = browser.find_element_by_css_selector(".nowrap + #input_value")
    x = xElement.text
    y = calc(x)
    time.sleep(1)
    input = browser.find_element_by_id("answer")
    input.send_keys(y)
    time.sleep(1)
    #click on checkbox
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    time.sleep(1)
    #click on radiobutton
    radiobutton = browser.find_element_by_css_selector("[for='robotsRule']")
    radiobutton.click()
    time.sleep(1)
    #click on submit button
    submitButton = browser.find_element_by_css_selector("[type='submit']")
    submitButton.click()

finally:
    time.sleep(8)
    browser.quit()
