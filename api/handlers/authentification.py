import logging

from webargs.aiohttpparser import use_args
from webargs import fields
from tortoise.exceptions import DoesNotExist

from bdd.models import User
from utils.response import success, fail
from utils.password import check_hashed_password_with_salt
from utils._jwt import get_token


args = {
    "username": fields.String(required=True),
    "password": fields.String(required=True),
}


@use_args(args)
async def authentificate(req, args):
    logging.debug(f"DEMANDE D'AUTHENTIFICATION")
    try:
        user = await User.get(username=args["username"])
        password_is_correct = await check_hashed_password_with_salt(
            args["password"], user.hashed_password, user.salt
        )

        if not password_is_correct:
            logging.debug(f"MOT DE PASSE INCORRECTE")
            raise DoesNotExist
            
        if user.user_is_validate == 0:
            logging.debug(f"UTILISATEUR NON VALIDÉ")
            return fail(status_code=401, message="Vous devez valider votre inscription avant d'accéder à EatWas. Veuillez Vérifier votre boîte mail.")

        logging.debug(f"RECUPERATION D'UN TOKEN JWT")        
        token = await get_token(user)
        return success(token)

    except DoesNotExist as why:
        logging.debug(f"NOM D'UTILISATEUR OUR MOT DE PASSE INCORRECTE POUR {args['username']} :: {why}")
        return fail(
            status_code=401, message="Nom d'utilisateur ou mot de passe incorrect"
        )

    except Exception as why:
        logging.debug(f"ERREUR DIVERS :: {why}")
        return fail(status_code=500, message="Impossible de générer un token JWT")

