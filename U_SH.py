from aiogram import types, executor, Bot, Dispatcher
from configuration import TOKEN
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

storage = MemoryStorage()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)
rkb = ReplyKeyboardMarkup(resize_keyboard=True)
rkb.add(KeyboardButton("/create"))


class Form(StatesGroup):
    name = State()
    age = State()
    photo = State()


async def on_startup(_):
    print('Botimiz ishlayapti')


@dp.message_handler(commands=['start'], state="*")
async def start_cmd(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer("Assalomu aleykum botimizga xush kelibsiz! "
                         "Ariza to'ldirish uchun /create tugmasidan foydalaning", reply_markup=rkb)


@dp.message_handler(commands=['create'])
async def start_reg(message: types.Message):
    await message.answer("Registratsiya boshlandi")
    await message.answer("Ismingizni kiriting!")
    await Form.name.set()


@dp.message_handler(state=Form.name)
async def set_name(message: types.Message, state: FSMContext):
    ism = message.text
    await state.update_data(ism=ism)

    await message.answer("Yoshingizni kiriting!")
    await  Form.age.set()


@dp.message_handler(state=Form.age)
async def set_age(message: types.Message, state: FSMContext):
    yoshi = message.text
    if not yoshi.isdigit():
        await message.answer("Yosh faqat raqamlardan iborat bo'lishi kerak!")
    else:
        await state.update_data(yoshi=yoshi)
        await message.answer("Rasmingizni jo'nating")
        await Form.photo.set()


@dp.message_handler(state=Form.photo, content_types=['photo'])
async def set_photo(message: types.Message, state: FSMContext):
    photo = message.photo[-1].file_id
    await state.update_data(photo=photo)

    data = await state.get_data()

    await message.answer_photo(photo=photo, caption=f"Foydalanauvchi ismi: {data['ism']},"
                                                    f"Foydalanuvchi yoshi: {data['yoshi']}")
    await state.reset_state()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
