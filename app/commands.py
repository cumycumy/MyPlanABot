from dataclasses import dataclass

from . import routers


@dataclass(frozen=True, order=True)
class DefaultCommand:
	name: str
	description: str


DEFAULT_COMMANDS = sorted([
	DefaultCommand('start',
		'Запуск или перезапуск'),
	DefaultCommand('help',
		'Уточнить информацию'),
	DefaultCommand('menu',
		'Главное меню'),
	DefaultCommand('profile',
		'Показать профиль'),
])


__all__ = [
	'DefaultCommand',
	'DEFAULT_COMMANDS',
]