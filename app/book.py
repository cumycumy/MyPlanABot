from aiogram.filters import Command, CommandStart
from aiogram import F


BOT_DESCRIPTION = (
	'1. Поможет составить личный график и распорядок с учётом повседневной нагрузки.\n'
	'2. Порекомендует изменения графика или распорядка при изменениях нагрузки и условий.\n'
	'3. Уведомит о переходе к определённому пункту графика или распорядка.\n'
	'4. Покажет статистику личного графика и распорядка по различным параметрам.\n'
)

DEFAULT_START_ANSWER = (
	'Привет, {username}! Я - твой помощник в планировании графика и распорядка!\n'
	'Приятно познакомиться, будь уверен - мы очень быстро подружимся!\n'
	'\n'
	'В боковом меню ты сможешь найти все команды с описанием.\n'
	'Если тебе что-то будет непонятно - отправь /help.\n'
)

DEFAULT_HELP_ANSWER = (
	'Вижу, возникли некоторые вопросы...тогда разъясню:\n'
)
DEFAULT_HELP_COMMAND_START_ANSWER = (
	'/start 	- запуск или перезапуск\n'
)
DEFAULT_HELP_COMMAND_HELP_ANSWER = (
	'/help 		- уточнить информацию о командах\n'
)
DEFAULT_HELP_COMMAND_MENU_ANSWER = (
	'/menu 		- главное меню\n'
)
DEFAULT_HELP_COMMAND_SCHEDULES_ANSWER = (
	'/schedules - главное меню\n'
)
DEFAULT_HELP_COMMAND_ROUTINES_ANSWER = (
	'/routines 	- главное меню\n'
)
DEFAULT_HELP_COMMAND_SCHEDULE_ANSWER = (
	'/schedule	- главное меню\n'
)

DEFAULT_MENU_ANSWER = (
	'Главное меню\n'
)

DEFAULT_PROFILE_GET_ANSWER = (
	'{username} id{identificator}\n'
	'Графики: {schedule}\n'
	'Распорядки: {routines}\n'
)


DEFAULT_START_NAME 		= 'start'
DEFAULT_HELP_NAME 		= 'help'
DEFAULT_MENU_NAME 		= 'menu'
DEFAULT_SCHEDULES_NAME 	= 'schedules'
DEFAULT_ROUTINES_NAME 	= 'routines'
DEFAULT_SCHEDULE_NAME 	= 'schedule'

DEFAULT_START_DESCRIPTION 		= 'Запуск или перезапуск'
DEFAULT_HELP_DESCRIPTION 		= 'Уточнить информацию'
DEFAULT_MENU_DESCRIPTION 		= 'Главное меню'
DEFAULT_SCHEDULES_DESCRIPTION 	= 'Мои распорядки'
DEFAULT_ROUTINES_DESCRIPTION 	= 'Мои графики'
DEFAULT_SCHEDULE_DESCRIPTION 	= 'Моё расписание'

DEFAULT_START_COMMAND 		= CommandStart()
DEFAULT_HELP_COMMAND 		= Command(DEFAULT_HELP_NAME)
DEFAULT_MENU_COMMAND 		= Command(DEFAULT_MENU_NAME)
DEFAULT_SCHEDULES_COMMAND 	= Command(DEFAULT_SCHEDULES_NAME)
DEFAULT_ROUTINES_COMMAND 	= Command(DEFAULT_ROUTINES_NAME)
DEFAULT_SCHEDULE_COMMAND 	= Command(DEFAULT_SCHEDULE_NAME)

DEFAULT_START_ANSWER 		= '''
	Привет, {username}! Я - твой помощник в планировании графика и распорядка!
	Приятно познакомиться, будь уверен - мы очень быстро подружимся!
	
	Если тебе что-то будет непонятно - помощь всегда на виду - лишь нажми /help.
'''
DEFAULT_HELP_ANSWER 		= '''
help
'''
DEFAULT_MENU_ANSWER 		= '''
menu
'''
DEFAULT_SCHEDULES_ANSWER 	= '''
schedules
'''
DEFAULT_ROUTINES_ANSWER 	= '''
routines
'''
DEFAULT_SCHEDULE_ANSWER 	= '''
schedule
'''

DEFAULT_START_CALLBACK 		= F.data == 'start'
DEFAULT_HELP_CALLBACK 		= F.data == 'help'
DEFAULT_MENU_CALLBACK 		= F.data == 'menu'
DEFAULT_SCHEDULES_CALLBACK 	= F.data == 'schedules'
DEFAULT_ROUTINES_CALLBACK 	= F.data == 'routines'
DEFAULT_SCHEDULE_CALLBACK 	= F.data == 'schedule'