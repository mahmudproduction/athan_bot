from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton,ReplyKeyboardMarkup,KeyboardButton,Location 
from aiogram import types,executor #загрузки библиотеки для работы бота на основе аиограмм

async def other(message: types.Message):
    await bot.send_message(message.chat.id,f"Уважаемый кто то пожалуйста, пошлите мне ваше местоположение")



def register_hendlers_athan(dp: dp):
    dp.register_message_handler(cmd_hello)