from serial import Serial
from time import sleep

PORT = '/dev/tty.usbmodemfd141'

ser = Serial(PORT, 9600, timeout=1)

MIN_ANGLE = 0
MAX_ANGLE = 130
INCREMENT = 5


def move(angle, servo):
    ser.write(str(angle) + servo)

if __name__ == '__main__':
    for pos in range(MIN_ANGLE, MAX_ANGLE, INCREMENT):
        print pos
        move(pos, 'x')
        move(pos, 'y')
        sleep(0.1)
    move(0, 'x')
    move(0, 'y')
