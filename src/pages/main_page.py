from src.pages.base_page import BasePage
from src.locators.main_page_locators import MainPageLocators
import allure
from src.config import Config
from selenium.webdriver.common.action_chains import ActionChains
from src.helpers import register_new_user


class MainPage(BasePage):

    @allure.step('Открыть браузер Chrome')
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открыть главную страницу StellarBurgers')
    def navigate_to_main_page(self):
        self.navigate(Config.URL)

    @allure.step('Логин юзера')
    def login_user(self):
        email, password = register_new_user()
        self.click_login_to_account_button()
        self.enter_email(email)
        self.enter_password(password)
        self.click_submit_button()

    @allure.step('Перейти на табу Конструктор')
    def navigate_to_constructor_tab(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_TAB)

    @allure.step('Проверить что текущая таба - Конструктор')
    def check_constructor_tab(self):
        return self.element_is_present(MainPageLocators.CONSTRUCTOR_TAB_TITLE)

    @allure.step('Перейти на табу Лента Заказов')
    def navigate_to_order_feed_tab(self):
        self.click_element(MainPageLocators.ORDER_FEED_TAB)

    @allure.step('Проверить что текущая таба - Лента Заказов')
    def check_order_feed_tab(self):
        if self.element_is_present(MainPageLocators.ORDER_FEED_TAB_TITLE) and self.current_url() == f'{Config.URL}/feed':
            return True

    @allure.step('Кликнуть на ингредиент')
    def click_on_ingredient(self):
        self.click_element(MainPageLocators.BUN_INGREDIENT)

    @allure.step('Проверить появление всплывающего окна с деталями ингредиента')
    def check_ingredient_details_popup(self):
        return self.wait_for_element_visible(MainPageLocators.INGREDIENT_POPUP)

    @allure.step('Закрыть всплывающее окно с деталями ингредиента')
    def close_ingredient_details_popup(self):
        self.click_element(MainPageLocators.CLOSE_INGREDIENT_POPUP_BUTTON)

    @allure.step('Добавить ингредиент в заказ')
    def add_ingredient_to_order(self):
        action = ActionChains(self.driver)
        source_element = self.find_element(MainPageLocators.BUN_INGREDIENT)
        target_element = self.find_element(MainPageLocators.INGREDIENTS_LIST)
        action.drag_and_drop(source_element, target_element).perform()

    @allure.step('Проверить значение каунтера для ингредиента')
    def check_ingredient_counter(self):
        counter_value = self.find_element(MainPageLocators.INGREDIENT_COUNTER).text
        return counter_value

    @allure.step('Кликнуть на кнопку Оформить заказ')
    def click_on_create_order_button(self):
        self.click_element(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Проверить появление всплывающего окна с подтверждением создания заказа')
    def check_confirmation_order_popup(self):
        return self.wait_for_element_visible(MainPageLocators.ORDER_CONFIRMATION_POPUP)








