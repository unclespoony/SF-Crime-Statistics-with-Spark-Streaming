import asyncio

from confluent_kafka import Consumer


async def consume(topic_name):
    consumer = Consumer({
        'bootstrap.servers': 'PLAINTEXT://localhost:9092',
        'group.id': 0,
    })

    consumer.subscribe([topic_name])

    while True:
        messages = consumer.consume(5, timeout=1)

        for message in messages:
            if message is None:
                print('No messages')
            elif message.error() is not None:
                print(f'Error encountered: {message.error()}')
            else:
                print(f'{message.value()})

        await asyncio.sleep(1)


if __name__ == '__main__':
    try:
        print("Starting Conusmer")
        asyncio.run(consume("sf.police.callsforsvc"))
    except Exception as ex:
        print(f'Consumer encountered the following error: {ex}')
