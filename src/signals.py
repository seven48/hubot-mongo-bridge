""" Module for aiohttp signals """

from src.db import Connection


async def on_startup(_):
    """ Function that will called on server starting """

    connection = Connection(host='localhost', port=27018)
    await connection.check_connection()
