from aiogram.types import Message, CallbackQuery
from aiogram.filters import (
	CommandObject,
	CommandStart,
	Command,
)
from aiogram import Router, F

import os

from . import keyboards
from . import filters
from . import book


default_router = Router()


@default_router.message(CommandStart())
async def default_start(
		message: Message,
		command: CommandObject):
	await message.answer(
		book.DEFAULT_START_ANSWER.format(
			username=message.from_user.first_name),
		reply_markup=keyboards.start_keyboard)

@default_router.message(Command('help'))
async def default_help(
		message: Message,
		command: CommandObject):
	if command.args:
		answer = [book.DEFAULT_HELP_ANSWER]
		for arg in command.args.split(' '):
			match arg:
				case 'start':
					answer.append(book.DEFAULT_HELP_COMMAND_START_ANSWER)
				case 'help':
					answer.append(book.DEFAULT_HELP_COMMAND_HELP_ANSWER)
				case 'menu':
					answer.append(book.DEFAULT_HELP_COMMAND_MENU_ANSWER)
	else:
		answer = [
			book.DEFAULT_HELP_ANSWER,
			book.DEFAULT_HELP_COMMAND_START_ANSWER,
			book.DEFAULT_HELP_COMMAND_HELP_ANSWER,
			book.DEFAULT_HELP_COMMAND_MENU_ANSWER,
		]
	await message.answer(''.join(answer))


@default_router.message(Command('menu'))
async def default_menu(
		message: Message,
		command: CommandObject):
	await message.answer(
		book.DEFAULT_MENU_ANSWER,
		reply_markup=keyboards.menu_keyboard)

@default_router.callback_query(F.data == 'menu')
async def default_callback_menu(callback: CallbackQuery):
	await callback.message.edit_text(
		book.DEFAULT_MENU_ANSWER,
		reply_markup=keyboards.menu_keyboard)


@default_router.message(Command('profile'))
async def default_profile(
		message: Message,
		command: CommandObject):
	await message.answer(
		book.DEFAULT_PROFILE_GET_ANSWER,
		reply_markup=keyboards.profile_keyboard)

@default_router.callback_query(F.data == 'profile_get')
async def default_callback_profile_get(callback: CallbackQuery):
	await callback.message.edit_text(
		book.DEFAULT_PROFILE_GET_ANSWER,
		reply_markup=keyboards.profile_keyboard)


__all__ = ['default_router']