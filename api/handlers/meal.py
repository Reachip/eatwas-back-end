import asyncio
import logging

from utils._jwt import auth_required
from utils.response import success, fail
from utils.suggestion import Suggestion
from utils.greenpeace_sheet import GreenPeaceSheet

@auth_required()
async def suggestion(req, token):
    loop = asyncio.get_event_loop()
    suggestion = await loop.run_in_executor(None, Suggestion, token)
    meal, fruit = await loop.run_in_executor(None, suggestion.suggest)
    logging.debug(f"RECUPERATION D'UN REPAS : {meal}")
    logging.debug(f"RECUPERATION D'UN FRUIT : {fruit}")
    message = {
        "dish": {
            "name": meal.name,
            "protein": meal.protein,
            "calories": meal.calories,
            "lipid": meal.lipid, 
            "glucides": meal.glucides,
        },

        "fruit": {
            "name": fruit.name,
            "month": fruit.months_of_consumption
        }
    }

    logging.debug(f"SUGGESTION : {message}")
    return success(message=message)
