from aiohttp import web


def success(message):
    return web.json_response({"code": 200, "message": message})


def fail(status_code, message):
    return web.json_response({"code": status_code, "message": message})
