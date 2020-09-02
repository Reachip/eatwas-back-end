import logging
import uuid
import os
from tortoise.exceptions import DoesNotExist
from webargs import fields
from webargs.aiohttpparser import use_args
from aiohttp import web
import aiofiles

from utils.response import success, fail
from utils.mail import send_reset_password_link
from utils.password import get_hashed_password_and_salt
from utils.response import success
from bdd.models import User

send_mail_to_reset_password = {
    "email": fields.Email(required=True), 
    "username": fields.Str(required=True)
}

@use_args(send_mail_to_reset_password)
async def send_mail_to_reset_password(req, args):
    try:
        user = await User.get(username=args["username"])

        if not args["email"] == user.email:
            raise Exception()
 

        link = f"http://192.168.10.105:8080/reset/password?uuid={user.uuid}"
        await send_reset_password_link(link, args["email"])
        
        return success(message="Mail envoyé à l'utilisateur concerné avec succès")

    except Exception as why:
        logging.debug(why)
        return fail(status_code=401, message=f"Impossible d'envoyer un mail à l'utilisateur concerné : Identifiants invalides.")

reset_password = {"uuid": fields.UUID(required=True), "password": fields.Str(required=True)}

@use_args(reset_password)
async def reset_password(req, args):
    user = await User.get(uuid=args["uuid"])
    hashed_password, salt = await get_hashed_password_and_salt(args["password"])
    user.hashed_password = hashed_password
    user.salt = salt
    await user.save()
    user = await User.get(hashed_password=hashed_password)
    user.uuid = str(uuid.uuid4())
    await user.save()
    return success(message=None)


reset_password_page = {"uuid": fields.UUID(required=True)}

@use_args(reset_password_page)
async def reset_password_page(req, args):
    async with aiofiles.open(os.getenv("HTML_LOCATION") + "reset_password.html", mode='r') as response:
        content = await response.read()
        return web.Response(text=content, content_type="text/html")