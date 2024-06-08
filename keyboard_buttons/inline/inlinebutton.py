from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

min_menu_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text= "⬅️",callback_data="left"),InlineKeyboardButton(text= "➡️",callback_data="right")],
        [InlineKeyboardButton(text= "🛎 Zakaz qilish",callback_data="🛎 Zakz qilish")],
        [InlineKeyboardButton(text= "Oliviya",callback_data="oliviya"),InlineKeyboardButton(text= "Fransuzki",callback_data="fransuzki")],
        [InlineKeyboardButton(text= "Mimoza",callback_data="mimoza"),InlineKeyboardButton(text= "Sezar",callback_data="sezar")],
    ]
)
