from aiogram.types import BotCommand, BotCommandScopeDefault
from aiogram import Bot, Dispatcher

from .commands import DEFAULT_COMMANDS
from .book import BOT_DESCRIPTION


async def bot_main(bot, dp):
	await bot.set_my_description(
			description=BOT_DESCRIPTION,
			language_code='ru')
	await bot.set_my_commands([
		BotCommand(
			command=command.name,
			description=command.description)
		for command in DEFAULT_COMMANDS
	], scope=BotCommandScopeDefault())
	await bot.delete_webhook(drop_pending_updates=True)
	await dp.start_polling(bot)


__all__ = ['bot_main']