""" Module for server running """

from aiohttp import web

from src.server import SERVER


if __name__ == "__main__":
    web.run_app(
        SERVER
    )
