from aiogram.utils.keyboard import *
from aiogram import *


def get_keyboard_go_or_die(message):
    buttons = [ 
                [
                  types.InlineKeyboardButton(text="✅", callback_data=f'go_or_die_1_{message["msg_id"]}'),
                  types.InlineKeyboardButton(text="❌", callback_data=f'go_or_die_0_{message["msg_id"]}'),
                  types.InlineKeyboardButton(text="Skip", callback_data=f'go_or_die_2_{message["msg_id"]}') 
                ] 
             ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
