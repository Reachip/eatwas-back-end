import asyncio
import hashlib
import uuid


async def get_hashed_password_and_salt(password):
    def get_hashed_password_and_salt_sync():
        salt = uuid.uuid4().hex
        encoded_string = (password + salt).encode("utf-8")       
        hashed_password = hashlib.sha256(encoded_string).hexdigest()

        return (hashed_password, salt)

    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, get_hashed_password_and_salt_sync)

async def check_hashed_password_with_salt(password, given_hashed_password, salt):
    def check_hashed_password_with_salt_sync():
        encoded_string = (password + salt).encode("utf-8")
        hashed_password = hashlib.sha256(encoded_string).hexdigest()

        return hashed_password == given_hashed_password

    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, check_hashed_password_with_salt_sync)