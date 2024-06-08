from loader import dp
from aiogram import F
from aiogram.types import CallbackQuery, Message
from keyboard_buttons.default import keyboardbutton

@dp.callback_query(F.data=="🛎 Zakz qilish")
async def Uzs_usd(callback:CallbackQuery):
    await callback.answer("To'lov usuli")
    await callback.message("To'lov usuli",reply_markup=keyboardbutton.pay_button)
    await callback.message.delete()



