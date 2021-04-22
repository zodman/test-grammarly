# coding=utf-8
"""Grammarly not working like expect feature tests."""

from pytest_bdd import given, scenario, then, when
from .utils import get_shadow, activate
import time


@scenario('features/grammarly_negative.feature',
          'Write a phrase without comas')
def test_check_grammarly_puntaction(browser):
    pass


@given("grammarly activated")
def grammarly_activated(browser):
    activate(browser)
    browser.find_by_tag("textarea").first.type("hola")
    mirror = browser.find_by_tag("grammarly-mirror").first
    shadow = get_shadow(browser, mirror)
    cancelOnboarding = 'div[data-grammarly-part="btnCancelOnboarding"]'
    no_thanks = shadow.find_element_by_css_selector(cancelOnboarding)
    no_thanks.click()


@when('user type a phrase without comas')
def the_browser_can_not_connect_to_the_websocket(browser):
    browser.visit("https://www.grammarly.com/grammar-check")
    element = browser.find_by_tag("textarea").first
    element.type("Thanks for tutoring me No biggie Sally")
    time.sleep(10)  # time to grammarly api response
    extension = browser.find_by_tag("grammarly-extension").first
    other_shadow = get_shadow(browser, extension)
    gbutton_sel = "div[data-grammarly-part='gbutton']"
    button_check = other_shadow.find_element_by_css_selector(gbutton_sel)
    assert button_check.text == ' '


@then('grammarly not showing error')
def grammarly_show_an_error(browser):
    import pdb
    pdb.set_trace()
