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
    await bot.send_message(chat_id="@for_dvmn", text='It is text')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except Exception as e:
        print(f'Ошибка во время main(): {e}')