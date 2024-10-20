from loader import bot,db,dp,ADMINS
from aiogram.types import Message
from aiogram.filters import Command
from filters.admin import IsBotAdminFilter
from states.reklama import Adverts
from aiogram.fsm.context import FSMContext #new
from keyboard_buttons.default import admin_keyboard
import time 
from aiogram import F
from states.all_states import SalatAdd



@dp.message(Command("admin"),IsBotAdminFilter(ADMINS))
async def is_admin(message:Message):
    await message.answer(text="Admin menu",reply_markup=admin_keyboard.admin_button)


@dp.message(F.text=="Foydalanuvchilar soni",IsBotAdminFilter(ADMINS))
async def users_count(message:Message):
    counts = db.count_users()
    text = f"Botimizda {counts[0]} ta foydalanuvchi bor"
    await message.answer(text=text)

@dp.message(F.text=="Reklama yuborish",IsBotAdminFilter(ADMINS))
async def advert_dp(message:Message,state:FSMContext):
    await state.set_state(Adverts.adverts)
    await message.answer(text="Reklama yuborishingiz mumkin !")

@dp.message(Adverts.adverts)
async def send_advert(message:Message,state:FSMContext):
    
    message_id = message.message_id
    from_chat_id = message.from_user.id
    users = db.all_users_id()
    count = 0
    for user in users:
        try:
            await bot.copy_message(chat_id=user[0],from_chat_id=from_chat_id,message_id=message_id)
            count += 1
        except:
            pass
        time.sleep(0.01)
    
    await message.answer(f"Reklama {count}ta foydalanuvchiga yuborildi")
    await state.clear()

@dp.message(F.text=="Add Salat",IsBotAdminFilter(ADMINS))
async def add_salat(message:Message, state:FSMContext):
    await message.answer(text="Salat nomini kiriting!")
    await state.set_state(SalatAdd.name)

@dp.message(SalatAdd.name)
async def salat_name(message:Message, state:FSMContext):
    name = message.text

    await state.update_data(name = name)
    await message.answer(text="Salat rasmini kiriting!")
    await state.set_state(SalatAdd.img)

@dp.message(SalatAdd.img)
async def salat_img(message:Message,state:FSMContext):
    photo = message.photo[-1].file_id
    await state.update_data(photo = photo)

    await message.answer(text="Salat haqida ma'lumot kiriting!")
    await state.set_state(SalatAdd.description) 


@dp.message(SalatAdd.description)
async def salat_description(message:Message,state:FSMContext):

    data = await state.get_data() 

    name = data.get("name")
    photo = data.get("photo")
    description = message.text

    db.add_salat(name, photo, description)

    await message.answer(text="Salat ma'lumotlari muvaffaqiyatli saqlandi!")

    await state.clear()