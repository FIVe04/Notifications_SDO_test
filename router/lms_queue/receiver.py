import pika, sys, os, json

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='from_lms')

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")
        router(body, channel)


    channel.basic_consume(queue='from_lms', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

def router(data_received, channel):
    data = json.loads(data_received)
    print(data["id"], data["text"])
    match data["social_media"]:
        case "tg":
            send_to_tg(json.dumps(data), channel)
        case "vk":
            send_to_vk(json.dumps(data), channel)

def send_to_tg(data, channel):
    channel.queue_declare(queue='to_tg')
    channel.basic_publish(exchange='', routing_key='to_tg', body=data)
    print(f" [x] Sent to tg {data}")

def send_to_vk(data, channel):
    channel.queue_declare(queue='to_vk')
    channel.basic_publish(exchange='', routing_key='to_vk', body=data)
    print(f" [x] Sent to vk {data}")



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)