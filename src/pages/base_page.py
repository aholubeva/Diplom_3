from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from src.config import Config
from src.locators.base_page_locators import BasePageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def navigate(self, url):
        self.driver.get(url)

    def current_url(self):
        return self.driver.current_url

    def find_element(self, locator,timeout=10):
        return WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator))

    def click_element(self, locator, timeout=10):
        self.find_element(locator, timeout).click()

    def enter_text(self, locator, text, timeout=10):
        self.find_element(locator, timeout).send_keys(text)

    def wait_for_element_visible(self, locator,timeout=10):
        return WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def open_new_window_and_wait(self, url):
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(EC.url_to_be(url))

    def element_is_present(self, locator, timeout=10):
        return self.find_element(locator, timeout).is_displayed()

    @allure.step('Кликнуть на кнопку Личный кабинет на главной странице')
    def click_login_to_account_button(self):
        self.click_element(BasePageLocators.LOGIN_BUTTON)

    @allure.step('Проверить что текущая страница - это страница логина')
    def check_login_page(self):
        if self.current_url() == f'{Config.URL}/login':
            return True

    @allure.step('Вводим емейл')
    def enter_email(self, email):
        self.enter_text(BasePageLocators.EMAIL_FIELD, email)

    @allure.step('Вводим пароль')
    def enter_password(self, password):
        self.enter_text(BasePageLocators.PASSWORD_FIELD, password)

    @allure.step('Кликаем на кнопку Войти')
    def click_submit_button(self):
        self.click_element(BasePageLocators.SUBMIT_BUTTON)






