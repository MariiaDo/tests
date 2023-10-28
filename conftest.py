import pytest
import random
from utilities.config_reader import AppConfig
from utilities.driver_factory import DriverFactory


@pytest.fixture
def create_driver():
    driver = DriverFactory(AppConfig.browser_id).get_driver()
    driver.maximize_window()
    driver.get(AppConfig.url)
    yield driver
    driver.quit()


@pytest.fixture
def fake():
    city = random.choice(['London', 'Berlin', 'Paris', 'Oslo'])
    return city
