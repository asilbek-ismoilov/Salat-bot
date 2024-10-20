from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from baza.sqlite import Database

db = Database()

def get_salad_menu(page=0):
    # Bazadan barcha salatlar
    salads = db.select_all_salads()
    salads_per_page = 4
    start = page * salads_per_page
    end = start + salads_per_page
    sliced_salads = salads[start:end]

    keyboard = []

    # Salatlarni qo'shamiz
    for salad in sliced_salads:
        name = salad[1]
        keyboard.append([InlineKeyboardButton(text=name, callback_data=f"salad:{name}")])

    # ⬅️ va ➡️ tugmalari
    navigation_buttons = [
        InlineKeyboardButton(text="⬅️", callback_data=f"left:{page}"),
        InlineKeyboardButton(text="➡️", callback_data=f"right:{page}")
    ]
    keyboard.append(navigation_buttons)

    # Zakaz qilish tugmasi
    keyboard.append([InlineKeyboardButton(text="🛎 Zakaz qilish", callback_data="zakaz")])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)
