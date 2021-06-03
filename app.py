import os
import handlers
from aiogram import executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from data import config
from data.strings import start_message, bot_command
from loader import dp, db, bot
import filters
import logging


filters.setup(dp)


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    """Приветственное сообщение"""
    await message.answer(start_message)
    await message.answer(bot_command)


@dp.message_handler(content_types=['text'])
async def get_command_bot(message: types.Message):
    if message.text.lower() == 'команды':
        await message.answer(bot_command)
    else:
        await message.answer('Я тебя не понимаю!!!')


async def on_startup(dp):
    logging.basicConfig(level=logging.INFO)
    db.create_tables()

    await bot.delete_webhook()


async def on_shutdown():
    logging.warning("Shutting down..")
    await bot.delete_webhook()
    await dp.storage.close()
    await dp.storage.wait_closed()
    logging.warning("Bot down")


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=False)
