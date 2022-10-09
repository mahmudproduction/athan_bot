from hijri_converter import Hijri, Gregorian
from datetime import timedelta 
import time,datetime 
import requests #загрузки библиотеки для парсига сайта
import logging
#≡≡≡≡≡≡⇶ Получения в юникс время сегодняшнего дня
today = datetime.datetime.now()
today_epohe  = int(time.mktime(today.timetuple()))
logging.info(f"Gregorian date \"Now\": {today} ")
logging.info(f"Gregorian date EPOHE \"Now\": {today_epohe} ")
                    
#≡≡≡≡≡≡⇶ 


#≡≡≡≡≡≡⇶ Создание уникс эпоха времени +1 lol = time.mktime(lil.timetuple())
date = today + datetime.timedelta(days=1)
tomorrow_epohe = date.date()
logging.info(f"Gregorian date \"Tomorrow\": {date} ")
logging.info(f"Gregorian date wihout hour-min-sec \"Tomorrow\": {tomorrow_epohe} ")


#≡≡≡≡≡≡⇶Получение Даты по хиджри
hjdate_month = Hijri.today().month_name()
hjdate_today  = Hijri.today().datetuple()
hjdate = f'{hjdate_today[2]}-{hjdate_month}-{hjdate_today[0]}'

print("========================================\n Hijri date  \"Now\":",hjdate,"\n========================================") 

#≡≡≡≡≡≡⇶ Функция получения. времен на два дня
def getathan(ml_la,ml_lo,langs):
    logging.info(f'Функции пошли данные {ml_la,ml_lo,langs}')
	# Создание сылки для парсинга(сегодняшний день)
    res_url = f'https://api.aladhan.com/v1/timings/{today_epohe}?latitude={ml_la}&longitude={ml_lo}&method=99&methodSettings=17,1,18&tune=0,0,0,4,0,0,1,0,0&school=1&adjustment=1'
    # Создание сылки для парсинга(на завтра) 
    res_url_t = f'https://api.aladhan.com/v1/timings/{tomorrow_epohe}?latitude={ml_la}&longitude={ml_lo}&method=99&methodSettings=17,1,18&tune=0,0,0,4,0,0,1,0,0&school=1&adjustment=1'
    # Start парсинга на сегодняшний день
    resp = requests.get(res_url, params = {'address': 'London'})
    # Start парсинга на завтра
    resp_t = requests.get(res_url_t, params = {'address': 'London'})
    #Выборка из полученных  данных времена молитв на сегодня . Тебе не нужно было все, но я сделал все что выдавал запрос
    # alls = resp.json() 
    # bids = resp.json()['data']['timings']  
    Asr =  resp.json()['data']['timings']['Asr']
    Dhuhr =  resp.json()['data']['timings']['Dhuhr']
    Fajr =  resp.json()['data']['timings']['Fajr']
    Imsak =  resp.json()['data']['timings']['Imsak']
    Isha =  resp.json()['data']['timings']['Isha']
    Maghrib =  resp.json()['data']['timings']['Maghrib']
    Midnight =  resp.json()['data']['timings']['Midnight']
    Sunrise =  resp.json()['data']['timings']['Sunrise']
    Sunset =  resp.json()['data']['timings']['Sunset']
    #Выборка из полученных  данных времена молитв на завтра .
    Y_Asr = resp_t.json()['data']['timings']['Asr']
    Y_Dhuhr = resp_t.json()['data']['timings']['Dhuhr']
    Y_Fajr = resp_t.json()['data']['timings']['Fajr']
    Y_Imsak = resp_t.json()['data']['timings']['Imsak']
    Y_Isha = resp_t.json()['data']['timings']['Isha']
    Y_Maghrib = resp_t.json()['data']['timings']['Maghrib']
    Y_Midnight = resp_t.json()['data']['timings']['Midnight']
    Y_Sunrise = resp_t.json()['data']['timings']['Sunrise']
    Y_Sunset = resp_t.json()['data']['timings']['Sunset']

    if langs== 'ru':
        logging.info('Отпраленны данные на русском языке')
        answ = f"""
                    <b>Today {today.day}-{today.month}-{today.year}</b> 
                        <i>Hijri date{hjdate}</i>                          
                         ⌜-Фаджр = {Fajr}                          
                         |-Имсак = {Imsak}                         
                         |-Восход = {Sunrise}                         
                         |-Зухр = {Dhuhr}                      
                         |-Аср = {Asr}                           
                         |-Магриб = {Maghrib}                        
                         |-Закат = {Sunset}   
                         |-Иша = {Isha}                        
                         ∟-Полночь = {Midnight}                         
                    <b>Tomorrow {date.day}-{date.month}-{date.year}</b> 
                         ⌜-Фаджр = {Y_Fajr}                         
                         |-Имсак = {Y_Imsak}                         
                         |-Восход = {Y_Sunrise}                         
                         |-Зухр = {Y_Dhuhr}                         
                         |-Аср = {Y_Asr}                         
                         |-Магриб = {Y_Maghrib}                         
                         |-Закат = {Y_Sunset}  
                         |-Иша = {Y_Isha}                         
                         ∟-Полночь = {Y_Midnight}                         
                          """
    
    
    elif langs =='uzk':
            logging.info('Отпраленны данные на узбекском языке(кириллица)')
            answ = f"""Харитадаги жойда, бугун, {today.day}-{today.month}-{today.year}:
                         ({hjdate})
                         • Бомдод вақтининг кириши (cаҳарликда оғиз ёпиш): {Fajr} 
                         • Пешин: {Dhuhr}
                         • Аср: {Asr}
                         • Шом (ифторликда оғиз очиш): {Maghrib}
                         • Хуфтон: {Isha}
                         ➖➖➖➖➖➖➖
                         Эртага, 16-апрел:
                         • Cаҳарликда оғиз ёпиш: {Y_Imsak}
                         • Ифторликда оғиз очиш: {Y_Maghrib}
                         """ 
    elif langs =='uzl':
            logging.info('Отпраленны данные на узбекском языке(латиница)')
            answ = f"""Харитадаги жойда, бугун, {today.day}-{today.month}-{today.year}:
                         ({hjdate})
                         • Бомдод вақтининг кириши (cаҳарликда оғиз ёпиш): {Fajr} 
                         • Пешин: {Dhuhr}
                         • Аср: {Asr}
                         • Шом (ифторликда оғиз очиш): {Maghrib}
                         • Хуфтон: {Isha}
                         ➖➖➖➖➖➖➖
                         Эртага, 16-апрел:
                         • Cаҳарликда оғиз ёпиш: {Y_Imsak}
                         • Ифторликда оғиз очиш: {Y_Maghrib}
                         """ 
    sendansw = f"Широта:{ml_la}\nДолгота:{ml_lo}\n{answ}"
    return sendansw