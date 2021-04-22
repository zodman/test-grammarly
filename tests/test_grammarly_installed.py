# coding=utf-8
"""Check if grammarly is installed feature tests."""
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('features/grammarly_installed.feature',
          'with a chrome browser with grammarly installed')
def test_grammarly_installed():
    pass


@given('a url like google.com')
def visit_website(browser):
    browser.visit("https://google.com")


@when('wait for the webpage is fully loaded')
def check_website_loaded(browser):
    # force to open only google.com
    browser.windows[0].is_current = True
    browser.windows.current.close_others()
    assert browser.is_element_present_by_name("q", wait_time=5)


@then('check if the body property contains data-gr-ext-installed property')
def check_installed_on_body(browser, request):
    """
        Check if grammarly is installed or not.

    """
    assert browser.is_element_present_by_tag("body")
    body_tag = browser.find_by_tag("body").first
    if request.config.getoption("--grammarly-ext"):
        assert_msg = "grammarly Ext not installed"
        assert body_tag["data-gr-ext-installed"] == "", assert_msg
    else:
        print(">>>>>>> grammarly not installed")
        assert body_tag["data-gr-ext-installed"] is None
