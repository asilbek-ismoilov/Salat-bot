from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import dp
from aiogram import F
from aiogram.types import CallbackQuery, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from keyboard_buttons.default import keyboardbutton

min_menu_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text= "⬅️",callback_data="left"),InlineKeyboardButton(text= "➡️",callback_data="right")],
        [InlineKeyboardButton(text= "🛎 Zakaz qilish",callback_data="🛎 Zakz qilish")],
        [InlineKeyboardButton(text= "Oliviya",callback_data="oliviya"),InlineKeyboardButton(text= "Fransuzki",callback_data="fransuzki")],
        [InlineKeyboardButton(text= "Mimoza",callback_data="mimoza"),InlineKeyboardButton(text= "Sezar",callback_data="sezar")],
        [InlineKeyboardButton(text= "Greek",callback_data="greek"),InlineKeyboardButton(text= "Caprese",callback_data="caprese")],
        [InlineKeyboardButton(text= "Nicoise",callback_data="Nicoise"),]
    ]
)

salads_info = {
    "Oliviya": {"photo": "https://ratatum.com/wp-content/uploads/2017/11/prazdnichyj-salat.jpg", "product": "Pamidor, Bodring"},
    "Fransuzki": {"photo": "https://ratatum.com/wp-content/uploads/2017/11/prazdnichyj-salat.jpg", "product": "Pamidor, Bodring"},
    "Mimoza": {"photo": "https://ratatum.com/wp-content/uploads/2017/11/prazdnichyj-salat.jpg", "product": "Pamidor, Bodring"},
    "Sezar": {"photo": "https://ratatum.com/wp-content/uploads/2017/11/prazdnichyj-salat.jpg", "product": "Pamidor, Bodring"},
    "Greek": {"photo": "https://ratatum.com/wp-content/uploads/2017/11/prazdnichyj-salat.jpg", "product": "Pamidor, Bodring"},
    "Caprese": {"photo": "https://ratatum.com/wp-content/uploads/2017/11/prazdnichyj-salat.jpg", "product": "Pamidor, Bodring"},
    "Nicoise": {"photo": "https://ratatum.com/wp-content/uploads/2017/11/prazdnichyj-salat.jpg", "product": "Pamidor, Bodring"},
}


@dp.callback_query(F.data=="🛎 Zakz qilish")
async def Uzs_usd(callback:CallbackQuery):
    await callback.answer("To'lov usuli")
    await callback.message("To'lov usuli",reply_markup=keyboardbutton.pay_button)
    await callback.message.delete()

@dp.callback_query(F.data.in_(["Oliviya", "Fransuzki", "Mimoza", "Sezar", "Greek", "Caprese", "Nicoise"]))
async def Uzs_usd(callback:CallbackQuery):
    
    await callback.message.delete()

@dp.callback_query(F.data=="")
async def Uzs_usd(callback:CallbackQuery):
    
    await callback.message.delete()

@dp.callback_query(F.data=="")
async def Uzs_usd(callback:CallbackQuery):
    
    await callback.message.delete()

@dp.callback_query(F.data=="")
async def Uzs_usd(callback:CallbackQuery):
    
    await callback.message.delete()
