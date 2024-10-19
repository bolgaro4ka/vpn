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
    res = requests.get(os.getenv("URL") + "api/common/gpr/")
    await bot.send_message(current_chat, str(res.json()), parse_mode="HTML")


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())