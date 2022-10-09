\from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton,ReplyKeyboardMarkup,KeyboardButton,Location 
from aiogram import types,executor #загрузки библиотеки для работы бота на основе аиограмм
from datetime import timedelta #загрузки библиотеки тоже работа с вренем
from create_bot import dp,bot #Загрузка файла подключения к боту через бот токен 
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from hijri_converter import Hijri, Gregorian
import time,datetime #загрузки библиотеки для работы с временем
 
import logging
import sys 
#≡≡≡≡≡≡⇶ Мои библиотеки, модули
import utils.sqlitedatabaseconnect  as ut_sql #Модуль все что связанно с базой данных Впоследствии вообще удалить конфиг файл из исполняемого
import utils.athantime as ath_time
import utils.geo as geogea  
#≡≡≡≡≡≡⇶ 
import config #загрузки конфиг файла
#≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⇶ Старт основных переменных
#≡≡≡≡≡≡⇶ Глобальная переменная авторизован ли человек тоже скоро удалить
global check_user 
check_user = None
#≡≡≡≡≡≡⇶Логирование
logging.basicConfig(level=logging.INFO)
#≡≡≡≡≡≡⇶Кнопки, можно в принципе бросить в кофниг файл. Последнии дни Рамадана голова кругом идет уже)

mr =  ReplyKeyboardMarkup(resize_keyboard= True).add(KeyboardButton(text='SEND LOCATION',request_location=True, callback_data='sendG')) 

hello_kb =  InlineKeyboardMarkup().insert(InlineKeyboardButton(text='Азан', callback_data='wh_athan')).insert(InlineKeyboardButton(text='Коран', callback_data='wh_koran')).insert(InlineKeyboardButton(text='Хадисы', callback_data='wh_hadith')).insert(InlineKeyboardButton(text='Другое', callback_data='under')) 

  

#Данные ФСМ машины
# States
class Form(StatesGroup):
    u_id = State()    # Добовляем в базу айди пользователя
    name = State()    # Имя
    u_name = State()  # Если есть имя пользователя
    lang = State()    # Выбранный им язык

#≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⇶  
 


#≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⇶ Команда /start
async def cmd_hello(message: types.Message ):
    #Проверяем есть ли пользователь в базе
    check_user = ut_sql.check_user(message.chat.id)
    if check_user == None:
        print (" Включаем ФСМ машину")
        hello_kb =  InlineKeyboardMarkup().insert(InlineKeyboardButton(text="Язык,Тил,Til", callback_data='reg_new_user'))
        txtx  =  f"Ассаламу алейкум{message.from_user.first_name}({message.from_user.username or message.from_user.id}) Для выбора языка нажмите кнопку\nAssalomu alaykum{message.from_user.first_name}({message.from_user.username or message.from_user.id}) Til tanlash uchun tugmani bosing"
    else :
        txtx = "Старый юзер мясяляси"
    await message.reply(txtx,reply_markup=hello_kb)
       # if not message.from_user.username:
       #      SOBAKA = "Id:"
       #  else:
       #      SOBAKA = "@"  
       #  logging.info(f"~{message.chat.first_name }({SOBAKA}{message.from_user.username or message.from_user.id})~Уже зарегестрированный")
       
       #  await message.reply(f"В настройках пользователя выбран язык: {check_user[5]}\n \
       #                        Уже зарегестрированный пользователь может видеть тут что угодно.\
       #                        Я пока оставил кнопку показать, времена намазов на два \
       #                        можно просто кнопку чтоб показать времена азанов кстати можно календарь\
       #                         на месяц вперед",reply_markup=reg_hello_kb)
async def new_user(message: types.Message,state: FSMContext):
    select_lang_kb = InlineKeyboardMarkup().insert(InlineKeyboardButton(text="O'zbek kirill", callback_data='but_lang_uzk')).insert(InlineKeyboardButton(text="O'zbekcha lotin tilida", callback_data='but_lang_uzl')).insert(InlineKeyboardButton(text='Русский язык', callback_data='but_lang_ru')) 
    await message.reply(f"Please Selected your language", reply_markup = select_lang_kb, parse_mode="HTML")
    
        
        # logging.info(f'Новый пользователь ~{message.chat.first_name }({message.from_user.username or message.from_user.id})~ включил бота')
 
       
            
  
#≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⇶ Выбор языка   
    # NEX consrtante
    await Form.name.set()
    # Добавим в базу @Actions@ что новый пользователь  нажал на старт
    ut_sql.hello(message.chat.id, message.from_user.first_name, message.chat.username,'Started bot', ath_time.today_epohe)
  

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

#≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⇶
async def cmd_stop(message: types.Message): 
    print ('QUIT')
    # quit() 
    # sys.exit()    
def register_hendlers_athan(dp: dp):
    dp.register_message_handler(cmd_hello, commands=['start', 'help', 'старт'], commands_prefix='/' )
    dp.register_message_handler(new_user, text = "reg_new_user", state=Form.name)
    dp.register_message_handler(cmd_stop, commands=['stop'], commands_prefix='/')
    dp.register_callback_query_handler(lang_uzk, text= "but_lang_uzk", state=Form.name ) 
    dp.register_message_handler(loc_handler,content_types=['location'])