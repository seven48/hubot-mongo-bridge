""" Module for server initialization """

from aiohttp import web

from src.router import ROUTER


SERVER = web.Application()

SERVER.add_routes(ROUTER)
