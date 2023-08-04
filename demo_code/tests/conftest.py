
from django.core.management import call_command
import pytest



@pytest.fixture(scope="session")
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command("loaddata", "seed_data.json")


@pytest.fixture(scope="session")
def mock_functions_env():
    os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = "true"


@pytest.fixture(scope="session")
def live_server_url(live_server):
    """Returns the url of the live server"""
    return live_server.url
