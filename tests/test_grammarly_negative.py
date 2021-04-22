# coding=utf-8
"""Grammarly not working like expect feature tests."""

from pytest_bdd import given, scenario, then, when
from .base import activate, type_on_grammarly, grammarly_check


@scenario('features/grammarly_negative.feature',
          'Write a phrase without comas')
def test_check_grammarly_puntaction(browser):
    pass


@given("grammarly activated")
def grammarly_activated(browser):
    activate(browser)


@when('user type a phrase without comas')
def the_browser_can_not_connect_to_the_websocket(browser):
    msg = "Thanks for tutoring me No biggie Sally"
    type_on_grammarly(browser, msg, 10)


@then('grammarly not showing error')
def grammarly_show_an_error(browser):
    assert grammarly_check(browser).strip() == ''
