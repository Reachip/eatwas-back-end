import logging
import uuid
import os
from utils.response import success, fail
from bdd.models import User
from tortoise.exceptions import DoesNotExist
from webargs import fields
from webargs.aiohttpparser import use_args
import aiofiles
from aiohttp import web

args = {"uuid": fields.UUID(required=True)}

@use_args(args)
async def validate_user(req, args):
    try:
        user = await User.get(uuid=args["uuid"])
        user.user_is_validate = 1
        user.uuid = str(uuid.uuid4())
        await user.save()
        
        async with aiofiles.open(os.getenv("HTML_LOCATION") + "validation.html") as response:
            return web.Response(text=await response.read(), content_type="text/html")

    except DoesNotExist:
        return fail(status_code=401, message="Impossible de valider l'enregistrement de l'utilisateur concerné : Identifiant invalide")
