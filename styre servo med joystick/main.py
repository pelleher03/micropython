import time
import network

ssidRouter = 'VG3Data'
passwordRouter = 'Admin:1234'

def STA_setup(ssidRouter, passwordRouter):
    print('Setup start')
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to', ssidRouter)
        sta_if.active(True)
        sta_if.connect(ssidRouter,passwordRouter)
        while not sta_if.isconnected():
            pass
    print('connected, IP address:', sta_if.ifconfig())
    print('Setup End')
try:
    STA_setup(ssidRouter, passwordRouter)
except:
    sta_if.disconnect()
        
        
        