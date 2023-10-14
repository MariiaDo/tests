import pytest
from unit_test.car import Car


@pytest.fixture
def get_new_car():
    new_car = Car("BMW", "X5", 10)
    yield new_car


@pytest.fixture
def get_new_car_params():
    def __inner_new_car(brand, model):
        new_car = Car(brand, model)
        return new_car

    return __inner_new_car
