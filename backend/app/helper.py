from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse


helper_router = APIRouter()


#Root
@helper_router.get(
    "/",
    status_code=status.HTTP_200_OK,
    tags=["Root"],
    response_description="Get Doc Info",
)
async def root_directory():
    """
    - **Здесь была рука юного падавана Гаррика :)**
    """
    return {
        "msg": "Hello, there is Garry's API. Please check /docs for documentation <3"
    }
