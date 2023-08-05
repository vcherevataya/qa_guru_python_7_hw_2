import pytest
from selene import browser


@pytest.fixture()
def browser_window_size():
    browser.config.window_width = 1440
    browser.config.window_height = 1050

    yield
    browser.quit()
