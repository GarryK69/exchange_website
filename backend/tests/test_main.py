import pytest
from fastapi.testclient import TestClient
from app.create_app import create_app
from faker import Faker
import httpx

# Создаем экземпляр приложения FastAPI
app = create_app()

# Создаем экземпляр Faker для генерации случайных данных
fake = Faker()

# Фикстура для синхронного клиента
@pytest.fixture
def client():
    return TestClient(app)

# Фикстура для асинхронного клиента
@pytest.fixture
async def async_client():
    async with httpx.AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

async def test_get_currency_rates(client):
    response = client.get("/currency?base_currency=USD")
    assert response.status_code == 200
    data = response.json()
    assert "USD" in data

async def test_convert_currency(client):
    response = client.get("/convert?from_currency=USD&to_currency=EUR&amount=10")
    assert response.status_code == 200
    data = response.json()
    assert data["from_currency"] == "USD"
    assert data["to_currency"] == "EUR"
    assert data["amount"] == 10
    assert "converted_amount" in data

def test_create_user(client):
    name = fake.name()
    email = fake.email()

    response = client.post("/users/", json={"name": name, "email": email})
    assert response.status_code == 201
    response_json = response.json()
    assert response_json["name"] == name
    assert response_json["email"] == email

def test_read_user(client):
    name = fake.name()
    email = fake.email()

    response = client.post("/users/", json={"name": name, "email": email})
    user_id = response.json()["id"]

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["name"] == name
    assert response_json["email"] == email
