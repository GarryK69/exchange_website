from ..currency import currency_router
from ..convertor import convertor_router
from ..authorization import authorization_router
from ..users import user_router
from ..helper import helper_router

def include_routers(app):
    app.include_router(currency_router)
    app.include_router(convertor_router)
    app.include_router(authorization_router)
    app.include_router(user_router)
    app.include_router(helper_router)
