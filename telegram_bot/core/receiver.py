import sys, os
import aio_pika, json
import asyncio
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from main import bot


async def recieve_from_queue():
     connection = await aio_pika.connect_robust(
         host="localhost"
     )
     queue_name = "to_tg"
     async with connection:
         channel = await connection.channel()

         await channel.set_qos(prefetch_count=10)
         queue = await channel.declare_queue(queue_name)

         async with queue.iterator() as queue_iter:
             async for message in queue_iter:
                 async with message.process():
                     received_data = message.body.decode()
                     print(received_data)
                     data = json.loads(received_data)
                     await bot.send_message(data["id"], data["text"])


asyncio.run(recieve_from_queue())
