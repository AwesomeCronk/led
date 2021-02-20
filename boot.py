
#Connect to WiFi
#Set internal clock with ntptime
#Start the interpreter cycle
#`-This will occur when main.py runs.

import gc, network, utime, ntptime
from machine import Pin, PWM

g.collect()

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)
while not station.isconnected():
    pass

ntptime.host = 'us.pool.itp.org'
ntptime.settime()


pinR = Pin(15)
pwmR = PWM(pinR)
pwmR.freq(500)
pwmR.duty(1023)
