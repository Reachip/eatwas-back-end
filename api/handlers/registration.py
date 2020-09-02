import logging
import uuid
from aiohttp import web
from webargs import fields
from webargs.aiohttpparser import use_args
from utils.response import success, fail
from utils.password import get_hashed_password_and_salt
from utils.mail import send_validation_url
from bdd.models.user import User

args = {
    "username": fields.Str(required=True),
    "password": fields.Str(required=True),
    "sex": fields.Integer(required=True),
    "email": fields.Email(required=True),
    "sportFrequency": fields.Float(required=True),
    "goal": fields.Integer(required=True),
    "size": fields.Float(required=True),
    "weight": fields.Float(required=True),
    "birthday": fields.Date(required=True)
}


@use_args(args)
async def register(req, args):
    logging.debug("DEMANDE D'INSCRIPTION REÇU")
    logging.debug(args)
    user_uuid = str(uuid.uuid4())

    try:
        hashed_password, salt = await get_hashed_password_and_salt(args["password"])

        await User.create(
            uuid=user_uuid,
            user_is_validate=False,
            username=args["username"],
            hashed_password=hashed_password,
            email=args["email"],
            sex=args["sex"],
            salt=salt,
            weight=args["weight"],
            goal=args["goal"],
            sportfrequency=args["sportFrequency"],
            size=args["size"],
            birthday=args["birthday"]
        )

        validation_url = f"http://192.168.10.105:8080/api/user/validate?uuid={user_uuid}"
        await send_validation_url(validation_url, args["email"])
        return success(message={"message": "Utilisateur ajouté avec succès. Un mail de confirmation a été envoyé à l'adresse mail communiqué lors de l'inscription.", "uuid": user_uuid})
    
    except Exception as why:    
        logging.debug(why)
        return fail(401, "Cet utilisateur existe déjà")
