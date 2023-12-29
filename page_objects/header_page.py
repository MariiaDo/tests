import datetime
import time

from selenium.webdriver.common.by import By
from page_objects._base_page import BasePage
from page_objects.main_page import MainPage
from page_objects.start_page import StartPage
from utilities.deco import auto_step


@auto_step
class HeaderPage():
    def __init__(self, driver):
        self._page = BasePage(driver)

    __loc_banner = (By.ID, 'onetrust-accept-btn-handler')

    __loc_main_logo = (By.XPATH, '//a[@data-testid="header-booking-logo"]')
    __loc_submit_button = (By.XPATH, '//button[@type="submit"]')
    __loc_language_choice = (By.XPATH, '//button[@data-testid="header-language-picker-trigger"]')
    __loc_language_eng = (By.XPATH, '//span[contains(text(),"English (US)")]/ancestor::button')
    __loc_currency_choice = (By.XPATH, '//button[@data-testid="header-currency-picker-trigger"]')
    __loc_currency_euro = (By.XPATH, '//div[contains(text(),"EUR")]/ancestor::button')
    __loc_input_destination = (By.XPATH, '//input[@name="ss"]')

    __loc_calendar_date_start = (By.XPATH, '//button[@data-testid="date-display-field-start"]')
    __loc_calendar_date = (
    By.XPATH, '//*[@id="calendar-searchboxdatepicker"]/div/div[1]/div/div[2]/table/tbody/tr[2]/td[7]/span')
    __loc_calendar_date_next = (
    By.XPATH, '//*[@id="calendar-searchboxdatepicker"]/div/div[1]/div/div[2]/table/tbody/tr[3]/td[7]/span')

    __loc_type_alert = (By.XPATH, '//*[@id="b2searchresultsPage"]/div[4]/div/div/div/form/div[1]/div[1]/div/div[2]')

    def click_banner(self):
        self._page.click(self.__loc_banner)

    def click_main_logo(self):
        self._page.click(self.__loc_main_logo)
        return StartPage(self._page.driver)

    def click_change_language(self):
        self._page.click(self.__loc_language_choice)
        self._page.click(self.__loc_language_eng)

    def click_change_currency(self):
        self._page.click(self.__loc_currency_choice)
        self._page.click(self.__loc_currency_euro)

    def set_input_destination(self, value):
        self._page.send_keys(self.__loc_input_destination, value)

    def set_calendar_date(self):
        self._page.click_by_js(self.__loc_calendar_date_start)
        self._page.click_by_js(self.__loc_calendar_date)
        self._page.click_by_js(self.__loc_calendar_date_next)

    def click_submit_button(self):
        self._page.click_by_js(self.__loc_submit_button)
        return MainPage(self._page.driver)

    def type_alert_is_displayed(self):
        return self._page.is_displayed(self.__loc_type_alert)

    def click_present_date(self):
        self._page.click(self.__loc_calendar_date)

    def get_language(self):
        _by, _loc = self.__loc_submit_button
        self._page.scroll_into_view((_by, _loc))
        language = self._page.get_text(self.__loc_submit_button)
        return language

    def get_currency(self):
        _by, _loc = self.__loc_currency_choice
        self._page.scroll_into_view((_by, _loc))
        currency = self._page.get_text(self.__loc_currency_choice)
        return currency
