from aiogram.utils.keyboard import *
from aiogram import *


def get_keyboard_go_or_die(payment_id):
    buttons = [ 
                [
                  types.InlineKeyboardButton(text="✅", callback_data=f'go_or_die_1_{payment_id}'),
                  types.InlineKeyboardButton(text="❌", callback_data=f'go_or_die_0_{payment_id}'),
                  types.InlineKeyboardButton(text="Skip", callback_data=f'go_or_die_2_{payment_id}') 
                ] 
             ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
