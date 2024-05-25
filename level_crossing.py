#save as main.py and save to pico to run automatically

from picozero import LED
from picozero import Button
from time import sleep

orange = LED(5)
red1 = LED(8)
red2 = LED(13)
button = Button(18)

orange_pause = 3
flash_rate = 0.25


while True:
    if button.is_pressed:
        print("Button pressed")
        orange.on()
        sleep(orange_pause)
        orange.off()
        
        while True and button.is_pressed:
            red1.on()
            sleep(flash_rate)
            red1.off()
            red2.on()
            sleep(flash_rate)
            red2.off()
            
    else:
        print("Button not pressed")
        orange.off()
        red1.off()
        red2.off()

        

