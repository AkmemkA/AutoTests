# Импортируем необходимые библиотеки
import pytest  # Фреймворк для написания и запуска тестов
from selenium import webdriver  # Основной модуль Selenium для управления браузером
from selenium.webdriver.common.by import By  # Класс для указания способов поиска элементов

# URL тестируемой страницы
link = "http://selenium1py.pythonanywhere.com/"


# Фикстура - специальная функция, которая подготавливает данные для тестов
@pytest.fixture(scope="class")  # scope="class" означает, что фикстура будет вызвана один раз для всего класса тестов
def browser():
    # Действия перед началом тестов (setup)
    print("\nstart browser for test..")  # Выводим сообщение в консоль
    browser = webdriver.Chrome()  # Создаем экземпляр браузера Chrome

    # yield - ключевое слово, которое разделяет код на "до" и "после" тестов
    # Все что до yield - выполняется ДО тестов
    # Все что после yield - выполняется ПОСЛЕ тестов
    yield browser  # Передаем созданный браузер в тестовые функции

    # Действия после завершения тестов (teardown)
    print("\nquit browser..")  # Выводим сообщение в консоль
    browser.quit()  # Закрываем браузер


# Класс для группировки тестов
class TestMainPage1():
    # Первый тестовый метод
    def test_guest_should_see_login_link(self, browser):  # browser - фикстура, передается автоматически
        print("start test1")  # Выводим сообщение о начале теста

        # Открываем тестируемую страницу
        browser.get(link)

        # Ищем элемент на странице по CSS-селектору (#login_link - это id элемента)
        # Если элемент не найден, тест упадет с ошибкой
        browser.find_element(By.CSS_SELECTOR, "#login_link")

        print("finish test1")  # Выводим сообщение о завершении теста

    # Второй тестовый метод
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("start test2")  # Выводим сообщение о начале теста

        # Открываем тестируемую страницу (можно не открывать снова, если не требуется)
        browser.get(link)

        # Ищем другой элемент на странице по CSS-селектору
        # (.basket-mini .btn-group > a - это сложный селектор для поиска ссылки корзины)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

        print("finish test2")  # Выводим сообщение о завершении теста