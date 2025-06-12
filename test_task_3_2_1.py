import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def fill_form(self, link):
        self.browser.get(link)

        required_inputs = self.browser.find_elements(By.CSS_SELECTOR, "input[required]")

        # Универсальный словарь для всех возможных placeholder'ов
        placeholder_data = {
            "Input your first name": "Akhmed",
            "Input your name": "Akhmed",  # Для registration2.html
            "Input your last name": "Kadiev",
            "Input your email": "akhmed@example.com",
        }

        # Заполняем все обязательные поля
        for input_field in required_inputs:
            placeholder = input_field.get_attribute("placeholder")
            if placeholder in placeholder_data:
                input_field.send_keys(placeholder_data[placeholder])
            else:
                # Если встретится неизвестный placeholder, используем значение по умолчанию
                input_field.send_keys("DefaultValue")
                print(f"Used default value for: {placeholder}")

        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Ожидаем появления заголовка
        welcome_text_elt = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.TAG_NAME, "h1"))
        )
        return welcome_text_elt.text

    def test_registration1(self):
        welcome_text = self.fill_form("http://suninjuly.github.io/registration1.html")
        self.assertEqual(
            welcome_text,
            "Congratulations! You have successfully registered!",
            f'Текст "{welcome_text}" не соответствует ожидаемому'
        )

    def test_registration2(self):
        welcome_text = self.fill_form("http://suninjuly.github.io/registration2.html")
        self.assertEqual(
            welcome_text,
            "Congratulations! You have successfully registered!",
            f'Текст "{welcome_text}" не соответствует ожидаемому'
        )


if __name__ == "__main__":
    unittest.main()