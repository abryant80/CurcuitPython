
# credits Nick Bednar
#9/15
#Servo shifts between 0-360 degrees back and forth.
import time
import board
import pwmio
from adafruit_motor import servo
from digitalio import DigitalInOut, Direction, Pull

btn = DigitalInOut(board.SWITCH)
btn.direction = Direction.INPUT
btn.pull = Pull.UP
# create a PWMOut object on Pin 12.
pwm = pwmio.PWMOut(board.D12, duty_cycle=2 ** 20, frequency=40)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)
angle = 90
from digitalio import DigitalInOut, Direction, Pull

btn = DigitalInOut(board.SWITCH)
btn.direction = Direction.INPUT
btn.pull = Pull.U
while True:
    if btn.value and angle < 180:
        my_servo.angle = angle++

    if btn2.value and angle > 0:
        my_servo.angle = angle--
       if not btn.value:
        print("BTN is down")
    else:
        #print("BTN is up")
        pass

    time.sleep(0.1) # sleep for debounce