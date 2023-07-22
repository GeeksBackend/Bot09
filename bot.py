from aiogram import Bot, Dispatcher, types, executor
from config import token

bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer("Привет!")

@dp.message_handler(text='Как дела?')
async def whats_up(message:types.Message):
    await message.answer("Нормально, спасибо что спросил")

@dp.message_handler(commands='test')
async def test(message:types.Message):
    print(message)
    await message.reply(f"{message.from_user.full_name}")
    await message.answer_dice()
    await message.answer_location(40.519413, 72.802976)
    await message.answer_photo('https://static.tildacdn.com/tild3863-3635-4138-b133-613431396662/230124-237_2.jpg')

#{"message_id": 1278, "from": {"id": 731982105, "is_bot": false, "first_name": "Курманбек", "last_name": "Токторов", "username": "Toktorov2", "language_code": "ru"}, "chat": {"id": 731982105, "first_name": "Курманбек", "last_name": "Токторов", "username": "Toktorov2", "type": "private"}, "date": 1689796346, "text": "/test", "entities": [{"type": "bot_command", "offset": 0, "length": 5}]}

executor.start_polling(dp)