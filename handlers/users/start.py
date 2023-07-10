from aiogram import types

from aiogram.dispatcher.filters import CommandStart

from loader import dp




@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    await message.answer(f"Привет {name}")