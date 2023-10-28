from selenium.webdriver.common.by import By
from page_objects._base_page import BasePage
from page_objects.main_page import MainPage


class StartPage():
    def __init__(self, driver):
        self._page = BasePage(driver)

    __loc_box_recently_searched = (By.XPATH, '//*[@id="bodyconstraint-inner"]/div[1]/div[6]/div[2]/ul/li[1]//a')
    __loc_box_popular_direction = (By.XPATH, '//*[@data-testid="destination-postcards-firstrow"]//a')

    def recently_searched_box_is_present(self):
        return self._page.is_displayed(self.__loc_box_recently_searched)

    def click_popular_direction_box(self):
        self._page.scroll_into_view(self.__loc_box_popular_direction)
        self._page.click(self.__loc_box_popular_direction)
        return MainPage(self._page.driver)
