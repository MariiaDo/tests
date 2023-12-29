from selenium.webdriver.common.by import By
from page_objects._base_page import BasePage
from utilities.deco import auto_step


@auto_step
class PlacementPage():
    def __init__(self, driver):
        self._page = BasePage(driver)

    __loc_button_order = (By.XPATH, '//*[@data-component="hotel/new-rooms-table/summary/dont-worry"]')
    __loc_select_order = (By.XPATH, '//*[@class="hprt-reservation-cta"]')
    __loc_alert_order = (By.XPATH, '//*[@class="select_room_tooltip_alert_reminder shadow"]')

    def click_button_order(self):
        self._page.scroll_into_view(self.__loc_button_order)
        self._page.click_enter(self.__loc_button_order)

    def is_button_order_displayed(self):
        return self._page.is_displayed(self.__loc_button_order)

    def type_alert_is_displayed(self):
        return self._page.is_displayed(self.__loc_alert_order)
