from src.pages.main_page import MainPage
import allure


class TestMainPage:

    @allure.title('Проверяем переход по клику на «Конструктор» табу')
    def test_go_to_constructor_tab(self, driver):
        main_page = MainPage(driver)
        main_page.navigate_to_main_page()
        main_page.navigate_to_constructor_tab()
        assert main_page.check_constructor_tab()

    @allure.title('Проверяем переход по клику на табу «Лента заказов»')
    def test_go_to_orders_feed_tab(self, driver):
        main_page = MainPage(driver)
        main_page.navigate_to_main_page()
        main_page.navigate_to_order_feed_tab()
        assert main_page.check_order_feed_tab()

    @allure.title('Проверяем что по клику на ингредиент показывается всплывающее окно с деталями')
    def test_click_on_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.navigate_to_main_page()
        main_page.click_on_ingredient()
        assert main_page.check_ingredient_details_popup()

    @allure.title('Проверяем что всплывающее окно закрывается кликом по крестику')
    def test_click_on_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.navigate_to_main_page()
        main_page.click_on_ingredient()
        main_page.check_ingredient_details_popup()
        main_page.close_ingredient_details_popup()
        main_page.click_on_ingredient()
        assert main_page.check_ingredient_details_popup()

    @allure.title('Проверяем что при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_counter_of_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.navigate_to_main_page()
        first_counter_value = main_page.check_ingredient_counter()
        main_page.add_ingredient_to_order()
        second_counter_value = main_page.check_ingredient_counter()
        assert first_counter_value == "0"
        assert second_counter_value == "2"

    @allure.title('Проверяем что залогиненный пользователь может оформить заказ')
    def test_create_order(self, driver):
        main_page = MainPage(driver)
        main_page.navigate_to_main_page()
        main_page.login_user()
        main_page.add_ingredient_to_order()
        main_page.click_on_create_order_button()
        assert main_page.check_confirmation_order_popup()




