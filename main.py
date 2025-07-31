import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = 'ضع التوكن الخاص بك هنا'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("أهلا بك في بوت الإحالة 🎉")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
