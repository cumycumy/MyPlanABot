from aiogram.types import BotCommand, BotCommandScopeDefault
from aiogram import Bot, Dispatcher

from .book import BOT_DESCRIPTION
from . import properties


async def BOT_MAIN(bot, dp):
	await bot.set_my_description(
			description=BOT_DESCRIPTION,
			language_code='ru')
	await bot.set_my_commands([
		BotCommand(
			command=command.name,
			description=command.description)
		for command in properties.DEFAULT_COMMANDS
	], scope=BotCommandScopeDefault())
	await bot.delete_webhook(drop_pending_updates=True)
	await dp.start_polling(bot)


__all__ = ['BOT_MAIN']