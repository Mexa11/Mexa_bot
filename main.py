from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, \
    ReplyKeyboardMarkup, KeyboardButton

TOKEN = "5840023460:AAFQlsIzVHr_W7eUu93dtblrdP_tsZHAbyU"

bot = Bot(token=TOKEN)

dp = Dispatcher(bot=bot)

ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("❤️", callback_data="Like"), InlineKeyboardButton("💔", callback_data="dislike", )]
])
rkb = ReplyKeyboardMarkup(resize_keyboard=True)
rkb.add(KeyboardButton(text="/yordam"))
rkb.add(KeyboardButton(text="/start"))


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo="https://encrypted-tbn0.gstatic.com/images?q=tbn"
                               ":ANd9GcRgUNaoFwOOa3sOnMoc8CVUJ65bhS822etxVQ&usqp=CAU",
                         caption="Bu rasm sizga yoqdimi?",
                         reply_markup=rkb)


@dp.callback_query_handler(text="Like")
async def like_button(callback: types.CallbackQuery):
    await callback.answer("Sizga yoqdi😊")


@dp.callback_query_handler(text="dislike")
async def dislike_button(callback: types.CallbackQuery):
    await callback.answer("Sizga yoqmadi😔")


# @dp.message_handler(Text(equels="Location")
#     await bot.send_location(chat_id=message.from_user.id,
#                             latitude=)

@dp.message_handler(Text(equals="malumotlar"))
async def get_commands(message: types.Message):
    text = """/start - create a new bot
              /mybots - edit your bots [beta]
    """
    await message.answer(text=text)


# async def echo_answer(message: types.Message):
#     await message.answer(text=message.text.upper())


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)
