# coding=utf-8
"""Grammarly works feature tests."""
import time
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from .utils import get_shadow, wait_time


@scenario('features/grammarly_positive.feature',
          'Check if grammarly works well')
def test_grammarly_works(browser):
    pass



@when('User access to grammarly checker and type a incorrect word')
def checker_and_write_incorrect_word(browser):
    # activate grammarly
    browser.visit("https://demo.grammarly.com/?hideSignupPopup")


@then('grammarly should notice about the mistypo')
def grammarly_should_notice_about_the_error(browser):
    browser.visit("https://www.grammarly.com/grammar-check")
    browser.find_by_tag("textarea").first.type("im ok")
    time.sleep(10)  # wait to grammarly extension respond
    extension = browser.find_by_tag("grammarly-extension").first
    other_shadow = get_shadow(browser, extension)
    gbutton_sel = "div[data-grammarly-part='gbutton']"
    button_check = other_shadow.find_element_by_css_selector(gbutton_sel)
    assert button_check.text == '1'
