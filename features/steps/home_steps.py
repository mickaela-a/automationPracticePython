#from time import time
from behave import given, when
from utils.Driver import launch_browser
from features.page_objects.basePage import click_element_by_css_selector
from features.page_objects.home_page import FIRSTPRODUCT_LINK, HOME_URL


@given('the common user is on demoblaze page')
def navigate_to_demoblaze(context):
    launch_browser(context)
    context.driver.maximize_window()
    context.driver.get(HOME_URL)


@when('the user clicks on a product')
def click_on_a_product(context):
    click_element_by_css_selector(context, FIRSTPRODUCT_LINK)
