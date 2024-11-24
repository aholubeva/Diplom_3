from src.pages.base_page import BasePage
from src.locators.forgot_password_page_locators import ForgotPasswordPageLocators
import allure
from src.config import Config
import time
from src.helpers import register_new_user


class ForgotPasswordPage(BasePage):

    @allure.step('Открыть браузер Chrome')
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открыть главную страницу StellarBurgers')
    def navigate_to_main_page(self):
        self.navigate(Config.URL)

    @allure.step('Открыть страницу восстановления пароля')
    def navigate_to_forgot_password_page(self):
        self.navigate(f'{Config.URL}/forgot-password')

    @allure.step('Кликнуть на кнопку Войти в аккаунт на главной странице')
    def click_go_to_account_button(self):
        self.click_element(ForgotPasswordPageLocators.GO_TO_ACCOUNT_BUTTON)

    @allure.step('Кликнуть на ссылку Восстановить пароль на странице логина')
    def click_forgot_password_link(self):
        self.click_element(ForgotPasswordPageLocators.FORGOT_PASSWORD_LINK)

    @allure.step('Проверить что текущая страница - это страница forgot-password')
    def check_forgot_password_page(self):
        if self.current_url() == f'{Config.URL}/forgot-password':
            return True

    @allure.step('Ввести емейл на странице восстановления пароля')
    def enter_email_on_forgot_password_page(self):
        email, password = register_new_user()
        self.enter_text(ForgotPasswordPageLocators.EMAIL_FIELD, email)

    @allure.step('Кликнуть на кнопку Восстановить на странице восстановления пароля')
    def click_on_reset_button(self):
        self.click_element(ForgotPasswordPageLocators.RESET_BUTTON)

    @allure.step('Проверить что страница reset-password загрузилась ')
    def check_reset_password_page_is_loading(self):
        self.wait_for_element_visible(ForgotPasswordPageLocators.FORGOT_PASSWORD_TITLE)
        time.sleep(3)


    @allure.step('Проверить что текущая страница - это страница reset-password')
    def check_reset_password_page(self):
        if self.current_url() == f'{Config.URL}/reset-password':
            return True

    @allure.step('Кликнуть на иконку Скрыть/показать пароль')
    def click_hide_password_button(self):
        self.click_element(ForgotPasswordPageLocators.HIDE_PASSWORD_BUTTON)

    @allure.step('Получить тип кнопки скрытия Пароля')
    def check_hide_password_button_type(self):
        password_field_type = self.find_element(ForgotPasswordPageLocators.PASSWORD_FIELD).get_attribute("type")
        return password_field_type





