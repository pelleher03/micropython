from machine import ADC, Pin
from myservo import myServo
import time

servo = myServo(15)
servo.myServoWriteAngle(0)
time.sleep(1)

adc = ADC(Pin(36))
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_12BIT)

def get_degree(adc_val):
        degrees = []
        val = 0

        for x in range (0, 181):
            degree = [val, (val + 22.75)]
            degrees.append(degree)
            val += 22.75
        
        for degree in degrees:
            if (adc_val >= degree[0]) and (adc_val < degree[1]):
                servo_degree = degrees.index(degree)
        return servo_degree

while True:
    adc_val = adc.read()
    if get_degree(adc_val) > 0:
        servo.myServoWriteAngle(get_degree(adc_val))
        print(get_degree(adc_val), adc_val)
    time.sleep_ms(20)

