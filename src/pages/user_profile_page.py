from src.pages.base_page import BasePage
from src.locators.user_profile_page_locators import UserProfilePageLocators
import allure
from src.config import Config
from src.helpers import register_new_user


class UserProfilePage(BasePage):

    @allure.step('Открыть браузер Chrome')
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открыть главную страницу StellarBurgers')
    def navigate_to_main_page(self):
        self.navigate(Config.URL)

    @allure.step('Кликнуть на кнопку Личный кабинет на главной странице')
    def click_login_to_account_button(self):
        self.click_element(UserProfilePageLocators.LOGIN_BUTTON)

    @allure.step('Проверить что текущая страница - это страница логина')
    def check_login_page(self):
        return self.current_url() == f'{Config.URL}/login'

    @allure.step('Логин юзера')
    def login_user(self):
        email, password = register_new_user()
        self.click_login_to_account_button()
        self.enter_email(email)
        self.enter_password(password)
        self.click_submit_button()

    @allure.step('Переходим в Историю заказов в профиле пользователя')
    def click_orders_history_button(self):
        self.click_element(UserProfilePageLocators.ORDERS_HISTORY_BUTTON)

    @allure.step('Проверить что текущая страница - это страница истории заказов')
    def check_orders_history_page(self):
        return self.current_url() == f'{Config.URL}/order-history'

    @allure.step('Открыть Профиль пользователя')
    def go_to_profile_page(self):
        self.navigate(f'{Config.URL}/account/profile')

    @allure.step('Кликаем по кнопке Выход на странице Профиля')
    def click_exit_button(self):
        self.click_element(UserProfilePageLocators.EXIT_BUTTON)

