import pytest
import random

PARAMS = {
    'argnames': 'brand, model',
    'argvalues': [['BMW', '5'], ('Mercedes', 's klasse'), ('Mazda', '3')],
    'ids': ['BMW', 'Mercedes', 'Mazda']
}


@pytest.mark.parametrize(**PARAMS)
@pytest.mark.positive
def test_start_engine_first_time(get_new_car_params, brand, model):
    my_car = get_new_car_params(brand, model)
    engine_info = my_car.start_engine()
    assert engine_info == "Engine started."


@pytest.mark.parametrize(**PARAMS)
@pytest.mark.negative
def test_start_engine_already_running(get_new_car_params, brand, model):
    my_car = get_new_car_params(brand, model)
    my_car.start_engine()
    engine_info = my_car.start_engine()
    assert engine_info == "Engine is already running."


@pytest.mark.parametrize(**PARAMS)
@pytest.mark.positive
def test_stop_engine_after_start(get_new_car_params, brand, model):
    my_car = get_new_car_params(brand, model)
    my_car.start_engine()
    engine_info = my_car.stop_engine()
    assert engine_info == "Engine stopped."


@pytest.mark.parametrize(**PARAMS)
@pytest.mark.negative
def test_stop_engine_without_start(get_new_car_params, brand, model):
    my_car = get_new_car_params(brand, model)
    engine_info = my_car.stop_engine()
    assert engine_info == "Engine is already off."


@pytest.mark.positive
def test_drive_positive(get_new_car):
    my_car = get_new_car
    start_miles_limit = my_car.miles_limit
    my_car.start_engine()
    miles_to_drive = random.randint(1, 10)
    drive_info = my_car.drive(miles_to_drive)
    final_miles_limit = my_car.miles_limit
    assert drive_info == f"Driving {miles_to_drive} miles."
    assert final_miles_limit == start_miles_limit - miles_to_drive


@pytest.mark.negative
def test_drive_without_engine_starting(get_new_car):
    my_car = get_new_car
    start_miles_limit = my_car.miles_limit
    miles_to_drive = random.randint(1, 10)
    drive_info = my_car.drive(miles_to_drive)
    final_miles_limit = my_car.miles_limit
    assert drive_info == "Cannot drive. Engine is off."
    assert final_miles_limit == start_miles_limit


@pytest.mark.negative
def test_drive_without_enough_miles(get_new_car):
    my_car = get_new_car
    start_miles_limit = my_car.miles_limit
    my_car.start_engine()
    miles_to_drive = random.randint(11, 100)
    drive_info = my_car.drive(miles_to_drive)
    final_miles_limit = my_car.miles_limit
    assert drive_info == "The miles limit has been exceeded"
    assert final_miles_limit == start_miles_limit
