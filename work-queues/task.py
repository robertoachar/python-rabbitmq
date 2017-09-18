#!/usr/bin/env python

import pika

# connect to RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

# create a channel
channel = connection.channel()

# assert a queue (durable=True)
# make sure that RabbitMQ will never lose our queue.
channel.queue_declare(queue='task', durable=True)

# send a task
channel.basic_publish(exchange='',
                      routing_key='task',
                      body='New task',
                      properties=pika.BasicProperties(
                          delivery_mode=2  # make task persistent
                      ))
# show confirmation
print('Task sent')

# close connection
connection.close()
