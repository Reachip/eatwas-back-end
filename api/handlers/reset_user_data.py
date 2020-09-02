import logging
from webargs import fields
from bdd.models import User
from utils._jwt import auth_required
from utils._jwt import get_token
from webargs.aiohttpparser import use_args
from utils.response import success

args = {
    "goal": fields.Integer(required=False),
    "weight": fields.Float(required=False),
    "sportFrequency": fields.Float(required=False),
    "size": fields.Float(required=False)
}

@auth_required()
@use_args(args)
async def reset_user_data(req, token, args):
    user = await User.get(username=token["username"])

    try:
        user.goal = args["goal"]

    except KeyError:
        pass
    
    try:
        user.weight = args["weight"]

    except KeyError:
        pass
    
    try:
        user.sportFrequency = args["sportFrequency"]
    
    except KeyError:
        pass

    try:
        user.size = args["size"]

    except KeyError:
        pass

    finally:
        await user.save()
        new_token = await get_token(user)
        return success(message=new_token)

    

    
