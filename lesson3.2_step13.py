import unittest
from selenium import webdriver
import time

# код из уроков 1.6_step10 + step 11

class RegistrationTest(unittest.TestCase):

    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        firstNameField = browser.find_element_by_css_selector(".form-control.first[required]")
        firstNameField.send_keys("lol")
        lastNameField = browser.find_element_by_css_selector(".form-control.second[required]")
        lastNameField.send_keys("lol")
        emailField = browser.find_element_by_css_selector(".form-control.third[required]")
        emailField.send_keys("lol")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")

        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        browser.quit()



    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        firstNameField = browser.find_element_by_css_selector(".form-control.first[required]")
        firstNameField.send_keys("lol")
        lastNameField = browser.find_element_by_css_selector(".form-control.second[required]")
        lastNameField.send_keys("lol")
        emailField = browser.find_element_by_css_selector(".form-control.third[required]")
        emailField.send_keys("lol")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")

        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        browser.quit()

if __name__  == "__main__":
    unittest.main()