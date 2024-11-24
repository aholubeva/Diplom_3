from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:

    GO_TO_ACCOUNT_BUTTON = (By.XPATH, '//button[contains(@class,"button_button__33qZ0 button_button_type_primary") and (text()="Войти в аккаунт")]')
    FORGOT_PASSWORD_LINK = (By.XPATH, '//a[contains(@href,"/forgot-password")]')
    FORGOT_PASSWORD_TITLE = (By.XPATH, '//h2[text()="Восстановление пароля"]')
    EMAIL_FIELD = (By.XPATH, '//input[contains(@class,"text input__textfield text_type_main-default")]')
    RESET_BUTTON = (By.XPATH, '//button[contains(@class,"button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa") and (text()="Восстановить")]')
    HIDE_PASSWORD_BUTTON = (By.XPATH, '//div[contains(@class,"input__icon input__icon-action")]')
    PASSWORD_FIELD = (By.XPATH, '//input[@name = "Введите новый пароль"]')



