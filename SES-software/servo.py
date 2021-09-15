from pyfirmata import Arduino, SERVO
from time import sleep

port = 'COM5'
pin = 10
board = Arduino(port)

board.digital[pin].mode = SERVO


def rotateServo(pin, angle):
    board.digital[pin].write(angle)
    sleep(0.015)


def unlock():
    for i in range(0, 90):
        rotateServo(pin, i)


def lock():
    for i in range(90, 1, -1):
        rotateServo(pin, i)

