import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher import filters
from aiogram.utils import executor
import requests

API_TOKEN = '7877054403:AAEl3brZHLAExXFr2PXq9sfVxPR82_scZBI'
PROXY_URL = "http://user132581:schrvd@45.88.15.215:5085" # прокси, без них нейросеть не работает на территории РФ

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN, proxy=PROXY_URL)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот, который может помочь тебе общаться с нейросетью. Напиши мне что-нибудь!")

# Обработчик текстовых сообщений
@dp.message_handler()
async def handle_message(message: types.Message):
    url = "https://tarotoo.com/wp-json/openai/v1/chat-message"
    
    headers = {
        'accept': '*/*',
        'content-type': 'application/json',
    }

    data = {
        "messages": [
            {"role": "user", "content": message.text}
        ],
        "currentSiteLang": "en"
    }

    try:
        response = requests.post(url, headers=headers, json=data, proxies={"http": PROXY_URL, "https": PROXY_URL})
        response_data = response.json()
        print(response_data)
        reply = response_data.get('content', 'Извините, я не смог получить ответ от нейросети.')
    except Exception as e:
        reply = f"Произошла ошибка: {str(e)}"

    await message.reply(reply)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True) 