from datetime import datetime
from typing import Annotated
import httpx
from fastapi import APIRouter, HTTPException, Query, status

from .utils.utilities import fetch_currency_rates

convertor_router = APIRouter()

@convertor_router.get(
    "/convert",
    status_code=status.HTTP_200_OK,
    tags=["conversion"],
    response_description="Conversion Successful",
)
async def convert_currency(
    from_currency: Annotated[
        str, Query(description="Currency to convert from", min_length=3, max_length=3)
    ],
    to_currency: Annotated[
        str, Query(description="Currency to convert to", min_length=3, max_length=3)
    ],
    amount: Annotated[
        float,
        Query(
            description="Amount to convert",
            alias="amount-to-convert",
            title="Conversion Amount",
            lt=1_000_000_000,
            gt=0,
        ),
    ],
):
    try:
        rates = await fetch_currency_rates(from_currency)

        if "rates" not in rates:
            raise HTTPException(status_code=500, detail="Rates data not available")

        rate = rates["rates"].get(to_currency)

        if rate is not None:
            converted_amount = amount * rate
            return {
                "from_currency": from_currency,
                "to_currency": to_currency,
                "amount": amount,
                "converted_amount": converted_amount,
                "convert_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
        else:
            raise HTTPException(status_code=404, detail="Conversion rate not found")

    except httpx.HTTPStatusError as e:
        raise HTTPException(
            status_code=e.response.status_code, detail=f"HTTP error occurred: {e}"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error converting currency: {e}")
