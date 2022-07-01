from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.data import keyboards_data as kd

__all__ = [
    "get_user_menu",
    "back",
]


async def get_user_menu():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(text="🤍", callback_data="act_1"),
        InlineKeyboardButton(text="🎁", callback_data="act_2"),
        InlineKeyboardButton(text="❔", callback_data="act_3"),
    )
    return keyboard


async def back():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text="Назад", callback_data="back"))
    return keyboard
