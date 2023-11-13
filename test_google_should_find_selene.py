import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture
def open_browser():
    browser.config.window_width = 1280
    browser.config.window_height = 720

    yield
    browser.quit()


def test_search_selene(open_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_search_another(open_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('dsdsdsdsdsdsdsfldgmkgfkgnfkgfgeokgeorgeorpgjrgr').press_enter()
    browser.element('[class="card-section"]').should(have.text('ничего не найдено'))
