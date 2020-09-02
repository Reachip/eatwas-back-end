import asyncio
import uuid

from utils.password import get_hashed_password_and_salt
from .user import User
from .consumption import Consumption
from .energy_expenditure import EnergyExpenditure

from tortoise.exceptions import IntegrityError

async def make_easter_eggs():
    hashed_password, salt = await get_hashed_password_and_salt("admin")
    
    try:
        await User.create(
            uuid=str(uuid.uuid4()), 
            username="admin", 
            user_is_validate=True,
            hashed_password=hashed_password,
            salt=salt,
            email="vuvu@gmail.com",
            weight=150,
            size=1.65,
            goal=1,
            sportfrequency=0,
            sex=1,
            birthday="1970-01-01"
        )

    except IntegrityError:
        pass

