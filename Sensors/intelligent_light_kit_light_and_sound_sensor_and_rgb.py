from machine import I2C,Pin,ADC
from ws2812 import WS2812
from utime import sleep

led = WS2812(18,1)
Light_SENSOR = ADC(0)
Sound_SENSOR = ADC(1)

while True:
    sleep(0.5)
    average = 0
    light = Light_SENSOR.read_u16()/256
    
    for i in range (1000): 
        sound = Sound_SENSOR.read_u16()/256 #on divise par 256 car la range value de la led rgb est de 0-255
        average += sound
        
    sound = average/1000
    print (light,sound)
    
    if light < 50:
        led.pixels_fill((255,255,255))
        led.pixels_show()
        sleep(0.1)
    else:
        if sound >= 50:
            led.pixels_fill((255,0,0))
            led.pixels_show()
            sleep(1)
        if sound >= 25 and sound < 50:
            led.pixels_fill((255,255,0))
            led.pixels_show()
            sleep(1)
        if sound < 25:   
            led.pixels_fill((0,255,0))
            led.pixels_show()
            sleep(1)
