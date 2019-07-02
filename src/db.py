""" Module for connecting to MongoDB """

from motor import motor_asyncio


class Connection:  # pylint: disable=too-few-public-methods
    """ Class for connecting to mongodb """

    INSTANCE = None

    def __init__(self, host='localhost', port=27017):
        """ Creating connection to MongoDB """

        self.connection = motor_asyncio.AsyncIOMotorClient(
            host=host,
            port=port
        )

    def __new__(cls, *args, **kwargs):
        """ Implementation of singleton """

        if not cls.INSTANCE:
            cls.INSTANCE = super(cls, Connection).__new__(cls)
            cls.INSTANCE.__init__(*args, **kwargs)

        return cls.INSTANCE
