import time


def get_shadow(browser, element):
    args = "return arguments[0].shadowRoot", element._element
    return browser.execute_script(*args)


def wait_time(wait_time, run):
    end_time = time.time()+wait_time
    while time.time() < end_time:
        if run():
            return True
    return False
