# async def cancel_handler(message: types.Message, state: FSMContext):
#     """
#     Allow user to cancel any action
#     """
#     current_state = await state.get_state()
#     if current_state is None:
#         return

#     logging.info('Cancelling state %r', current_state)
#     # Cancel state and inform user about it
#     await state.finish()
#     # And remove keyboard (just in case)
#     await message.reply('Cancelled.', reply_markup=types.ReplyKeyboardRemove())
# async def geo(message: types.Message):
# 	#Послать Геопозицю кнопка
#     mr =  ReplyKeyboardMarkup(resize_keyboard= True).add(KeyboardButton(text='SEND LOCATION',request_location=True, callback_data='sendG')) 
#     # Поздороваться с человеком
#     print ({message.from_user.first_name},{message.from_user.last_name},{message.chat.id},{message.chat.username} ) 
#     # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#     # await bot.send_message(message.chat.id, f"{config.hello}({message.chat.title or message.chat.id}){message.from_user.first_name} ! ", reply_markup = mr, parse_mode="HTML") # 
#     await bot.send_message(message.chat.id, f"{message.from_user.first_name},{RUSSIAN['start']} ! ", reply_markup = mr, parse_mode="HTML") # 
#     # Добавим в базу что он нажал на старт
#     user = (None,message.from_user.first_name,message.from_user.last_name,message.chat.id,message.chat.username,None,None,None,'Started bot')
#     # user = (None, '{message.from_user.first_name}', '{message.from_user.last_name}', '{message.chat.id}','{message.chat.username}','None','None','None','Started bot')
#     cur.execute("INSERT INTO actions VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);", user)
#     conn.commit()
# async def maps(message: types.Message):
#     print ("message.text")  
