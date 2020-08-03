import pytest
from selenium import webdriver
import time
import math



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(15)
    yield browser
    print("\nquit browser..")
    browser.quit()

# декоратор для параметризации запросов, зайти на 9 страниц с разными ID
@pytest.mark.parametrize('id', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905" ])
# в функцию передаем аргументы фикстуры browser и ID с декоратора параметризации
def test_guest_should_see_login_link(browser, id):
    # функция откроет 9 раз разные уроки, разница только в {id}
    link = f"https://stepik.org/lesson/{id}/step/1"
    # открыть браузер
    browser.get(link)
    # найти текстовое поле
    textArea = browser.find_element_by_css_selector("div .show-plugin > div .textarea")
    # функция подсчета ответа (будет вызвана 9 раз)
    answer = str(math.log(int(time.time())))
    # добавить результат функции answer в текстовое поле
    textArea.send_keys(answer)
    # найти кнопку
    button = browser.find_element_by_css_selector("div .attempt__actions > button.submit-submission")
    # нажать на кнопку
    button.click()
    # найти текст который появляется после отправки формы
    correctText = browser.find_element_by_css_selector("div .smart-hints__feedback > pre.smart-hints__hint").text
    # сравнение что текст соответствует
    assert correctText == "Correct!", f"NOOOOOO, current text: {correctText} "
    #assert correctText == correctText, f"NOOOOOO, current text: {correctText} "
    time.sleep(3)
