import logging
import datetime
import asyncio


def _get_age_sync(user):
    actual_date = datetime.datetime.now().date()
    return actual_date.year - user.birthday.year

def _get_week_number_sync():
    actual_date = datetime.datetime.now().date()
    return actual_date.isocalendar()[1]

def _get_day_number_sync():
    actual_date = datetime.datetime.today()
    return actual_date.weekday()

async def get_day_number():
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, _get_day_number_sync)

async def get_age(user):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, _get_age_sync, user)
    
async def get_week_number():
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, _get_week_number_sync)