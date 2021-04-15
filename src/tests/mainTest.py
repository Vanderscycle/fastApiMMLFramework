# TestClient doesn't work for async functions
from starlette.testclient import TestClient
import pytest
from httpx import AsyncClient
from app.main import app

client = TestClient(app)

@pytest.mark.asyncio
async def test_read_root():
    async with AsyncClient(app=app, base_url="http://localhost:8000/") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_post_users():
    response = client.post(
        "/users/",
        json = {
        "name":"Joe",
        "family":"baldwin",
        "description":"JOE BALDWINNN"
                }
    )
    assert response.status_code == 200
    assert response.json() == {
        "name":"Joe",
        "family":"baldwin",
        "description":"JOE BALDWINNN"
    }


def test_get_users():
    response = client.get(
        "/users/1"
    )
    assert response.status_code == 200
    assert response.json() == {
        "name":"Joe",
        "family":"baldwin",
        "description":"JOE BALDWINNN"
    }
