import json
import random

import allure
import pytest
from faker import Faker
from api_collections.notes_api import NotesApi
from constants import ROOT_PATH
from db.sqlite_pack.goods_repo import GoodsRepo

from utilities.driver_factory import DriverFactory
from utilities.json_to_class import DictToClass


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture
def create_driver(env, request):
    driver = DriverFactory(env.browser_id).get_driver()
    driver.maximize_window()
    driver.get(env.url)
    yield driver
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(),
                      name='Fail_screenshot',
                      attachment_type=allure.attachment_type.PNG)
    driver.quit()


@pytest.fixture(scope='session')
def env():
    with open(f"{ROOT_PATH}/configs/conf.json") as f:
        conf_dict = json.loads(f.read())
        return DictToClass(**conf_dict)


@pytest.fixture
def fake_city():
    city = random.choice(['London', 'Berlin', 'Paris', 'Oslo'])
    return city


@pytest.fixture()
def get_fake_note_payload(fake):
    return {
        "title": fake.sentence(5),
        "description": fake.sentence(15),
        "category": random.choice(['Home', 'Work', 'Personal'])
    }


@pytest.fixture()
def put_fake_note_payload(fake, get_new_note_id):
    return {
        "id": get_new_note_id,
        "title": fake.sentence(5),
        "description": fake.sentence(15),
        "completed": random.choice(['false', 'true']),
        "category": random.choice(['Home', 'Work', 'Personal'])
    }

@pytest.fixture()
def patch_fake_completed_payload(fake, get_new_note_id):
    return {
        "id": get_new_note_id,
        "completed": random.choice(['false', 'true'])
    }

@pytest.fixture()
def get_new_note_id(get_fake_note_payload):
    resp = NotesApi().post_new_note(note_data=get_fake_note_payload)
    return resp.json().get('data')['id']


@pytest.fixture
def fake():
    fake = Faker()
    return fake


@pytest.fixture(scope='module')
def good_repo(env):
    return GoodsRepo(f'{ROOT_PATH}{env.db_param["path"]}')



@pytest.fixture()
def fake_good(fake):
    data = {
        "artikul": fake.pyint(1000, 1000000),
        "name_of_product": random.choice(['skirt', 'trousers', 'skirt', 'dress', 't-shirt']),
        "brand": random.choice(['zara', 'H&M', 'Mango', 'GAP', 'Nike']),
        "size": random.choice(['xs', 's', 'm', 'l', 'xl']),
        "quantity": fake.pyint(10, 500),
        "purchase_amount": float(fake.pyint(10, 50)),
        "sales_amount": float(fake.pyint(50, 100))
    }
    return data