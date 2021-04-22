# coding=utf-8
"""Grammarly works feature tests."""
from pytest_bdd import given, scenario, then, when
from .base import type_on_grammarly, grammarly_check, activate


@scenario('features/grammarly_positive.feature',
          'Check if grammarly works well')
def test_grammarly_works(browser):
    pass


@given("grammarly activated")
def grammarly_activated(browser):
    activate(browser)


@when('User access to grammarly checker and type a incorrect word')
def checker_and_write_incorrect_word(browser):
    type_on_grammarly(browser, 'im ok', 10)


@then('grammarly should notice about the mistypo')
def grammarly_should_notice_about_the_error(browser):
    assert grammarly_check(browser).strip() == '1'
