import httpx
from .config import API_URL

from typing import Dict
from fastapi import APIRouter, HTTPException, status

API_URL = API_URL

currency_router = APIRouter()

@currency_router.get(
    "/currency",
    response_model=Dict[str, float],
    status_code=status.HTTP_200_OK,
    tags=["currency"],
    response_description="Currency Successfully Retrieved",
)
async def get_currency_rates(base_currency: str = "USD"):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{API_URL}{base_currency}")
            response.raise_for_status()
            data = response.json()

        return data.get("rates", {})

    except httpx.HTTPStatusError as e:
        raise HTTPException(
            status_code=e.response.status_code, detail=f"HTTP error occurred: {e}"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {e}")
