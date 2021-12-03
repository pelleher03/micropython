from machine import Pin, PWM, ADC
import time

pwm_0 = PWM(Pin(15, Pin.OUT), 10000,0)
pwm_1 = PWM(Pin(2, Pin.OUT), 10000,0)
pwm_2 = PWM(Pin(5, Pin.OUT), 10000,0)

adc_0 = ADC(Pin(36))
adc_1 = ADC(Pin(39))
adc_2 = ADC(Pin(34))

adc_0.atten(ADC.ATTN_11DB)
adc_1.atten(ADC.ATTN_11DB)
adc_2.atten(ADC.ATTN_11DB)

adc_0.width(ADC.WIDTH_10BIT)
adc_1.width(ADC.WIDTH_10BIT)
adc_2.width(ADC.WIDTH_10BIT)

try:
    while True:
        print(adc_0.read(), adc_1.read(), adc_2.read())
        pwm_0.duty(1023-adc_0.read())
        pwm_1.duty(1023-adc_1.read())
        pwm_2.duty(1023-adc_2.read())
except:
    pwm_0.deinit()
    pwm_1.deinit()
    pwm_2.deinit()
