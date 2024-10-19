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
BASE_URL = os.getenv("BASE_URL", "")

bot = Bot(token=SECRET_KEY)

logging.basicConfig(level=logging.INFO)
dp = Dispatcher()
admins = ['1587780429', '1636897876']

async def check_payments():
    """Фоновая задача для периодической проверки новых платежей."""
    while True:
        try:
            res = requests.get(BASE_URL + "api/common/gpr/")
            payments = res.json()

            if len(payments) == 0:
                logging.info("Нет новых платежей")
            else:
                for aid in admins:
                    await bot.send_message(aid, f"Платёж: {str(res.json()[0]['payment_id'])} \n\nПользователь: {str(res.json()[0]['user_id'])} \n\n Дата: {str(res.json()[0]['created_at'])} \n\n Это всё что мы знаем", parse_mode="HTML", reply_markup=get_keyboard_go_or_die(res.json()[0]['payment_id']))
        except Exception as e:
            logging.error(f"Ошибка при проверке платежей: {e}")

        # Задержка между проверками (например, 60 секунд)
        await asyncio.sleep(60)


@dp.message(Command("start"))
async def user_registration(msg: types.Message):
    current_chat = str(msg.chat.id)
    if not (current_chat in admins):
        await bot.send_message(current_chat, 'Ты не админ. Ухади', parse_mode="HTML")
        return
    await bot.send_message(current_chat, 'Ну поехали.', parse_mode="HTML")


@dp.message(Command("m"))
async def user_registration(msg: types.Message):
    current_chat = str(msg.chat.id)
    if not (current_chat in admins):
        await bot.send_message(current_chat, 'Ты не админ. Ухади', parse_mode="HTML")
        return
    res = requests.get(os.getenv("BASE_URL") + "api/common/gpr/")

    if len(res.json()) == 0:
        await bot.send_message(current_chat, 'Нет платежей', parse_mode="HTML")
        return

    await bot.send_message(current_chat, f"Платёж: {str(res.json()[0]['payment_id'])} \n\nПользователь: {str(res.json()[0]['user_id'])} \n\n Дата: {str(res.json()[0]['created_at'])} \n\n Это всё что мы знаем", parse_mode="HTML", reply_markup=get_keyboard_go_or_die(res.json()[0]['payment_id']))

@dp.message()
async def echo(msg: types.Message):
    current_chat = str(msg.chat.id)
    if not (current_chat in admins):
        await bot.send_message(current_chat, 'Ты не админ. Ухади', parse_mode="HTML")

    try:
        user_id = msg.split(' ')[0]
        money = msg.split(' ')[1]
    except IndexError:
        await bot.send_message(current_chat, 'Неправильная команда. \n\nПаттерн: <user_id> <money>', parse_mode="HTML")
        return

    res = requests.post(os.getenv("BASE_URL") + "api/common/give_money/", json={'user_id': user_id, 'money': money})
    if res.status_code == 200:
        await bot.send_message(current_chat, f'{money} рублей успешно выдано', parse_mode="HTML")
    else:
        err = res.json()['error']
        await bot.send_message(current_chat, f'Ошибка при выдаче денег: {err}', parse_mode="HTML")


@dp.callback_query()
async def callback_query(call: types.CallbackQuery):
    if 'go_or_die' in call.data:
        await call.message.delete()
        action = call.data.split('_')[3]
        payment_id = call.data.split('_')[4]

        if action == '1':
            # Логика потом добавлю
            res = requests.post(os.getenv("BASE_URL") + "api/common/dpr/", json={'payment_id': payment_id})
            if res.status_code == 200:
                await bot.send_message(call.from_user.id, f'Платёж оплачен. Не забудьте закинуть лавехи пользователю.\n\n PID: {payment_id}', parse_mode="HTML")
            else:
                err = res.json()['error']
                await bot.send_message(call.from_user.id, f'Платёж не оплачен (ошибка).\n\n Причина: {err}\n\n PID: {payment_id}', parse_mode="HTML")

        if action == '0':
            res = requests.post(os.getenv("BASE_URL") + "api/common/dpr/", json={'payment_id': payment_id})
            if res.status_code == 200:
                await bot.send_message(call.from_user.id, f'Платёж отменен. PID: {payment_id}', parse_mode="HTML")
            else:
                err = res.json()['error']
                await bot.send_message(call.from_user.id, f'Платёж не оплачен (ошибка).\n\n Причина: {err}\n\n PID: {payment_id}', parse_mode="HTML")

        if action == '2':
            await bot.send_message(call.from_user.id, f'Платёж пропущен. PID: {payment_id}', parse_mode="HTML")
        
async def main():
    # Запуск фоновой задачи для проверки платежей
    asyncio.create_task(check_payments())
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())