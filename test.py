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
        sleep(0.1)
        for y_pos in range(MIN_ANGLE, MAX_ANGLE, INCREMENT):
            move(y_pos, 'y')
            sleep(0.1)
    move(40, 'x')
    move(40, 'y')

    import pdb; pdb.set_trace();
