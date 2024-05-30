from machine import ADC, Pin
from utime import sleep
from picozero import LED

#Setup phyisical connections
pot = ADC(26)     #pin 31, ADC 0
orange = LED(5)   #pin 7
red1 = LED(9)     #pin 12
red2 = LED(13)    #pin 17

#Value of measurement resistor in ohms
measurement_resistor = 10000

#Train present thresholds in mili-amps based on 10k measurement resistor
high_threshold = 0.146
low_threshold = 0.14

#LED timing in seconds
orange_pause = 1
flash_rate = 0.25

#ADC steps to volts conversion factor - fixed for Pi Pico
conversion_factor = 3.3 / 65535

#Check if train is present in section
def train_present():
    raw = pot.read_u16()
    volts = raw * conversion_factor
    amps = (volts / measurement_resistor) *1000
    if (amps < low_threshold) or (amps > high_threshold):
        presence = True
    else:
        presence = False
    print('Raw: {} '.format(raw), 'Voltage: {:.2f}V '.format(volts), 'Amps: {:.3}mA '.format(amps), 'Train: {}'.format(presence))
    return presence


#Main look checking if train present and then triggering lights
while True:
    if train_present():
        print("Train detected")
        orange.on()
        sleep(orange_pause)
        orange.off()
        
        while True and train_present():
            red1.on()
            sleep(flash_rate)
            red1.off()
            red2.on()
            sleep(flash_rate)
            red2.off()
            
    else:
        orange.off()
        red1.off()
        red2.off()
    sleep(0.25)