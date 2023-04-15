#!/usr/bin/env python3

import time
from pynput.mouse import Button, Controller
from pynput import keyboard
import threading

mouse = Controller()

Cords = [(680, 460), (780, 520), (780, 640), (680, 700), (570, 645), (570, 520), (740, 340), (840, 400), (920, 520), (900, 640), (850, 750), (750, 800), (600, 800), (515, 740), (450, 650), (430, 530), (515, 420), (620, 360), (680, 230), (880, 280), (980, 400), (1030, 580), (980, 750), (880, 880), (670, 930), (500, 880), (370, 750), (330, 590), (380, 400), (500, 280)]

loop_running = False

def on_press(key):
    global loop_running

    if key == keyboard.Key.enter:
        if not loop_running:
            loop_running = True
            t = threading.Thread(target=loop)
            t.start()
        else:
            loop_running = False

def loop():
    while loop_running:
        for Cord in Cords:
            if not loop_running:
                break
            mouse.position = Cord
            mouse.press(Button.left)
            time.sleep(delay_time)
            mouse.release(Button.left)

def main():
    global delay_time

    delay_time = 0.7

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == '__main__':
    main()

