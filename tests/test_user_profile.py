from src.pages.user_profile_page import UserProfilePage
import allure
from src.helpers import get_sign_in_data
from src.helpers import register_new_user
import time


class TestUserProfile:

    @allure.title('Проверяем переход по клику на Личный кабинет')
    def test_go_to_user_profile(self, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.navigate_to_main_page()
        user_profile_page.click_login_to_account_button()
        assert user_profile_page.check_login_page()

    @allure.title('Проверяем переход в раздел История заказов')
    def test_go_to_orders_history(self, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.navigate_to_main_page()
        user_profile_page.login_user()
        user_profile_page.click_login_to_account_button()
        time.sleep(3)
        user_profile_page.click_orders_history_button() #- не переходит на историю, не кликает
        assert user_profile_page.check_orders_history_page()

    @allure.title('Проверяем выход из аккаунта')
    def test_exit_account(self, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.navigate_to_main_page()
        user_profile_page.login_user()
        user_profile_page.click_login_to_account_button()
        time.sleep(3)
        user_profile_page.click_exit_button() #- не переходит на Выход, не кликает
        assert user_profile_page.check_login_page()

