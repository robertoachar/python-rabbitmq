#!/usr/bin/env python

import pika


def callback(ch, method, properties, body):
    print("Task received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


# connect to RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

# create a channel
channel = connection.channel()

# assert a queue (durable=True)
# make sure that RabbitMQ will never lose our queue.
channel.queue_declare(queue='task', durable=True)

# This tells RabbitMQ not to give more than one task
# to a worker at a time
channel.basic_qos(prefetch_count=1)

# subscribe to a queue
channel.basic_consume(callback,
                      queue='task')

print('Waiting for tasks...')

# wait for tasks
channel.start_consuming()
