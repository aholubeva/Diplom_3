from src.pages.forgot_password_page import ForgotPasswordPage
import allure

class TestForgotPassword:

    @allure.title('Проверяем переход на страницу восстановления пароля по кнопке Восстановить пароль')
    def test_go_to_forgot_password_page(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.navigate_to_main_page()
        forgot_password_page.click_go_to_account_button()
        forgot_password_page.click_forgot_password_link()
        assert forgot_password_page.check_forgot_password_page()

    @allure.title('Проверяем ввод почты и клик по кнопке Восстановить')
    def test_enter_email_and_click_on_restore(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.navigate_to_forgot_password_page()
        forgot_password_page.enter_email_on_forgot_password_page()
        forgot_password_page.click_on_reset_button()
        forgot_password_page.check_reset_password_page_is_loading()
        assert forgot_password_page.check_reset_password_page()

    @allure.title('Проверяем что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.')
    def test_click_hide_password_button(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.navigate_to_forgot_password_page()
        forgot_password_page.enter_email_on_forgot_password_page()
        forgot_password_page.click_on_reset_button()
        forgot_password_page.check_reset_password_page_is_loading()
        type1 = forgot_password_page.check_hide_password_button_type()
        forgot_password_page.click_hide_password_button()
        type2 = forgot_password_page.check_hide_password_button_type()
        assert type1 == 'password'
        assert type2 == 'text'
