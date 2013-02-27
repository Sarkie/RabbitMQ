#!/usr/bin/env python
import pika
import datetime

connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!' + str(datetime.datetime.now()))
print " [x] Sent 'Hello World!'" + str(datetime.datetime.now())
connection.close()
