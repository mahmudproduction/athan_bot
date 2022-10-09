from create_bot import dp,bot #Загрузка файла подключения к боту через бот токен 
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton,ReplyKeyboardMarkup,KeyboardButton,Location 
from aiogram import types,executor #загрузки библиотеки для работы бота на основе аиограмм
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
 
async def other(callback: types.CallbackQuery):
    print ("other")


def register_hendlers_reg(dp: dp):
    dp.register_callback_query_handler(other, text="under")