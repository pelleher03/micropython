from machine import Pin, PWM, ADC
import time

pwm = PWM(Pin(25, Pin.OUT), 10000)
adc = ADC(Pin(36))
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_10BIT)

try:
    while True:
        adc_val = adc.read()
        pwm.duty(adc_val)
        print(adc_val)
        time.sleep_ms(100)
except:
    pwm.deinit()
