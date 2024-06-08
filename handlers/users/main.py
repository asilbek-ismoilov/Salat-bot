from aiogram.types import Message
from aiogram import F
from loader import dp
from keyboard_buttons.default import keyboardbutton
from keyboard_buttons.inline import inlinebutton

@dp.message(F.text=="🥗 Salatlar")
async def info_salads(message:Message):
    await message.answer("Bizning salatlar",reply_markup=inlinebutton.min_menu_button) #

# @dp.message(F.text.func(lambda  salad: salad in  inlinebutton.salads))
# async def  salad_info(message:Message):
#     info = inlinebutton.salads_info.get(message.text)

#     photo = info.get("photo")
#     product = info.get("product")

#     text = f"{message.text} \nSalat: {product}"

#     await message.answer_photo(photo=photo,caption=text, reply_markup=inlinebutton.min_menu_button)

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
