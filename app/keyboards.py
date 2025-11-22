from aiogram.utils.keyboard import (
	InlineKeyboardBuilder,
	ReplyKeyboardBuilder,
)


start_keyboard = (InlineKeyboardBuilder()
	# [1]
	.button(text='Меню', 		callback_data='menu')
	.button(text='Помошь',		callback_data='help')
	
	.adjust(2)
).as_markup()

HELP_KEYBOARD = (InlineKeyboardBuilder()
	# [1]
	.button(text='Меню',		callback_data='menu')
	# [2]
	.button(text='start', 		callback_data='help-start')
	.button(text='help',		callback_data='help-help')
	.button(text='menu', 		callback_data='help-menu')
	# [3]
	.button(text='schedules', 	callback_data='help-schedules')
	.button(text='routines', 	callback_data='help-routines')
	.button(text='schedule', 	callback_data='help-schedule')
	
	.adjust(1, 3, 3)
).as_markup()

menu_keyboard = (InlineKeyboardBuilder()
	# [1]
	.button(text='Графики', 	callback_data='schedules')
	.button(text='Распорядки', 	callback_data='routines')
	.button(text='Расписание', 	callback_data='schedule')

	.adjust(3)
).as_markup()