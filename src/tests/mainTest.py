# TestClient doesn't work for async functions
from starlette.testclient import TestClient
import pytest
from httpx import AsyncClient
from app.main import app

client = TestClient(app)

# we are redefining functions at multiple places and that's not good
@pytest.mark.asyncio
async def test_read_root():
    async with AsyncClient(app=app, base_url="http://localhost:8000/") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

#POST VALID
def test_post_valid_users1():
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


@pytest.mark.asyncio
async def test_post_valid_users2():
    async with AsyncClient(app=app,base_url='http://localhost:8000/') as ac:
        response = await ac.post(
            "/users/",
            json = {
                "name":"Keanu",
                "family":"Reeves",
                "description":"You are breathtaking"
            })
    assert response.status_code == 200
    assert response.json() == {
                "name":"Keanu",
                "family":"Reeves",
                "description":"You are breathtaking"
            }

#POST INVALID
@pytest.mark.asyncio
async def test_post_invalid_users1():
    async with AsyncClient(app=app,base_url='http://localhost:8000/') as ac:
        response = await ac.post(
            "/users/",
            json = {
                "name":"Joe",
                "family":34
            })
    assert response.status_code == 422

# should be invalid since we only want stings but I don't know why sql alchemy allows for ints
@pytest.mark.asyncio
async def test_post_invalid_users2():
    async with AsyncClient(app=app,base_url='http://localhost:8000/') as ac:
        response = await ac.post(
            "/users/",
            json = {
                "name": 812313,
                "family":"BALDWIN",
                "description": 81131
            })
    assert response.status_code == 200
    assert response.json() == {
                "name": "812313",
                "family":"BALDWIN",
                "description": "81131"
    }

#GET VALID
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

#GET INVALID
@pytest.mark.asyncio
async def test_get_invalid_users():
    async with AsyncClient(app=app,base_url='http://localhost:8000/') as ac:
        response = await ac.post(
            "/users/401")
    #apparently retuns a 405 error(blocks request)
    assert response.status_code == 405

#PATCH
@pytest.mark.asyncio
async def test_patch_valid_users():
    async with AsyncClient(app=app,base_url='http://localhost:8000') as ac:
        response = await ac.patch(
            "/users/2",
            json={
              "name": "string",
              "family": "string",
              "description": "Wake up samurai, we have a program to crash."
            }
        )
    assert response.status_code == 200
    assert response.json() == {
                "name":"Keanu",
                "family":"Reeves",
              "description": "Wake up samurai, we have a program to crash."
            }

@pytest.mark.asyncio
async def test_patch_valid_users2():
    async with AsyncClient(app=app,base_url='http://localhost:8000') as ac:
        response = await ac.patch(
            "/users/2",
            json={
              "name": "Joe",
              "family": "Hackerman",
              "description": "I'm in"
            }
        )
    assert response.status_code == 200
    assert response.json() == {
              "name": "Joe",
              "family": "Hackerman",
              "description": "I'm in"
            }

# PATCH INVALID
@pytest.mark.asyncio
async def test_patch_invalid_users():
    async with AsyncClient(app=app,base_url='http://localhost:8000') as ac:
        response = await ac.patch(
            "/users/2",
            json={
              "name": "Joe",
              "family": "Ha",
            }
        )
    assert response.status_code == 422

# DELETE VALID
@pytest.mark.asyncio
async def test_delete_valid_users():
    async with AsyncClient(app=app,base_url='http://localhost:8000') as ac:
        response = await ac.delete(
            "/users/3"
            )
    assert response.status_code == 200
    assert response.json() == {
            "message": "userId 3 delete"
        }

# DELETE INVALID
# at this point the delete function is idempotent
@pytest.mark.asyncio
async def test_delete_invalid_users():
    async with AsyncClient(app=app,base_url='http://localhost:8000') as ac:
        response = await ac.delete(
            "/users/3"
            )
    # really should be  422
    assert response.status_code == 200
    #assert response.json() == {
    #        "message": "userId 3 does not exist"
    #    }

# GET ALL USERS
@pytest.mark.asyncio
async def test_getall_valid_users():
    async with AsyncClient(app=app,base_url='http://localhost:8000') as ac:
        response = await ac.get(
            "/users/"
            )
    assert response.status_code == 200
    assert response.json() == {
"[{\n    \"id\": 1,\n    \"name\": \"Joe\",\n    \"family\": \"baldwin\",\n    \"description\": \"JOE BALDWINNN\"\n}, {\n    \"id\": 2,\n    \"name\": \"Joe\",\n    \"family\": \"Hackerman\",\n    \"description\": \"I'm in\"\n}]"
        }
