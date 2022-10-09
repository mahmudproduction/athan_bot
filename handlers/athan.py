from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton,ReplyKeyboardMarkup,KeyboardButton,Location 
from aiogram import types,executor #загрузки библиотеки для работы бота на основе аиограмм
from datetime import timedelta #загрузки библиотеки тоже работа с вренем
from create_bot import dp,bot #Загрузка файла подключения к боту через бот токен 
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from hijri_converter import Hijri, Gregorian
from keyboards import kb_client,reg_hello_kb,hello_kb,mr,re_reg,ayarlir
import time,datetime #загрузки библиотеки для работы с временем
 # check_user
import logging
import sys 
#≡≡≡≡≡≡⇶ Мои библиотеки, модули
import utils.sqlitedatabaseconnect  as ut_sql #Модуль все что связанно с базой данных Впоследствии вообще удалить конфиг файл из исполняемого
import utils.athantime as ath_time
import utils.geo as geogea  
import utils.tools as tools

#≡≡≡≡≡≡⇶ 
import config #загрузки конфиг файла
#≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⇶ Старт основных переменных
#≡≡≡≡≡≡⇶ Глобальная переменная авторизован ли человек тоже скоро удалить
global check_user 
check_user = None
global language
language = None
#≡≡≡≡≡≡⇶Логирование
logging.basicConfig(level=logging.INFO)

#Данные ФСМ машины
# States
class Form(StatesGroup):
    u_id = State()    # Добовляем в базу айди пользователя
    name = State()    # Имя
    u_name = State()  # Если есть имя пользователя
    lang = State()    # Выбранный им язык

#≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⇶  
# async def cmd_helloS(message: types.Message,state: FSMContext):
#     hkb =ZZ
#     await message.reply("",reply_markup = hkb) 

#≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⇶ Команда /start
async def cmd_hello(message: types.Message,state: FSMContext):
    ut_sql.hello(message.chat.id, message.from_user.first_name, message.chat.username,'Started bot', ath_time.today_epohe)
    # fop = tools.sobak(message.from_user.username )
    if not message.from_user.username:
        fop ="-"
    else:
        fop="@"
    
    #Проверяем есть ли пользователь в базе
    check_user = ut_sql.check_user(message.chat.id)
    #     print  
    if check_user == None or check_user[8] == 0: #Если нет стартуем машину с начала
          
        await message.reply(f"Приветсвие - имя, фамилия, если есть имя пользователя и айди.{fop}{message.from_user.username or message.from_user.id} На одном из языков, обявляем о регистрации(дата база пользователей как ты хотел брат) и записываем данные в базу.\n Советую сделать приветсвие сразу на двух языках(русский, и родной в варианте латинском и кирилице", reply_markup = hello_kb, parse_mode="HTML")
    
        
        # logging.info(f'Новый пользователь ~{message.chat.first_name }({message.from_user.username or message.from_user.id})~ включил бота')
        # NEX consrtante
        await Form.name.set()
        # Добавим в базу @Actions@ что новый пользователь  нажал на старт
  
    else: #Если есть тут по твоему желанию, или сразу же перебрасываем его на азан, или же еще что то

        if not message.from_user.username:
            SOBAKA = "Id:"
        else:
            SOBAKA = "@"  
        logging.info(f"Уже зарегестрированный ~{message.chat.first_name }({SOBAKA}{message.from_user.username or message.from_user.id})~нажал старт")
         
        await message.answer(f"{message.chat.first_name } В настройках выбран язык: {check_user[5]}. ",reply_markup=ayarlir)
       
            
  
#≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⇶ Выбор языка   
    

#≡≡≡≡≡≡≡≡≡≡≡≡≡⇶ Выбор языка Узбекский кирилица
async def lang_uzk (callback: types.CallbackQuery, state: FSMContext):
     
    await callback.message.delete() 
    async with state.proxy() as data:
        data['u_id'] = callback.from_user.id
        data['name'] = callback.from_user.first_name
        data['u_name'] = callback.from_user.username
        data['lang'] =  'uzk'
         
        await callback.message.answer(f"({callback.from_user.id}) Кирил Узбек Тили сечдиниз\nНачинаем собирать информацию + добовляем в базу язык на котором пользователь хочет чтоб бот с ним обращался.\n{callback.from_user.id}\n{callback.from_user.first_name}\n{callback.from_user.username}\ndata['lang'] = uzk\n И главное спрашиваем  у него  локацию.",reply_markup=mr)
        await state.finish() 
    ut_sql.hello(callback.message.chat.id, data['name'], callback.message.chat.username,'Selected Uzbek lang kirilyc', ath_time.today_epohe)
          
