import time


def get_shadow(browser, element):
    return browser.execute_script("return arguments[0].shadowRoot",
                                  element._element)


def wait_time(wait_time, run):
    end_time = time.time()+wait_time
    while time.time() < end_time:
        if run():
            return True
    return False


def activate(browser):
    browser.visit("https://demo.grammarly.com/?hideSignupPopup")
    wait_time(5, lambda *args: len(browser.windows) > 1)
    browser.windows[0].is_current = True
    browser.windows.current.close_others()
    browser.visit("https://www.grammarly.com/grammar-check")

