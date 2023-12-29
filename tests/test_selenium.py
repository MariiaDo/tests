import time
import allure
import pytest
from page_objects.header_page import HeaderPage
from page_objects.main_page import MainPage
from page_objects.start_page import StartPage


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test positive search header")
@pytest.mark.smoke
@pytest.mark.positive
def test_positive_search_header(create_driver, fake_city):
    header_page = HeaderPage(create_driver)
    header_page.click_banner()
    header_page.set_input_destination(fake_city)
    header_page.set_calendar_date()
    header_page.click_submit_button()
    main_page = MainPage(create_driver)
    assert main_page.is_label_displayed(), 'Label failed, label not displayed'


@allure.title("Test negative search header")
@pytest.mark.negative
def test_negative_search_header(create_driver):
    header_page = HeaderPage(create_driver)
    header_page.click_banner()
    header_page.set_calendar_date()
    header_page.click_submit_button()
    assert header_page.type_alert_is_displayed, 'Type alert is not displayed'


@allure.title("Test recently searched start page")
def test_recently_searched_start_page(create_driver, fake_city):
    header_page = HeaderPage(create_driver)
    start_page = StartPage(create_driver)
    test_positive_search_header(create_driver, fake_city)
    header_page.click_main_logo()
    assert start_page.recently_searched_box_is_present(), 'recently_searched, blok not displayed'
    # driver.execute_script("window.history.go(-1)")


@allure.title("Test popular direction start page")
def test_popular_direction_start_page(create_driver):
    start_page = StartPage(create_driver)
    main_page = start_page.click_popular_direction_box()
    assert main_page.is_label_displayed(), 'popular_direction failed, label not displayed'


@allure.title("Test change language header")
@pytest.mark.positive
def test_change_language_header(create_driver):
    header_page = HeaderPage(create_driver)
    header_page.click_banner()
    header_page.click_change_language()
    lang = header_page.get_language()
    assert lang == "Search", "change_language failed. Name of button does not fit"


@allure.title("Test change currency header")
@pytest.mark.positive
def test_change_currency_header(create_driver):
    header_page = HeaderPage(create_driver)
    header_page.click_banner()
    header_page.click_change_currency()
    currency = header_page.get_currency()
    assert currency == "EUR", "change_currency failed. Currency does not fit"


@allure.title("Test sort main page")
@pytest.mark.smoke
def test_sort_main_page(create_driver, fake_city):
    main_page = MainPage(create_driver)
    test_positive_search_header(create_driver, fake_city)
    main_page.click_sort_by()
    score_top = main_page.product_get_score(1)
    score_next = main_page.product_get_score(5)
    assert score_top >= score_next, "score is not sorted correctly"


@allure.title("Test filter main page")
def test_filter_main_page(create_driver, fake_city):
    main_page = MainPage(create_driver)
    test_positive_search_header(create_driver, fake_city)
    main_page.check_box_filter_by_score()
    score_top = main_page.product_get_score(1)
    score_next = main_page.product_get_score(5)
    assert float(score_top) >= 9 and float(score_next) >= 9, "Score filter failed, filter_main_page"


@allure.title("Test check box filter by mealplan main page")
def test_check_box_filter_by_mealplan_main_page(create_driver, fake_city):
    main_page = MainPage(create_driver)
    header_page = HeaderPage(create_driver)
    header_page.click_change_language()
    test_positive_search_header(create_driver, fake_city)
    main_page.check_box_filter_by_mealplan()
    meal_plan_top = main_page.product_get_meal_item(1)
    meal_plan_next = main_page.product_get_meal_item(5)
    assert meal_plan_top == "Breakfast included" and meal_plan_next == "Breakfast included", "filter_by_mealplan failed, label is not present"

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test placement choice from main page")
@pytest.mark.smoke
def test_placement_choice_from_main_page(create_driver, fake_city):
    main_page = MainPage(create_driver)
    test_positive_search_header(create_driver, fake_city)
    placement_page = main_page.click_placement()
    assert placement_page.is_button_order_displayed, "placement_choice_from_main_page dose not work. Button_order_displayed is not displayed"
