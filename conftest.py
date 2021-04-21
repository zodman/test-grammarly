import pytest
import os
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--run-local", action="store_true", help="run on local")
    parser.addoption("--grammarly-ext", help="grammarly extension located")


@pytest.fixture(scope="session")
def splinter_driver_kwargs(request, splinter_webdriver):
    kwargs = {}
    if request.config.getoption("--run-local"):
        kwargs.update({'port': 9515})

    ext_path = request.config.getoption("--grammarly-ext")
    chrome_options = webdriver.ChromeOptions()
    if ext_path:
        chrome_options.add_extension(ext_path)
    if splinter_webdriver == "remote":
        kwargs.update({'browser': 'chrome'})
    kwargs.update({'options': chrome_options})
    return kwargs
