from aiogram import Bot, types
from aiogram.types import InputTextMessageContent,InlineQueryResultArticle
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from create_bot import dp, bot
import logging
import hashlib
import config
import sqlite3
import time

# 🟢convert start..

logging.basicConfig(level = logging.INFO)
logging.basicConfig(level=  logging.DEBUG)



 
async def on_startup(_):
    #≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⇶Оповещения бота о его включении в нужный  тебе чат
    bot_info = (await bot.get_me())
    local_time = time.ctime()
    hellos = (f" '{bot_info.first_name}[@{bot_info.username}]' <u>turn on in </u> <b>{local_time}</b>  ")
    await bot.send_message(config.chat_id ,  text= hellos , parse_mode="HTML")
    #≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⇶ Cоздание таблицы и коннект
    try:
        conn = sqlite3.connect(config.sqldatabase) #За соединение будет отвечать переменная conn.Если файл уже существует, то функция connect осуществит подключение к нему.Путь должен прописоваться от корня. Узнать можно в настройках
        cur = conn.cursor()#После создания объекта соединения с базой данных нужно создать объект cursor
        #Теперь Создаем таблицы базы данных 
        cur.execute("""CREATE TABLE IF NOT EXISTS actions(
           id INTEGER   NOT NULL ,
           u_id  INTEGER,
           fname  TEXT,
           u_uname  TEXT,
           action TEXT,
           curtime INTEGER,
           PRIMARY KEY(id AUTOINCREMENT));
           """) 
        cur.execute("""CREATE TABLE IF NOT EXISTS users(
           id INTEGER   NOT NULL  ,
           fname TEXT,
           lname TEXT,
           u_id  INTEGER ,
           u_uname TEXT,
           u_lang  TEXT,
           latitude TEXT,
           longitude TEXT,
           status INTEGER,
           curtime INTEGER,
           PRIMARY KEY(id AUTOINCREMENT));
           """) 
        logging.info("Created database: OK")
    except Exception as err:
        logging.warning(err)
    else:
        logging.info("Sqlite database working: Ok ")
    
#≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⇶КЛИЕНТСКАЯ ЧАСТЬ
from handlers import  admin,athan,reg                     
# client.register_hendlers_client(dp)
admin.register_hendlers_admin(dp)
athan.register_hendlers_athan(dp)
 
 

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup) #skip_updates=True,