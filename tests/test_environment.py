from pytest import mark

def test_env_qa(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://myqa-env.com'
    assert port == 80

@mark.skip
def test_env_dev(env):
    assert env == 'dev'
