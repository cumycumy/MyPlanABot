from aiogram.utils.keyboard import (
	InlineKeyboardBuilder,
	ReplyKeyboardBuilder,
)


start_keyboard = (InlineKeyboardBuilder()
	.button(text='Меню', callback_data='menu')
).as_markup()

menu_keyboard = (InlineKeyboardBuilder()
	.button(text='Профиль', callback_data='profile_get')
).as_markup()

profile_keyboard = (InlineKeyboardBuilder()
	.button(text='Перезаполнить', callback_data='profile_reset')
	.button(text='Назад', callback_data='Menu')
).as_markup()