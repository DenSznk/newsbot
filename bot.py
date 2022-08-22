import json
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from url_header import TOKEN
import os
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['news'])
async def process_start_command(message: types.Message):
    with open('new_dict.json') as file:
        new_dict = json.load(file)

    for k, v in sorted(new_dict.items()):
        news = f"{v['post_time']}\n" \
               f"{v['url_post']}"

        await message.answer(news)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Hello!\nIm CryptoNewsBot enter command '/news' to get info")


if __name__ == '__main__':
    executor.start_polling(dp)
