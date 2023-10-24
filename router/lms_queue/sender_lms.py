import pika
import json

data1 = {
    "id": 770746159,
    "social_media": "tg",
    "text": "Открыт новый урок в телегу"
}

data2 = {
    "id": 304314711,
    "social_media": "vk",
    "text": "Открыт новый урок в вк"
}

# Устанавливаем соединение с сервером
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Создание очереди
channel.queue_declare(queue='from_lms')

# Отправка сообщения в точку обмена exchange
channel.basic_publish(exchange='', routing_key='from_lms', body=json.dumps(data1))
print(f" [x] Sent {json.dumps(data1)}")

# Отправка сообщения в точку обмена exchange
channel.basic_publish(exchange='', routing_key='from_lms', body=json.dumps(data2))
print(f" [x] Sent {json.dumps(data2)}")

connection.close()
