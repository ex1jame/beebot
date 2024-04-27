from aiogram import Bot, Dispatcher, F
import asyncio

from app.database.models import async_main
from app.handlers import router


async def main():
    await async_main()
    bot = Bot(token='7166991834:AAFQOCQ5P9EvWV2tR80QI4AN40hRnwLwWl0')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")