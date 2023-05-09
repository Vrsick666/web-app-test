from fastapi import FastAPI
from aiogram import types, Dispatcher, Bot
from bot import dp, bot
from config import TUNNEL_URL, BOT_TOKEN


app = FastAPI()
WEBHOOK_PATH = f'/bot/{BOT_TOKEN}'
WEBHOOK_URL = f'{TUNNEL_URL}{WEBHOOK_PATH}'


@app.on_event('startup')
async def on_startup():
    webhook_info = await bot.get_webhook_info()
    if webhook_info.url != WEBHOOK_URL:
        await bot.set_webhook(url=WEBHOOK_URL)


@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    print(telegram_update)
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_update(telegram_update)
    print(str(update['message']['from']['id']))
    await bot.send_message(str(update['message']['from']['id']), 'accepted')


@app.get(WEBHOOK_PATH+'/code')
async def code_require():
    telegram_update = types.Update(**{"update_id": 542413245, "callback_query": "get code"})
    print(telegram_update)
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_update(telegram_update)


@app.on_event('shutdown')
async def on_shutdown():
    await bot.session.close()
