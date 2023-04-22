from aiogram.dispatcher import dispatcher
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command, Text
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import asyncio
import logging

from os import getenv
from dotenv import load_dotenv

load_dotenv()

TOKEN = getenv('TOKEN')


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
