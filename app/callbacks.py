from aiogram.filters import CallbackData


class MenuCallback(CallbackData, prefix='menu'):
	commands: str