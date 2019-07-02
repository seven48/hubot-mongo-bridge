""" Module for aiohttp signals """

from src.db import Connection
from src.settings import MONGODB_HOST, MONGODB_PORT


async def on_startup(_):
    """ Function that will called on server starting """

    Connection(host=MONGODB_HOST, port=MONGODB_PORT)
