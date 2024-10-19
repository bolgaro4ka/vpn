import os
from datetime import datetime
import logging
import asyncio
from aiogram.filters.command import Command
import json
from aiogram import *
import aiogram.exceptions
import os
from pathlib import Path
from functions import *
from keyboards import *
import nest_asyncio
from dotenv import load_dotenv
import requests

nest_asyncio.apply()

load_dotenv()
SECRET_KEY = os.getenv("TG_API_KEY", "not_so_secret")
PASSWORD = os.getenv("PASSWORD", "1488")


bot = Bot(token=SECRET_KEY)

logging.basicConfig(level=logging.INFO)
dp = Dispatcher()


@dp.message(Command("start"))
async def user_registration(msg: types.Message):
    current_chat = msg.chat.id
    await bot.send_message(current_chat, 'Ну поехали.', parse_mode="HTML")


@dp.message(Command("m"))
async def user_registration(msg: types.Message):
    current_chat = msg.chat.id
    res = requests.get(os.getenv("BASE_URL") + "api/common/gpr/")

    if len(res.json()) == 0:
        await bot.send_message(current_chat, 'Нет платежей', parse_mode="HTML")

    await bot.send_message(current_chat, f"Платёж: {str(res.json()[0]['payment_id'])} \n\nПользователь: {str(res.json()[0]['user_id'])} \n\n Дата: {str(res.json()[0]['created_at'])} \n\n Это всё что мы знаем", parse_mode="HTML", reply_markup=get_keyboard_go_or_die(res.json()[0]['payment_id']))

@dp.callback_query()
async def callback_query(call: types.CallbackQuery):
    if 'go_or_die' in call.data:
        await call.message.delete()
        action = call.data.split('_')[3]
        payment_id = call.data.split('_')[4]

        if action == '1':
            # Логика потом добавлю
            await bot.send_message(call.from_user.id, f'Платёж оплачен. PID: {payment_id}', parse_mode="HTML")

        if action == '0':
            await bot.send_message(call.from_user.id, f'Платёж отменен. PID: {payment_id}', parse_mode="HTML")

        if action == '2':
            await bot.send_message(call.from_user.id, f'Платёж пропущен. PID: {payment_id}', parse_mode="HTML")
        
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())