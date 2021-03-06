from app import schemas
from jose import jwt
from app.config import settings


def test_create_user(client):
    res = client.post(
        "/users/", json={"email": "someone@gmail.com", "password": "hihello"})
    print(res.json)
    assert res.status_code == 201


def test_login_user(client, test_user):
    res = client.post(
        "/login", data={"username": test_user['email'], "password": test_user['password']})
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token,
                         settings.secret_key, algorithms=settings.algorithm)
    id = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == 'bearer'

    assert res.status_code == 200
