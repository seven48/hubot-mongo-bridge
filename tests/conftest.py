import pytest

from src.utils import make_app


@pytest.fixture
def client(loop, aiohttp_client):
    return loop.run_until_complete(aiohttp_client(make_app()))
