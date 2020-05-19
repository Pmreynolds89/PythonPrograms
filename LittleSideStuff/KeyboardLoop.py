#!/usr/bin/env python
# coding: utf-8

from time import sleep
from pyKey import pressKey, releaseKey
from pynput import keyboard
import threading


def on_press(key):
    if key == keyboard.Key.esc:
        return False


def walk_loop():
    while True:
        pressKey('D')
        sleep(10)
        releaseKey('D')
        sleep(0.5)
        pressKey('A')
        sleep(10)
        releaseKey('A')
        sleep(0.5)


print('Starting in 5 seconds.')
sleep(5)

try:
    thread_one = threading.Thread(target=walk_loop, args=(), daemon=True)
    thread_one.start()
except Exception as error:
    print(error, "Error: unable to start thread")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

print('Done.')
sleep(0.75)
