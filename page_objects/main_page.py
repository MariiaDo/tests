from selenium.webdriver.common.by import By
from page_objects._base_page import BasePage
from page_objects.placement_page import PlacementPage


class MainPage():
    def __init__(self, driver):
        self._page = BasePage(driver)

    __loc_label = (By.XPATH, '//h1[@aria-live="assertive"]')
    __loc_sort_by = (By.XPATH, '//button[@data-testid="sorters-dropdown-trigger"]')
    __loc_sort_by_score = (By.XPATH, '//button[@data-id="class"]')
    __loc_item_title = (By.XPATH, '//div[@data-testid="property-card"]//a')
    __loc_item_score = (By.XPATH, '//div[@data-testid="review-score"]/div')
    __loc_filter_score_input = (By.XPATH, '(//div[@data-filters-item="review_score:review_score=90"])[1]')
    __loc_filter_mealplan = (By.XPATH, '(//div[@data-filters-item="mealplan:mealplan=1"])[1]')
    __loc_label_mealplan = (By.XPATH, '//span[contains(text(),"Breakfast included")]')

    def is_label_displayed(self):
        return self._page.is_displayed(self.__loc_label)

    def product_get_score(self, index=1):
        _by, _loc = self.__loc_item_score
        self._page.scroll_into_view((_by, f'({_loc})[{index}]'))
        score = self._page.get_text(self.__loc_item_score, index)
        return float(score.replace(",", "."))

    def product_get_meal_item(self, index=1):
        _by, _loc = self.__loc_label_mealplan
        self._page.scroll_into_view((_by, f'({_loc})[{index}]'))
        meal_item = self._page.get_text(self.__loc_label_mealplan, index)
        return meal_item

    def click_sort_by(self):
        self._page.click_enter(self.__loc_sort_by)
        self._page.click(self.__loc_sort_by_score)

    def check_box_filter_by_score(self):
        self._page.scroll_into_view(self.__loc_filter_score_input)
        self._page.click(self.__loc_filter_score_input)

    def check_box_filter_by_mealplan(self):
        self._page.scroll_into_view(self.__loc_filter_mealplan)
        self._page.click(self.__loc_filter_mealplan)

    def click_placement(self):
        self._page.scroll_into_view(self.__loc_item_title)
        self._page.click_enter(self.__loc_item_title)
        return PlacementPage(self._page.driver)