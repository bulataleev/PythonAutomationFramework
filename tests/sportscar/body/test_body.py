from pytest import mark

@mark.body
class BodyTests:
    
    @mark.smoke
    def test_body_as_expected(self):
        assert True

    @mark.other
    def test_other_test_name(self):
        assert True

    @mark.ui
    def test_navigate_to_page(self, chrome_browser):
        browser = chrome_browser.get('https://www.cars.com/')
        assert True