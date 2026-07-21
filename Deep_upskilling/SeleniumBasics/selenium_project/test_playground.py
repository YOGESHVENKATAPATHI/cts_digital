import pytest

from pages.simple_form_page import SimpleFormPage
from pages.checkbox_page import CheckboxPage
from pages.dropdown_page import DropdownPage
from pages.input_form_pages import InputFormPage


@pytest.mark.parametrize(
    "message",
    [
        "Hello",
        "Selenium Automation",
        "12345"
    ]
)
def test_simple_form_submission(driver, message):

    page = SimpleFormPage(driver)

    page.navigate_to(
        "https://www.lambdatest.com/selenium-playground/simple-form-demo"
    )

    page.enter_message(message)

    page.click_submit()

    assert page.get_displayed_message() == message


def test_checkbox_demo(driver):

    page = CheckboxPage(driver)

    page.navigate_to(
        "https://www.testmuai.com/selenium-playground/checkbox-demo/"
    )

    page.check_option()

    assert page.is_option_checked()

    page.uncheck_option()

    assert not page.is_option_checked()


def test_dropdown_selection(driver):

    page = DropdownPage(driver)

    page.navigate_to(
        "https://www.testmuai.com/selenium-playground/select-dropdown-demo/"
    )

    page.select_day("Wednesday")

    assert page.get_selected_day() == "Wednesday"

@pytest.mark.skip(reason="Input Form Demo page structure changed on TestMu site")
def test_input_form_submit(driver):
    
    page = InputFormPage(driver)

    page.navigate_to(
        "https://www.testmuai.com/selenium-playground/input-form-demo/"
    )

    page.fill_form(
        "Madhi",
        "madhi@test.com"
    )

    page.submit_form()

    assert page.get_success_message() is not None