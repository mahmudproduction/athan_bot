from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton,ReplyKeyboardMarkup,KeyboardButton,Location 
from aiogram import types,executor #загрузки библиотеки для работы бота на основе аиограмм
from create_bot import dp,bot #Загрузка файла подключения к боту через бот токен
import sqlite3 #загрузки библиотеки для работы с базой
import config
#≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⇶ Рабочие переменные начало!
#≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⇶ Рабочие переменные конец! 

#≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⇶ Команда администратора
async def adm_cmd(message: types.Message): # 315389405
    print (message.chat.id)
    print (config.sqldatabase)
 
#Run handlers
def register_hendlers_admin(dp: dp):
   dp.register_message_handler(adm_cmd, commands=['adm'], commands_prefix='.' )