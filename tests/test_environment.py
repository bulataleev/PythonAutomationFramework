def test_env_qa(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://myqa-env1.com'
    assert port == 80

def test_env_dev(env):
    assert env == 'dev'
