import httpx
from ..config import API_URL

API_URL = API_URL


# @cached(cache)
async def fetch_currency_rates(base_currency: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_URL}{base_currency}")
        response.raise_for_status()  # Проверка на успешный ответ
        data = response.json()

        return data
