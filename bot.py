import aiogram
import os
import asyncio
from aiogram import Dispatcher, Bot, types
from aiogram.filters import CommandStart, Command
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.environ['TG_BOT_TOKEN'])
dp = Dispatcher()


@dp.message(CommandStart)
async def start_command(message: types.Message):
    caption = 'Изображение'
    link_url = "https://images.unsplash.com/photo-1481349518771-20055b2a7b24?q=80&w=939&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    await bot.send_photo(chat_id="@for_dvmn", photo=link_url, caption=caption)

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except Exception as e:
        print(f'Ошибка во время main(): {e}')