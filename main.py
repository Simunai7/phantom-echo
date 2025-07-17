
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging
import os

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Set this in Railway ENV VARS

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help', 'pull'])
async def send_welcome(message: types.Message):
    await message.reply("👋 MunaiBot v1.0 activated. What shall we deal today?")

@dp.message_handler()
async def echo_all(message: types.Message):
    await message.reply("🔁 Munai echoes: " + message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
