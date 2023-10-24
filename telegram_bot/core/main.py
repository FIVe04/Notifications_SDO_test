import config
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
import asyncio
import pika

bot = Bot(token = config.BOT_TOKEN)
dp = Dispatcher()

@dp.message(F.text == "/start")
async def cmd_start(message: Message):
    await message.answer("Привет!")
    print(message.from_user.id, message.from_user.first_name)


async def send_from_queue(tg_id, text):
    await bot.send_message(tg_id, text)


async def main():
    print("Started")
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types(), none_stop=True)
    

if __name__ == "__main__":
    asyncio.run(main())