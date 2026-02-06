import asyncio
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("""Привет! 👋\n
        Я тестовый бот на aiogram.\n
        Напиши /help, чтобы узнать команды.""")


@dp.message(Command("help"))
async def help_handler(message: Message):
    await message.answer("""Доступные команды:\n
        /start — старт\n
        /help — помощь\n
        /echo — повторю твоё сообщение\n
        Или просто напиши любой текст 🙂"""
    )


@dp.message(Command("echo"))
async def echo_command_handler(message: Message):
    await message.answer("Напиши что-нибудь, я повторю 👇")


@dp.message(lambda message: message.text and not message.text.startswith("/"))
async def text_handler(message: Message):
    await message.answer(f"Ты написал: {message.text}")


@dp.message()
async def unknown_command_handler(message: Message):
    await message.answer("Я не знаю такую команду 🤷‍♂️ Напиши /help")



async def main():
    print("Bot started")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())