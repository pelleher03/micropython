from machine import ADC, Pin, DAC
import time

adc = ADC(Pin(36))
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_12BIT)
dac = DAC(Pin(25))


while True:
    adc_val = adc.read()
    dac_val = adc_val/16
    voltage = adc_val / 4095.0 * 3.3
    dac.write(int(dac_val))
    print('ADC value: ', adc_val, 'DAC value: ', dac_val, 'Voltage: ', voltage, 'V')
    time.sleep_ms(100)
