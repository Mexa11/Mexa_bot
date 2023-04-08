from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "5840023460:AAFQlsIzVHr_W7eUu93dtblrdP_tsZHAbyU"

bot = Bot(token=TOKEN)

dp = Dispatcher(bot=bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)




#
# @dp.message_handler(commands=['start'])
# async def start_command(message: types.Message):
#     await message.reply(text="Assalomu aleykum botimizga xush kelibsiz")
@dp.message_handler(Text(equals="commands"))
async def get_commands(message: types.Message):
    text = """/start - create a new bot
              /mybots - edit your bots [beta]
    """
    await message.answer(text=text)


# async def echo_answer(message: types.Message):
#     await message.answer(text=message.text.upper())


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)
