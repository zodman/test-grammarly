# coding=utf-8
"""Grammarly works feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('features/grammarly_positive.feature', 'Check if grammarly works well')
def test_check_if_grammarly_works_well():
    """Check if grammarly works well."""


@when('User access to grammarly checker and type a incorrect word')
def user_access_to_grammarly_checker_and_type_a_incorrect_word():
    """User access to grammarly checker and type a incorrect word."""
    raise NotImplementedError


@then('grammarly should notice about the error')
def grammarly_should_notice_about_the_error():
    """grammarly should notice about the error."""
    raise NotImplementedError


@then('show the correct word')
def show_the_correct_word():
    """show the correct word."""
    raise NotImplementedError

