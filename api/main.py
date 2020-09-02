import os
import logging
from aiohttp import web
from tortoise import Tortoise
from bdd.models import make_easter_eggs
from handlers import (
    register,
    authentificate,
    meal,
    bracelet,
    get_consumption,
    set_consumption,
    validate_user,
    reset_password_page,
    reset_password,
    send_mail_to_reset_password,
    reset_user_data
)


async def init_api():
    api = web.Application()
    logging.basicConfig(format="LOGGING:: %(message)s", level=logging.DEBUG)
    await Tortoise.init(
        db_url="sqlite://db.sqlite3", modules={"models": ["bdd.models"]}
    )
    await Tortoise.generate_schemas()
    await make_easter_eggs()
    api.add_routes([web.post("/api/register", register)])
    api.add_routes([web.post("/api/authentificate", authentificate)])
    api.add_routes([web.get("/api/meal/suggestion", meal.suggestion)])
    api.add_routes([web.get("/api/bracelet/data", bracelet.data)])
    api.add_routes([web.get("/api/consumption", get_consumption)])
    api.add_routes([web.post("/api/consumption", set_consumption)])
    api.add_routes([web.get("/api/user/validate", validate_user)])
    api.add_routes([web.get("/reset/password", reset_password_page)])
    api.add_routes([web.post("/api/user/reset/password", reset_password)])
    api.add_routes([web.post("/api/user/reset/password/mailing", send_mail_to_reset_password)])
    api.add_routes([web.post("/api/user/reset/data", reset_user_data)])
    
    return api

if __name__ == "__main__":
    web.run_app(init_api())
