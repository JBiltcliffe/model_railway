from machine import ADC, Pin
from utime import sleep
pot = ADC(26)
conversion_factor = 3.3 / 65535


while True:
    raw = pot.read_u16()
    volts = raw * conversion_factor
    amps = (volts / 10000) *1000
    if (volts < 1.40) or (volts > 1.45):
        presence = "Train Present"
    else:
        presence = "No Train"
    print('Raw: {} '.format(raw), 'Voltage: {:.2f}V '.format(volts), 'Amps: {:.3}mA '.format(amps), 'Train: {}'.format(presence))
    sleep(0.25) 