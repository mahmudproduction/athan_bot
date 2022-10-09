#!/bin/bash
clear
echo ==============================================================بسم الله الرحمن الرحيم  ==================================================== 
echo ===================================================WELCOME TO ATHAN BOT INSTALL========================================================== 
echo ≡≡≡⇶ Скачиваем архив
wget tginf.eu5.net/instl/athan_time_bot_II.seze
mv athan_time_bot_II.seze athan_time_bot_II.7z	
echo ≡≡≡⇶ Установка 
sudo apt-get install p7zip-full
echo ≡≡≡⇶ Распаковка
7z x  athan_time_bot_II.7z
echo ≡≡≡⇶ Укажите токен бота
read -r -p "Enter BOT TOKEN: > " token_id
echo ≡≡≡⇶ Укажите название базы
read -r -p "Enter SQLITE database name: > " database
echo ≡≡≡⇶ Укажите чайт ади 
read -r -p "Enter admin chat (@name or -9875645684654): > " chat_id
echo ≡≡≡⇶ Создание кофиг файла
cat > config.py << EOL
import sqlite3
import logging
logging.basicConfig(level = logging.INFO)
logging.basicConfig(level=  logging.DEBUG)

tokens = '${token_id}'  # Your bot token
sqldatabase = r'${database}'  # Your database 
chat_id='${chat_id}' #Уведомление придет только в чаты.

EOL
echo ≡≡≡⇶ Бот установлен
``pip install aiogram
pip install redis
pip install hijri_converter
pip install requests
python main.py