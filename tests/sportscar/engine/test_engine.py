from pytest import mark


@mark.smoke
@mark.engine
def test_engine_as_expected():
    assert True

@mark.ui
def test_engine_web(chrome_browser):
    chrome_browser.get('https://engine.com.pk/')


