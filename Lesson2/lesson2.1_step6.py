from selenium import webdriver
import time

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

#проверяем значение атрибута checked у people_radio
    people_radio = browser.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked == "true" , "People radio is not selected by default"

#проверяем значение атрибута checked у robots_radio
    robots_radio = browser.find_element_by_id("robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("value of robots_radio: ", robots_checked)
    assert robots_checked is None

#проверяем значение атрибута disabled у кнопки Submit
    button = browser.find_element_by_css_selector('.btn')
    button_disabled = button.get_attribute("disabled")
    print("value of button Submit: ", button_disabled)
    #проверка означает что переменная button_disabled не содержит атрибут
    assert button_disabled is None

#проверяем значение атрибута disabled у кнопки Submit после таймаута
    time.sleep(10)
    button_disabled = button.get_attribute("disabled")
    print("value of button Submit after 10sec is disabled : ", button_disabled)
    #проверка означает что у кнопки атрибут disabled не 0 или пустота
    assert button_disabled is not None

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла