from utils.response import success, fail
from webargs.aiohttpparser import use_args
from webargs import fields

args = {
    "date": fields.Str(required=True),
}


@use_args(args)
async def data(req, args):
    return success(message="mdr")
