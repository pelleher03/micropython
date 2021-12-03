from machine import Pin, ADC
from myservo import myServo
import time

degree = 0

servo = myServo(15)
servo.myServoWriteAngle(degree)
time.sleep_ms(1000)

xVal = ADC(Pin(36))
yVal = ADC(Pin(39))
zVal = Pin(14, Pin.IN, Pin.PULL_UP)

xVal.atten(ADC.ATTN_11DB)
yVal.atten(ADC.ATTN_11DB)
xVal.width(ADC.WIDTH_12BIT)
yVal.width(ADC.WIDTH_12BIT)

while True:
    servo.myServoWriteAngle(degree)
    print('X,Y,Z:', xVal.read(), ',', yVal.read(), ',', zVal.value())
    print(degree)
    x = xVal.read()
    time.sleep(0.1)
    if x > 3500:
        degree = degree + 5
    elif x < 600:
        degree = degree - 5
        
    
        