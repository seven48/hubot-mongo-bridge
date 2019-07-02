""" Module for views """

from aiohttp import web


async def get_locale(request):
    """Handler for getting user locale by id"""
    try:
        user_id = request.rel_url.query['user_id']
    except KeyError:
        raise web.HTTPBadRequest(text="user_id not found")
    # TODO: connect and get info from mongo here  # pylint: disable=fixme
    return web.Response(text=f"Hello, {user_id}")
