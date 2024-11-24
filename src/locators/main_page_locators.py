from selenium.webdriver.common.by import By


class MainPageLocators:

    CONSTRUCTOR_TAB = By.XPATH, "//p[text()='Конструктор']" # Таба Конструктор в хедере
    CONSTRUCTOR_TAB_TITLE = By.XPATH, "//h1[text()='Соберите бургер']" # Заголовок на  Конструктор табе
    ORDER_FEED_TAB = By.XPATH, "//p[text()='Лента Заказов']"  # Таба Лента заказов в хедере
    ORDER_FEED_TAB_TITLE = By.XPATH, "//h1[text()='Лента заказов']"  # Заголовок на табе Лента заказов
    BUN_INGREDIENT = (By.XPATH, '//img[contains(@class,"BurgerIngredient_ingredient__image__3e-07 ml-4 mr-4") and (@alt="Флюоресцентная булка R2-D3")]') #Первый ингредиент на табе Булки
    INGREDIENT_POPUP = By.XPATH, "//h2[text() = 'Детали ингредиента']" # Всплывающее окно с деталями ингредиента
    CLOSE_INGREDIENT_POPUP_BUTTON = By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK')]" #Кнопка закрытия всплывающего окна с деталями ингредиента
    INGREDIENTS_LIST = By.XPATH, "//img[@alt='Перетяните булочку сюда (верх)']" #Список добавленных ингредиентов
    INGREDIENT_COUNTER = By.XPATH, "//p[@class='counter_counter__num__3nue1']" #Счетчик ингредиента
    CREATE_ORDER_BUTTON = By.XPATH, "//button[text()='Оформить заказ']" #Кнопка Оформить заказ
    ORDER_CONFIRMATION_POPUP = By.XPATH, "//div[@class='Modal_modal__contentBox__sCy8X pt-30 pb-30']" #Попап с подтверждением заказа





