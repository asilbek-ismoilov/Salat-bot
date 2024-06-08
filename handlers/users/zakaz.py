from aiogram.types import Message
from aiogram import F
from loader import dp


@dp.message(F.text == "💳 Karta orqali")
async def about_as(message:Message):
    
    photo = "file:///C:/Users/Sozla.uz/OneDrive/Рабочий%20стол/My%20py%20Projrct/img/card.webp"
    text = "Ushbu karta laqamlariga pulni yuborishingiz mumkin ❗️"
    await message.answer_photo(photo=photo, caption= text)

@dp.message(F.text == "💵 Naqd pul")
async def about_as(message:Message):

    lat = 40.102296
    long = 65.37345
    await message.answer("📍 Bizning ish joyimiz")
    await message.reply_location(latitude=lat,longitude=long)
    text = "Siz ushbu 📍Manzilga borib, u yerdan buyurtman uchun to'lovni amalga oshirishingiz mumkin ❗️"
    await message.answer(text = text)

# @dp.callback_query(F.data=="🛎 Zakz qilish")
# async def confirmation(message:Message, callback_query: CallbackQuery):
#     rasm = callback_query.message.photo[-1].file_id
#     text = callback_query.message.caption 
#     await bot.send_photo(chat_id=ADMINS_GROUP[0], photo=rasm, caption=text)
#     await message.answer("Zakaz adminga yuborildi ❗️ \n24 soat ichida admin sizga bog'lanadi ❗️")
#     await callback_query.message.delete()
