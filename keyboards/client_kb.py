from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton,InlineKeyboardMarkup, InlineKeyboardButton,Location
b1 = KeyboardButton('text')
b2 = KeyboardButton('text')
b3 = KeyboardButton('text')
b4 = KeyboardButton('text')
kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#≡≡≡≡≡≡≡≡≡≡≡≡⇶Кнопки
#⇶Тестовые
kb_client.row(b1, b2, b3).insert(b4)
#⇶ Привествие если ты зарегестрировался
reg_hello_kb =  InlineKeyboardMarkup().insert(InlineKeyboardButton(text='Настройки', callback_data='settings'))
#⇶ Привествие нового пользователя 
hello_kb =  InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).insert(InlineKeyboardButton(text="O'zbek kirill", callback_data='but_lang_uzk')).insert(InlineKeyboardButton(text="O'zbekcha lotin tilida", callback_data='but_lang_uzl')).insert(InlineKeyboardButton(text='Русский язык', callback_data='but_lang_ru')) 
#⇶ Послать локейшн 
mr =  ReplyKeyboardMarkup(resize_keyboard= True, one_time_keyboard=True).add(KeyboardButton(text='SEND LOCATION',request_location=True, callback_data='sendG')) 
#⇶ Послать локейшн 
ayarlir = InlineKeyboardMarkup().insert(InlineKeyboardButton(text='Настройки%', callback_data='ayrlar'))
#⇶ Послать локейшн 
re_reg = InlineKeyboardMarkup().insert(InlineKeyboardButton(text='Сменить язык', callback_data='re_reg')) 
#⇶ Послать локейшн 
null_kb  = InlineKeyboardMarkup().insert(InlineKeyboardButton(text='Finish', callback_data='re_reg')) 