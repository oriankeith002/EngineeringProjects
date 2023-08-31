import pytest
from quart import Quart


@pytest.fixture
def app():
    yield Quart("test_app")


@pytest.fixture
async def test_client(app):
    yield app.test_client()


async def test_ws_works(test_client):
    async with test_client.websocket("/process") as test_ws:
        print(test_client)
        await test_ws.send("hello")
        result = await test_ws.receive()
        assert result == "hello"
