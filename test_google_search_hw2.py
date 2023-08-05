from selene import browser, be, have


def test_search_valid(browser_window_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_search_invalid(browser_window_size):
    browser.open('https://google.com')
    browser.element('[name=q]').should(be.blank).type(';lrmpfmvpvds;lmv;dvlm').press_enter()
    browser.element('[id="botstuff"]').should(have.text("По запросу ;lrmpfmvpvds;lmv;dvlm ничего не найдено."))
