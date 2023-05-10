# Aaron 
import board
import time
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5 

print("Make it red!")

while True:
    print("Make it red!")
    dot.fill((255, 0, 0))  # red
    time.sleep(3)          # delay 3 seconds
    print("Make it green!")  # green
    dot.fill((0, 255, 0))   
    time.sleep(3)       # delay 3 seconds
    print("Make it blue")  
    dot.fill((0, 0, 255))  # blue
    time.sleep(3)    # delay 3 seconds