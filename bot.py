import requests

from aiogram import Dispatcher, Bot, types, executor

from config import BOT_TOKEN, TUNNEL_URL

from random import shuffle

predict = [1, 2, 3, 4, 5, 6, 7, 8]

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

WEBHOOK_PATH = f'/bot/{BOT_TOKEN}'
WEBHOOK_URL = f'{TUNNEL_URL}{WEBHOOK_PATH}'


@dp.message_handler(commands='start')
async def start(message: types.Message):
    shuffle(predict)
    await message.answer(f'{message.from_user.full_name}, {predict[0]}')


@dp.message_handler(commands='test')
async def test(message: types.Message):
    await message.answer('есть контактик')

# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)
