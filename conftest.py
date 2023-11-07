import json
import random
import pytest
from faker import Faker
from api_collections.notes_api import NotesApi
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
