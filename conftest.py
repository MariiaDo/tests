import json

import pytest
import random

from constants import ROOT_PATH
from utilities.config_reader import AppConfig
from utilities.driver_factory import DriverFactory
from utilities.json_to_class import DictToClass


@pytest.fixture
def create_driver(env):
    driver = DriverFactory(env.browser_id).get_driver()
    driver.maximize_window()
    driver.get(env.url)
    yield driver
    driver.quit()


@pytest.fixture
def env():
    with open(f"{ROOT_PATH}/configs/conf.json") as f:
        conf_dict = json.loads(f.read())
        return DictToClass(**conf_dict)


@pytest.fixture
def fake():
    city = random.choice(['London', 'Berlin', 'Paris', 'Oslo'])
    return city
