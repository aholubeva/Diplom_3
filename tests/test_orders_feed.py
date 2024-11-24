from src.pages.order_feed_page import OrderFeed
import allure
import time


class TestOrderFeed:

    @allure.title('Проверить, что по клику на заказ, откроется всплывающее окно с деталями')
    def test_order_details_popup(self, driver):
        order_feed = OrderFeed(driver)
        order_feed.navigate_to_main_page()
        order_feed.navigate_to_order_feed_page()
        order_number_on_tile = order_feed.click_on_order_tile()
        order_number_on_popup = order_feed.check_order_confirmation_popup()
        assert order_number_on_popup == order_number_on_tile

    @allure.title('Проверить, что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_order_from_history_is_displayed_in_feed(self, driver):
        order_feed = OrderFeed(driver)
        order_feed.navigate_to_main_page()
        order_feed.login_user()
        order_feed.create_order()
        time.sleep(5)
        order_feed.navigate_to_user_profile()
        order_feed.navigate_to_order_history()
        time.sleep(5)
        order_feed.scroll_to_the_last_order()
        order_number_in_history = order_feed.check_order_number_in_history()
        order_feed.navigate_to_order_feed_page()
        order_number_in_feed = order_feed.check_order_number_in_feed()

        assert order_number_in_history == order_number_in_feed






