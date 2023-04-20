from aiogram import types, executor, Bot, Dispatcher
from States import storage
from configuration import TOKEN
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)
rkb = ReplyKeyboardMarkup(resize_keyboard=True)
rkb.add(KeyboardButton("/sherik_kerak"))


class Form(StatesGroup):
    name = State()
    job = State()
    phone_number = State()
    area = State()
    payment = State()
    time = State()
    the_goal = State()


async def on_startup(_):
    print("Bot chotki ishlayapti")


@dp.message_handler(commands=['start'], state="*")
async def start_cmd(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer("Assalomu aleykum botimizga xush kelibsiz! "
                         "Sizga sherik kerak bo'lsa  /sherik_kerak tugmasidan foydalaning", reply_markup=rkb)


@dp.message_handler(commands=['sherik_kerak'])
async def start_reg(message: types.Message):
    await message.answer("Sherik topish uchun ariza berish."
                         "Hozir sizga birnecha savollar beriladi. "
                         "Har biriga javob bering. "
                         "Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.")
    await message.answer("Ismingizni  kiriting!")
    await Form.name.set()


@dp.message_handler(state=Form.name)
async def set_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)

    await message.answer("📚Talab qilinadigan texnologiyalarni kiriting")
    await Form.job.set()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
