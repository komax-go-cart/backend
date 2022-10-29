import RPi.GPIO as GPIO
import time
import threading

GPIO.setmode(GPIO.BOARD)
GPIO.setup(38, GPIO.IN)

current_kmh = 0

def calculate_rpm(cycles_per_second):
    revperminute = cycles_per_second * 60
    meterperminute = revperminute * 90 / 100
    return str(round((meterperminute / 16.667))) + " km/h"

def main():
    global current_kmh
    counter = 1
    last = 0
    def counter_loop():
        nonlocal last
        nonlocal counter
        while True:
            data = GPIO.input(38)
            if last != data:
                last = data
                counter += 1

    th = threading.Thread(target=counter_loop)
    th.start()

    while True:
        counter_before = counter
        time.sleep(1)
        counter_after = counter

        ticks_per_s = counter_after - counter_before
        cycles_per_second = ticks_per_s / 12
        current_kmh = calculate_rpm(cycles_per_second)