# coding=utf-8
"""Grammarly works feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
import time


def get_shadow(browser, element):
    return browser.execute_script("return arguments[0].shadowRoot",
                                  element._element)


@scenario('features/grammarly_positive.feature',
          'Check if grammarly works well')
def test_grammarly_works(browser):
    pass


@when('User access to grammarly checker and type a incorrect word')
def checker_and_write_incorrect_word(browser):
    # activate grammarly
    browser.visit("https://demo.grammarly.com/?hideSignupPopup")
    browser.windows[0].is_current = True
    browser.windows.current.close_others()


@then('grammarly should notice about the error')
def grammarly_should_notice_about_the_error(browser):
    browser.visit("https://www.grammarly.com/grammar-check")
    browser.find_by_tag("textarea").first.type("im ok")
    mirror = browser.find_by_tag("grammarly-mirror").first
    shadow = get_shadow(browser, mirror)
    cancelOnboarding = 'div[data-grammarly-part="btnCancelOnboarding"]'
    no_thanks = shadow.find_element_by_css_selector(cancelOnboarding)
    no_thanks.click()
    extension = browser.find_by_tag("grammarly-extension").first
    time.sleep(10)
    other_shadow = get_shadow(browser, extension)
    gbutton_sel = "div[data-grammarly-part='gbutton']"
    button_check = other_shadow.find_element_by_css_selector(gbutton_sel)
    assert button_check.text == '1'
