from selenium.webdriver.common.by import By


class UserProfilePageLocators:

    LOGIN_BUTTON = By.XPATH, "//p[text()='Личный Кабинет']" # Кнопка Личный Кабинет на главной странице
    ORDERS_HISTORY_BUTTON = By.XPATH, '//a[@class="Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9"]'  # Раздел История заказов в Профиле пользователя
    PROFILE_USER_BUTTON = By.XPATH, '//a[contains(@href,"/account")]' # Кнопка Личный Кабинет на главной странице для зареганного пользователя
    EXIT_BUTTON = By.XPATH, "//button[text()='Выход']"



    #ORDERS_HISTORY_BUTTON = By.XPATH, '//a[contains( @ href, "/account/order-history")]'
    #//button[ @class ='Account_button__14Yp3 text text_type_main-medium text_color_inactive']


