from selenium.webdriver.common.by import By


class OrderFeedLocators:

    PROFILE_USER_BUTTON = By.XPATH, '//p[@class= "AppHeader_header__linkText__3q_va ml-2" and text()="Личный Кабинет"]'  # Кнопка Личный Кабинет на главной странице для зареганного пользователя
    ORDERS_HISTORY_BUTTON = By.XPATH, "//a[text()='История заказов']"  # Раздел История заказов в Профиле пользователя
    ORDERS_FEED_BUTTON = By.XPATH, "//p[text()='Лента Заказов']"
    ORDER_BLOCK = By.XPATH, "//li[@class='OrderHistory_listItem__2x95r mb-6']"
    ORDER_DETAILS = By.XPATH, "//p[@class='text text_type_digits-default']"
    ORDER_CONFIRMATION_POPUP = By.XPATH, "//p[@class='text text_type_digits-default mb-10 mt-5']"
    BUN_INGREDIENT = (By.XPATH, '//img[contains(@class,"BurgerIngredient_ingredient__image__3e-07 ml-4 mr-4") and (@alt="Флюоресцентная булка R2-D3")]')  # Первый ингредиент на табе Булки
    INGREDIENTS_LIST = By.XPATH, "//img[@alt='Перетяните булочку сюда (верх)']"
    CREATE_ORDER_BUTTON = By.XPATH, "//button[text()='Оформить заказ']"
    ORDER_CONFIRMATION_POPUP_CLOSE = By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"
    CONFIRM_ICON = (By.XPATH, '//img[contains(@class,"Modal_modal__image__2nh17") and (@alt="tick animation")]')
    LAST_ORDER = "//p[@class='text text_type_digits-default'][last()]"




