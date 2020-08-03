import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

# фикстура для функций
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    # yield сработает толко после прогона всех кейсов (функций def)
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():
    # метка смоук
    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
    # метка регресс тестов
    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")