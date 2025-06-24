from adafruit_circuitplayground import cp
import time

def turn_all_pixels_on():
    for i in range(10):
        cp.pixels[i] = (0, 255, 0)
    cp.pixels.show()

def turn_all_pixels_off():
    for i in range(10):
        cp.pixels[i] = (0, 0, 0)
    cp.pixels.show()

while True:
    if cp.touch_A1:
        turn_all_pixels_on()
    else:
        turn_all_pixels_off()

    time.sleep(0.1)

while True:
    if cp.button_a:
        cp.play_file("ahem_x.wav")

    if cp.button_b:
        cp.play_file("applause_y.wav")

while True:
    if cp.switch:
        cp.pixels[0]((255, 0, 0))
    else:
        cp.pixels[0]((0, 0, 0))
    cp.pixels.show()
    time.sleep(0.1)
# Write your code here :-)
