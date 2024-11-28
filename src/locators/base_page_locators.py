from selenium.webdriver.common.by import By


class BasePageLocators:

    LOGIN_BUTTON = By.XPATH, "//p[text()='Личный Кабинет']" # Кнопка Личный Кабинет на главной странице
    EMAIL_FIELD = By.XPATH, "//label[text() = 'Email']/following-sibling::input"  # Поле Email для существующего юзера
    PASSWORD_FIELD = By.XPATH, "//label[text() = 'Пароль']/following-sibling::input"  # Поле Пароль для существующего юзера
    SUBMIT_BUTTON = By.XPATH, "//button[text()='Войти']"  # Кнопка Войти для существующего юзера