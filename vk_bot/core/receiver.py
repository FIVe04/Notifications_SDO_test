import sys, os
import aio_pika, json
import asyncio
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from main import bot


async def recieve_from_queue():
     connection = await aio_pika.connect_robust(
         host="localhost"
     )
     queue_name = "to_vk"
     async with connection:
         channel = await connection.channel()

         await channel.set_qos(prefetch_count=10)
         queue = await channel.declare_queue(queue_name)

         async with queue.iterator() as queue_iter:
             async for message in queue_iter:
                 async with message.process():
                     received_data = message.body.decode()
                     print('!'*100)
                     print(received_data)
                     print('!' * 100)
                     data = json.loads(received_data)
                     print('1'*100)
                     await bot.api.messages.send(peer_id=data["id"], random_id=0, message=data["text"])


asyncio.run(recieve_from_queue())
