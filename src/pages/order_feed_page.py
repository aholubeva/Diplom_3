from src.pages.base_page import BasePage
from src.locators.order_feed_page_locators import OrderFeedLocators
import allure
from src.config import Config
from src.helpers import register_new_user
from src.helpers import get_sign_in_data
from selenium.webdriver.common.action_chains import ActionChains
import time


class OrderFeed(BasePage):

    @allure.step('Открыть браузер Chrome')
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открыть главную страницу StellarBurgers')
    def navigate_to_main_page(self):
        self.navigate(Config.URL)

    @allure.step('Логин юзера')
    def login_user(self):
        email, password = get_sign_in_data()
        self.click_login_to_account_button()
        self.enter_email(email)
        self.enter_password(password)
        self.click_submit_button()

    @allure.step('Перейти в Личный кабинет')
    def navigate_to_user_profile(self):
        self.click_element(OrderFeedLocators.PROFILE_USER_BUTTON)

    @allure.step('Перейти в Историю заказов')
    def navigate_to_order_history(self):
        self.click_element(OrderFeedLocators.ORDERS_HISTORY_BUTTON)

    @allure.step('Перейти в Ленту заказов')
    def navigate_to_order_feed_page(self):
        self.click_element(OrderFeedLocators.ORDERS_FEED_BUTTON)

    @allure.step('Кликнуть на заказ и запомнить номер заказа')
    def click_on_order_tile(self):
        order_number_on_tile = self.find_element(OrderFeedLocators.ORDER_DETAILS).text
        self.click_element(OrderFeedLocators.ORDER_BLOCK)
        return order_number_on_tile

    @allure.step('Проверить всплывающее окно с деталями заказа и сравнить номер заказа')
    def check_order_confirmation_popup(self):
        self.element_is_present(OrderFeedLocators.ORDER_CONFIRMATION_POPUP)
        order_number_on_popup = self.find_element(OrderFeedLocators.ORDER_CONFIRMATION_POPUP).text
        return order_number_on_popup

    @allure.step('Оформить заказ и запомнить номер заказа')
    def create_order(self):
        action = ActionChains(self.driver)
        source_element = self.find_element(OrderFeedLocators.BUN_INGREDIENT)
        target_element = self.find_element(OrderFeedLocators.INGREDIENTS_LIST)
        action.drag_and_drop(source_element, target_element).perform()
        self.click_element(OrderFeedLocators.CREATE_ORDER_BUTTON)
        time.sleep(5)
        order_number_on_popup = self.check_order_confirmation_popup()
        self.click_element(OrderFeedLocators.ORDER_CONFIRMATION_POPUP_CLOSE)
        return order_number_on_popup

    @allure.step('Проскроллить до последнего созданного заказа в Истории заказов')
    def scroll_to_the_last_order(self):
        #element = self.driver.find_element(OrderFeedLocators.ORDER_BLOCK).last
        #return self.driver.execute_script("arguments[0].scrollIntoView()", element)
        return self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    @allure.step('Проверить номер последнего созданного заказа в Истории заказов')
    def check_order_number_in_history(self):
        order_number_in_history = self.find_element(OrderFeedLocators.ORDER_DETAILS)[last].text
        return order_number_in_history

    @allure.step('Проверить номер последнего созданного заказа в Ленте заказов')
    def check_order_number_in_feed(self):
        order_number_in_feed = self.find_element(OrderFeedLocators.ORDER_BLOCK).text
        return order_number_in_feed






