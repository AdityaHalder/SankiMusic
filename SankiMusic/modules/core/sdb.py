# Sanki Database

from SankiMusic.utilities import config
from ...console import LOGGER

from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_



_mongo_async_ = _mongo_client_(config.MONGO_DB_URL)
_mongo_sync_ = MongoClient(config.MONGO_DB_URL)
mongodb = _mongo_async_.Rose
pymongodb = _mongo_sync_.Rose
