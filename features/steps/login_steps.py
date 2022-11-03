from features.page_objects.login_page import INVALID_PASSWORD, LOGIN_BOTON, LOGIN_BOTON_MENU, LOGIN_URL, LOGOUT_BOTON, VALID_USERNAME, PASSWORD_FIELD, VALID_PASSWORD, USERNAME_FIELD
from utils.Driver import launch_browser
import time
from behave import given, then, when
from features.page_objects.basePage import (click_element_by_css_selector, element_displayed,
                                            send_keys_by_css_selector, wait_until_element_displayed)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('the user is on demoblaze page')
def navigate_to_demoblaze(context):
    launch_browser(context)
    context.driver.maximize_window()
    context.driver.get(LOGIN_URL)


@when('the user logs in with valid credentials')
def login_with_valid_credentials(context):
    click_element_by_css_selector(context, LOGIN_BOTON_MENU)
    send_keys_by_css_selector(context, USERNAME_FIELD, VALID_USERNAME)
    send_keys_by_css_selector(context, PASSWORD_FIELD, VALID_PASSWORD)
    click_element_by_css_selector(context, LOGIN_BOTON)


@when('the user tries to login with invalid credentials')
def login_with_invalid_credentials(context):
    click_element_by_css_selector(context, LOGIN_BOTON_MENU)
    send_keys_by_css_selector(context, USERNAME_FIELD, VALID_USERNAME)
    send_keys_by_css_selector(context, PASSWORD_FIELD, INVALID_PASSWORD)
    click_element_by_css_selector(context, LOGIN_BOTON)


@then('the user see the logout boton')
def validate_user_is_logged(context):
#    time.sleep(10)
    wait_until_element_displayed(context, LOGOUT_BOTON)
    logout_boton_displayed = element_displayed(context, LOGOUT_BOTON)
    assert logout_boton_displayed == True


@then('the page shows an incorrect password message')
def show_an_incorrect_password_message(context):
    alert = WebDriverWait(context.driver, 5).until(EC.alert_is_present())
    alert_text = alert.text
    assert alert_text == 'Wrong password.'
    alert.accept()
