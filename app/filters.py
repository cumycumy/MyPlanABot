from aiogram.filters import BaseFilter
from aiogram.types import Message

import os


class AdminFilter(BaseFilter):
	async def __call__(self, message: Message) -> bool:
		return (True
			if message.from_user.id == os.environ['AdminID']
			else False)