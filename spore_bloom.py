#!/usr/bin/python

import paho.mqtt.client as mqtt
import time
import random
import os

broker_address=os.environ['BROKER']

colors = {
  'white': {
    'r':255,
    'g':255,
    'b':255 },
  'pink': {
    'r':255,
    'g':50,
    'b':50 },
  'teal': {
    'r':0,
    'g':255,
    'b':255},
  'greenish': {
    'r':0,
    'g':255,
    'b':100 },
  'purple': {
    'r':255,
    'g':0,
    'b':255},
  'yellow': {
    'r':255,
    'g':255,
    'b':0}
}

def on_message(client, userdata, message):
    shroom = str(message.payload.decode("utf-8"))
    print(shroom)
    client.publish("garden/" + shroom + "/set", "{'brightness': 255,'color': {'r': %(r)d,'g': %(g)d,'b': %(b)d},'transition': 0, 'state': 'ON'}" % (colors[random.choice(colors.keys())]))
    client.publish("garden/" + shroom + "/set", "{'brightness': 50, 'color': {'r': 0,'g': 25, 'b': 255},'transition': 1,'state': 'ON'}")
    client.publish("garden/" + shroom + "/set", "{'brightness': 50, 'color': {'r': 0,'g': 25, 'b': 255},'transition': 1,'state': 'ON'}")

client = mqtt.Client()

client.on_message=on_message
client.connect(broker_address) 
client.subscribe("garden/button", 0)

client.loop_forever()
