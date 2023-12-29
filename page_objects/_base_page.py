from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.deco import auto_step


@auto_step
class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_element_is_visible(self, locator: tuple, timeout=3) -> WebElement:
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    def wait_element_is_clickable(self, locator: tuple, timeout=3) -> WebElement:
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))

    def wait_element_is_presence(self, locator: tuple, timeout=3) -> WebElement:
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))

    def send_keys(self, locator: tuple, value):
        el = self.wait_element_is_visible(locator)
        el.send_keys(value)

    def click(self, locator: tuple):
        el = self.wait_element_is_clickable(locator)
        el.click()

    def click_enter(self, locator: tuple):
        el = self.wait_element_is_clickable(locator)
        el.send_keys(Keys.ENTER)


    def is_displayed(self, locator: tuple):
        el = self.wait_element_is_visible(locator)
        return el.is_displayed()

    def scroll_into_view(self, locator: tuple):
        el = self.wait_element_is_presence(locator)
        self.driver.execute_script('arguments[0].scrollIntoView()', el)

    def scroll_to_element(self, locator: tuple):
        el = self.wait_element_is_presence(locator, 5)
        ActionChains(self.driver).scroll_to_element(el).perform()


    def get_text(self, locator: tuple, index=1):
        self.wait_element_is_presence(locator)
        els = self.driver.find_elements(*locator)
        if len(els) < index-1:
            raise NoSuchElementException(str(locator) + f'by index=({index})')
        return els[index-1].text


    def click_by_js(self, locator: tuple):
        el = self.wait_element_is_presence(locator)
        self.driver.execute_script('arguments[0].click()', el)



