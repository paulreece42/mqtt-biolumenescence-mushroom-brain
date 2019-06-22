#!/usr/bin/python

import paho.mqtt.client as mqtt
import time
import random
import os

broker_address=os.environ['BROKER']
client = mqtt.Client()
client.connect(broker_address)

SHROOMS=['shroom01']

while True:
    time.sleep(random.randint(30,60))
    for shroom in SHROOMS:
        client.publish("garden/" + shroom + "/set", "{'brightness': %d, 'color': {'r': 0,'g': %d, 'b': 255},'transition': %d,'state': 'ON'}" % (random.randint(15,30),
            random.randint(200,255), random.randint(10,25)))
    time.sleep(random.randint(30,60))
    for shroom in SHROOMS:
        client.publish("garden/" + shroom + "/set", "{'brightness': %d, 'color': {'r': 0,'g': %d, 'b': 255},'transition': %d,'state': 'ON'}" % (random.randint(15,30),
            random.randint(0,25), random.randint(10,25)))

