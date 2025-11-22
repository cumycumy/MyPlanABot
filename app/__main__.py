from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher

import logging
import asyncio
import os

from . import BOT_MAIN
from . import routers


logging.basicConfig(
	level=logging.INFO,
	format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


bot = Bot(
	token=(os.environ['BOT_SECRET']),
	default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())

for router in routers.ROUTERS:
	dp.include_router(router)

try:
	asyncio.run(BOT_MAIN(bot, dp))
except KeyboardInterrupt:
	pass