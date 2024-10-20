from aiogram.types import Message, CallbackQuery
from aiogram import F
from loader import dp
from keyboard_buttons.default import keyboardbutton
from keyboard_buttons.inline.inlinebutton import get_salad_menu, db


@dp.message(F.text=="🥗 Salatlar")
async def info_salads(message: Message):
    await message.answer("Bizning salatlar", reply_markup=get_salad_menu(page=0))

# Sahifalar orasida harakatlanish uchun tugmalarni boshqarish
@dp.callback_query(lambda call: call.data.startswith("left") or call.data.startswith("right"))
async def navigate_salads(call: CallbackQuery):
    direction, current_page = call.data.split(":")
    current_page = int(current_page)

    # Harakatlanish logikasi
    if direction == "left":
        if current_page == 0:
            await call.answer("Siz 1 - sahifadasiz", show_alert=True)
            return
        current_page -= 1
    elif direction == "right":
        if (current_page + 1) * 4 >= len(db.select_all_salads()):
            await call.answer("Oxirgi sahifada turibsiz", show_alert=True)
            return
        current_page += 1

    # Yangi menyuni jo'natamiz
    await call.message.edit_reply_markup(reply_markup=get_salad_menu(page=current_page))

# Salat tavsifini ko'rsatish
@dp.callback_query(lambda call: call.data.startswith("salad:"))
async def show_salad_description(call: CallbackQuery):
    salad_name = call.data.split(":")[1]
    salad = db.select_salad_by_name(salad_name)
    if salad:
        name, photo, description = salad
        message_text = f"{name} salatasi\n\n{description}"
        await call.message.answer_photo(photo=photo, caption=message_text, reply_markup=get_salad_menu(0))
    else:
        await call.message.answer("Bunday salat topilmadi.")
    await call.answer()  # Xabarni ko'rsatish uchun


@dp.message(F.text=="🛎 Zakz qilish")
async def order_salad(message:Message):
    await message.answer("To'lov usuli",reply_markup=keyboardbutton.pay_button)

@dp.message(F.text =="🙋🏻‍♀️ Biz haqimizda")
async def about_as(message:Message):
    about = "Biz to'ylar, bayramlar va har xil marosimlar uchun \"🥗Salatlar\" va \"🥠Somsalar\" tayyorlab beramiz" 
    await message.answer(text= about)

@dp.message(F.text == "📍 Manzil")
async def workplace(message:Message):
    lat = 40.102296
    long = 65.37345
    await message.answer("📍 Bizning ish joyimiz")
    await message.reply_location(latitude=lat,longitude=long)

@dp.message(F.text=="🔙 ortga")
async def computer_func(message:Message):
    text = "Asosiy menyu"
    await message.answer(text=text, reply_markup=keyboardbutton.max_menu_button)
