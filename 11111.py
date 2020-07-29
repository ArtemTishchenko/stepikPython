from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    f_name = browser.find_element_by_css_selector("div.first_block>div.first_class.form-group:nth-child(1) > input")
    f_name.send_keys('Dm')
    s_name = browser.find_element_by_css_selector("div.first_block>div.second_class.form-group:nth-child(2) > input")
    s_name.send_keys('Sor')
    email = browser.find_element_by_css_selector("div.first_block>div.third_class.form-group:nth-child(3) > input")
    email.send_keys('a@mail.com')
    phone = browser.find_element_by_css_selector("div.second_block>div.first_class.form-group:nth-child(1) > input")
    phone.send_keys('12345')
    adress = browser.find_element_by_css_selector("div.second_block>div.first_class.form-group:nth-child(1) > input")
    adress.send_keys('dlan_miloserdia')

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    #time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
