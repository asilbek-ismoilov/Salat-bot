from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# menu Button
max_menu_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🥗 Salatlar"),KeyboardButton(text="🛎 Zakz qilish")],
        [KeyboardButton(text="📍 Manzil"),KeyboardButton(text="🙋🏻‍♀️ Biz haqimizda")]    
    ],
   resize_keyboard=True,
   input_field_placeholder="Tanlang .. "
)

# 🛎 Zakz qilish button 

pays = [
    "💳 Karta orqali",
    "💵 Naqd pul"
]

pay_button = ReplyKeyboardBuilder()

for pay in  pays:
    pay_button.add(KeyboardButton(text= pay))

pay_button.adjust(2, repeat=True)
pay_button.row(KeyboardButton(text="🔙 ortga"))
pay_button = pay_button.as_markup( resize_keyboard=True, input_field_placeholder="Tanlang .. ")
