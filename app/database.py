from sqlalchemy.ext.asyncio import (
	create_async_engine,
	async_sessionmaker,
	AsyncSession,
)
from sqlalchemy import text

import os

from . import models


print('Database is initialized!')