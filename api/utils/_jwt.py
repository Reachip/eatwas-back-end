import asyncio
import os
import functools
import logging
import jwt

from utils.date import _get_age_sync
from utils.response import fail


def _get_secret_jwt_key():
    secret_key = os.environ.get("SECRET_JWT_KEY")

    if secret_key is None:
        raise jwt.exceptions.InvalidKeyError("Variable d'environnement SECRET_JWT_KEY non-fourni")

    return secret_key


def auth_required():
    def decorator(fn):
        @functools.wraps(fn)
        async def wrapped(*args):
            try:
                request = args[0]
                supposed_token = request.headers['Authorization'].split()[1]
                logging.debug(f"TOKEN JWT RECU => {supposed_token}")
                token = await decode_token(supposed_token)

                return await fn(*args, token)

            except KeyError:
                return fail(message="Jeton JWT non-fourni", status_code=401)

        return wrapped
        
    return decorator


async def decode_token(supposed_token):
    def decode_token_sync():
        key = _get_secret_jwt_key()
        token = jwt.decode(supposed_token, key=key, algorithms='HS256', verify=True)

        return token

    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, decode_token_sync)


async def get_token(user):
    def get_token_sync():
        payload = {
            "username": user.username,
            "sex": user.sex,
            "goal": user.goal,
            "weight": user.weight,
            "sportFrequency": user.sportfrequency,
            "size": user.size,
            "age": _get_age_sync(user)
        }

        secret_key = _get_secret_jwt_key()
        return jwt.encode(payload, secret_key, algorithm='HS256').decode("utf-8")

    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, get_token_sync)
