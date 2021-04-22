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
