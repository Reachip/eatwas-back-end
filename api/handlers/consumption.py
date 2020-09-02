import logging
from utils._jwt import auth_required
from utils.response import success, fail
from utils.date import get_week_number, get_day_number
from bdd.models import Consumption, User
from webargs import fields
from webargs.aiohttpparser import use_args

get_args = {
    "week": fields.Int(required=True),
    "day": fields.Int(required=True),
}

set_args = {
    "protein": fields.Int(required=True),
    "calories": fields.Int(required=True),
    "lipid": fields.Int(required=True),
    "glucides": fields.Int(required=True),
}


@auth_required()
@use_args(get_args)
async def get_consumption(req, token, get_args):
    try:
        user = await User.get(username=token["username"])
        consumptions = await Consumption.filter(
            user=user, week=get_args["week"], day=get_args["day"]
        )

        lipids = []
        calories = []
        glucides = []

        for consumption in consumptions:
            lipids.append(consumption.lipid)
            calories.append(consumption.calories)
            glucides.append(consumption.glucides)

        data = {
            "calories": sum(calories),
            "lipid": sum(lipids) / len(lipids) ,
            "glucides": sum(glucides) / len(glucides),
        }    
        
        return success(message=data)

    except ZeroDivisionError:
        return success(message=None)


@auth_required()
@use_args(set_args)
async def set_consumption(req, token, set_args):
    day_number = await get_day_number()
    week_number = await get_week_number()

    logging.debug("ENTRÉE DE LA CONSOMMATION DE L'UTILISATEUR")
    logging.debug(f"LE JOUR {day_number} DE LA SEMAINE {week_number}")

    user = await User.get(username=token["username"])
    await Consumption.create(
        day=day_number,
        week=week_number,
        protein=set_args["protein"],
        calories=set_args["calories"],
        lipid=set_args["lipid"],
        glucides=set_args["glucides"],
        user=user,
    )
    return success(message="")
