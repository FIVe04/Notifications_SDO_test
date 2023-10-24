from vkbottle.bot import Bot, Message
from config import VK_TOKEN
import asyncio
bot = Bot(VK_TOKEN)


@bot.on.private_message(text="<msg>")
async def echo_answer(message: Message, msg):
    users_info = await bot.api.users.get(message.from_id)
    print('-'*100)
    print(users_info[0].id)
    print('-' * 100)
    await bot.api.messages.send(peer_id=users_info[0].id, random_id=0, message="Привет!")

if __name__ == "__main__":
    asyncio.run(bot.run_forever())