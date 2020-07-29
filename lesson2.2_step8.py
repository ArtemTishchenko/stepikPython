from selenium import webdriver
import time
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    firstName = browser.find_element_by_name("firstname")
    firstName.send_keys("Artur")
    lastName = browser.find_element_by_name("lastname")
    lastName.send_keys("Pirozkov")
    email = browser.find_element_by_name("email")
    email.send_keys("pirozkov@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'android.txt')
    # print(os.path.abspath(__file__))
    # print(os.path.abspath(os.path.dirname(__file__)))
    fileButton = browser.find_element_by_id("file")
    fileButton.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()




finally:
    time.sleep(3)
    browser.quit()
