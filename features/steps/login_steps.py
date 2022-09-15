import time
from features.page_objects.login_page import LOGIN_BOTON, LOGIN_BOTON_MENU, LOGIN_URL, LOGOUT_BOTON, VALID_USERNAME ,PASSWORD_FIELD, VALID_PASSWORD, USERNAME_FIELD
from utils.Driver import launch_browser
from behave import given, then, when
from features.page_objects.basePage import (click_element_by_css_selector, element_displayed,
                                            send_keys_by_css_selector)


@given('the user is on demoblaze page')
def navigate_to_demoblaze(context) :
    launch_browser(context, 'Chrome')
    context.driver.maximize_window()
    context.driver.get(LOGIN_URL)


@when('the user logs in with valid credentials')
def login_with_valid_credentials(context) :
    click_element_by_css_selector(context, LOGIN_BOTON_MENU)
    send_keys_by_css_selector(context, USERNAME_FIELD, VALID_USERNAME)
    send_keys_by_css_selector(context, PASSWORD_FIELD, VALID_PASSWORD)
    click_element_by_css_selector(context, LOGIN_BOTON)


@then('the user see the logout boton')
def validate_user_is_logged(context) :
    logout_boton_displayed = element_displayed(context, LOGOUT_BOTON)
    assert logout_boton_displayed == True
