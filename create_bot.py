from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage 
import config
import redis
#CONFIG 
LOG_PRIVATE_PUBLIC='@sheyxbotlog'
storage = MemoryStorage()
# storage = redis.Redis(host='localhost', port=6379, db=0ь)
bot = Bot(token = config.tokens)
dp = Dispatcher(bot,storage = storage)
 