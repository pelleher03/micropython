import time

print('ESP-32 klar for bruk')

while True:
    print('running time : ', time.ticks_ms()/1000, 's')
    time.sleep(1)