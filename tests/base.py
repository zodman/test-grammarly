from selenium.common.exceptions import NoSuchElementException
import time
from .utils import wait_time, get_shadow


def type_on_grammarly(browser, message, wait_time):
    browser.visit("https://www.grammarly.com/grammar-check")
    element = browser.find_by_tag("textarea").first
    element.type(message)
    time.sleep(wait_time)  # time to grammarly api response


def grammarly_check(browser):
    extension = browser.find_by_tag("grammarly-extension").first
    other_shadow = get_shadow(browser, extension)
    gbutton_sel = "div[data-grammarly-part='gbutton']"
    button_check = other_shadow.find_element_by_css_selector(gbutton_sel)
    return button_check.text


def activate(browser):
    browser.visit("https://demo.grammarly.com/?hideSignupPopup")
    wait_time(5, lambda *args: len(browser.windows) > 1)
    browser.windows[0].is_current = True
    browser.windows.current.close_others()
    browser.visit("https://www.grammarly.com/grammar-check")
    browser.find_by_tag("textarea").first.type("hola")
    mirror = browser.find_by_tag("grammarly-mirror").first
    shadow = get_shadow(browser, mirror)
    cancelOnboarding = 'div[data-grammarly-part="btnCancelOnboarding"]'
    try:
        no_thanks = shadow.find_element_by_css_selector(cancelOnboarding)
        no_thanks.click()
    except NoSuchElementException:
        pass
