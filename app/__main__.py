from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher

import logging
import asyncio
import os

from . import routers
from . import bot_main


logging.basicConfig(
	level=logging.INFO,
	format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


bot = Bot(
	token=os.environ['MyPlanABot'],
	default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())
dp.include_router(routers.default_router)

try:
	asyncio.run(bot_main(bot, dp))
except KeyboardInterrupt:
	pass