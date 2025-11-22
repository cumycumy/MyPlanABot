from aiogram.types import Message, CallbackQuery
from aiogram.filters import (
	CommandObject,
	CommandStart,
	Command,
)
from aiogram import Router, F

from . import properties
from . import keyboards
from . import filters


DEFAULT_ROUTER = Router()


@DEFAULT_ROUTER.message(properties
	.DEFAULT_COMMAND_START.command)
async def default_command_start(
		message: Message,
		command: CommandObject):
	await message.answer(
		(properties.DEFAULT_COMMAND_START.answer
			.format(username=message.from_user.first_name)
		), reply_markup=keyboards.start_keyboard)

@DEFAULT_ROUTER.callback_query(properties
	.DEFAULT_CALLBACK_START.callback)
async def default_callback_start(callback: CallbackQuery):
	await callback.message.edit_text(
		(properties.DEFAULT_CALLBACK_START.answer
			.format(
				username=callback.message.from_user.first_name)
		), reply_markup=keyboards.start_keyboard)


@DEFAULT_ROUTER.message(properties
	.DEFAULT_COMMAND_HELP.command)
async def default_command_help(
		message: Message,
		command: CommandObject):
	answer = await properties.COMMAND_MATCH(
		properties.DEFAULT_COMMANDS, command.args.split(' '))
	await message.answer(answer)

@DEFAULT_ROUTER.callback_query(properties
	.DEFAULT_CALLBACK_HELP.callback)
async def default_command_help(callback: CallbackQuery):
	await message.answer(DEFAULT_CALLBACK_HELP.answer)


@DEFAULT_ROUTER.message(properties
	.DEFAULT_COMMAND_MENU.command)
async def default_command_menu(
		message: Message,
		command: CommandObject):
	await message.answer(
		book.DEFAULT_MENU_ANSWER,
		reply_markup=keyboards.menu_keyboard)

@DEFAULT_ROUTER.callback_query(F.data == 'menu')
async def default_callback_menu(callback: CallbackQuery):
	await callback.message.edit_text(
		book.DEFAULT_MENU_ANSWER,
		reply_markup=keyboards.menu_keyboard)


ROUTERS = [
	DEFAULT_ROUTER,
]

__all__ = [
	'ROUTERS',
	'DEFAULT_ROUTER',
]