import logging
from aiogram import Bot, Dispatcher, executor, types

TOKEN = 8385251365:AAHt1kt6eU2sReQ7VtAjzESSZBZiptejhJU

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("🎲 Привет! Нажми /roll чтобы бросить кубик")

@dp.message_handler(commands=["roll"])
async def roll(message: types.Message):
    dice = await message.answer_dice("🎲")
    await message.answer("Попробуй ещё раз!")

if __name__ == "__main__":
    executor.start_polling(dp)

