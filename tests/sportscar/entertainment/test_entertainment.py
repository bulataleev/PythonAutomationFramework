from pytest import mark

@mark.entertainment
class EntertainmentTests:

    @mark.ui
    def test_navigate_to_page(self, chrome_browser):
        chrome_browser.get('https://www.ozon.ru/')
        assert True

