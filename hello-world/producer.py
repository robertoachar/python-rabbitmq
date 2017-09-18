#!/usr/bin/env python

import pika

# connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# create a channel
channel = connection.channel()

# assert a queue
channel.queue_declare(queue='hello', durable=False)

# send a message
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World')
# show confirmation
print('Message sent')

# close connection
connection.close()