#≡≡≡≡≡≡≡≡≡≡≡≡≡⇶ Выбор языка Узбекский латиница
async def lang_uzl (callback: types.CallbackQuery, state: FSMContext):
     
    await callback.message.delete() 
    async with state.proxy() as data:
        data['u_id'] = callback.from_user.id
        data['name'] = callback.from_user.first_name
        data['u_name'] = callback.from_user.username
        data['lang'] =  'uzl'
         
        await callback.message.answer(f"({callback.from_user.id}) Latin O'zbek tili secdiniz\nНачинаем собирать информацию + добовляем в базу язык на котором пользователь хочет чтоб бот с ним обращался.\n{callback.from_user.id}\n{callback.from_user.first_name}\n{callback.from_user.username}\ndata['lang']= uzl\n И главное спрашиваем  у него  локацию.",reply_markup=mr)
        await state.finish()
    ut_sql.hello(callback.message.chat.id, data['name'], callback.message.chat.username,'Selected Uzbek lang in latin', ath_time.today_epohe)
#≡≡≡≡≡≡≡≡≡≡≡≡≡⇶ Выбор языка русский
async def lang_ru(callback: types.CallbackQuery, state: FSMContext):
   await callback.message.delete() 
   async with state.proxy() as data:
        data['u_id'] = callback.from_user.id
        data['name'] = callback.from_user.first_name
        data['u_name'] = callback.from_user.username
        data['lang'] =  'ru'
        ut_sql.hello(callback.message.chat.id, data['name'], callback.message.chat.username,'Selected russian lang ', ath_time.today_epohe)

        await callback.message.answer(f"({callback.from_user.id}) Вы выбрали русский язык\nНачинаем собирать информацию + добовляем в базу язык на котором пользователь хочет чтоб бот с ним обращался.\n{callback.from_user.id}\n{callback.from_user.first_name}\n{callback.from_user.username}\ndata['lang'] = ru\nИ главное спрашиваем  у него  локацию.",reply_markup=mr)
        await state.finish()
    

#≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⇶ Подача Времени молитв на два дня 
async def loc_handler(message: types.Message, state: FSMContext):
    ut_sql.hello(message.chat.id, message.from_user.first_name, message.chat.username,'Send their location', ath_time.today_epohe)
#≡≡≡≡≡≡≡≡≡≡≡≡≡⇶  Мультиязычность включаем
    async with state.proxy() as data: # Берем данные из машины!
        print ('------------')
    attfun=ath_time.getathan(message.location.latitude,message.location.longitude, data['lang'])
    await bot.send_message(message.chat.id,f"Широта:{message.location.longitude}\nДолгота:{message.location.latitude}\n{attfun}",parse_mode="HTML") # 
#≡≡≡≡≡≡≡≡≡≡≡≡≡⇶ Добовляем нового пользователя в базу 
    ut_sql.add_usr( message.from_user.first_name,\
                  message.from_user.last_name,\
                  message.chat.id,\
                  message.chat.username,\
                  data['lang'],\
                  message.location.latitude,\
                  message.location.longitude,\
                  ath_time.today_epohe)
   
    logging.info(f"Новый пользователь ~{message.chat.first_name }({message.chat.id})~ добавлен в базу данных.")
#≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⇶
async def ayariki(callback: types.CallbackQuery):
    await callback.message.delete() 
    logging.info(f"Пользователь ~{callback.from_user.first_name }({callback.from_user.id})~ зaщел в настройки.")
    check_user = ut_sql.check_user(callback.from_user.id) 
    await callback.message.answer(f'N/S: {check_user[1]}{check_user[2]}\nUsername:@{check_user[4]}\nLang:{check_user[5]}',reply_markup=re_reg)
async def usr_is_null(callback:types.CallbackQuery):
    await callback.message.delete() 
    ut_sql.user_setting_null(callback.from_user.id)   
    logging.info(f"Пользователь ~{callback.from_user.first_name }({callback.from_user.id})~ обнулил настройки.")
    await callback.message.answer('/start')

def register_hendlers_athan(dp: dp):
    dp.register_message_handler(cmd_hello, commands=['start', 'help', 'старт'], commands_prefix='/' )
    # dp.register_message_handler(cmd_stop, commands=['stop'], commands_prefix='/')
     
    dp.register_callback_query_handler(lang_uzk, text= "but_lang_uzk", state=Form.name ) 
    dp.register_callback_query_handler(lang_uzl, text= "but_lang_uzl", state=Form.name )
    dp.register_callback_query_handler(lang_ru,  text= "but_lang_ru", state=Form.name)
    dp.register_message_handler(loc_handler,content_types=['location'])
    dp.register_callback_query_handler(ayariki, text="ayrlar")
    dp.register_callback_query_handler(usr_is_null, text="re_reg")
    # dp.register_callback_query_handler(reg_athan, text="wh_athan")
    # dp.register_callback_query_handler(settings_auth, text="settings") 