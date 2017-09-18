#!/usr/bin/env python

import pika

# define a callback


def callback(ch, method, properties, body):
    print("Message received %r" % body)


# connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# create a channel
channel = connection.channel()

# assert a queue
channel.queue_declare(queue='hello', durable=False)

# subscribe to a queue
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print('Waiting for messages...')

# wait for messages
channel.start_consuming()
