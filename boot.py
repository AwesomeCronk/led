
#Connect to WiFi
#Set internal clock with ntptime
#Start the interpreter cycle
#`-This will occur when main.py runs.

import gc, network, utime, ntptime
from machine import Pin, PWM

#Garbage collection, just in case
g.collect()

#Connect to WiFi
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)
while not station.isconnected():
    pass

print('Connected to {}'.format(ssid))
print(station.ifconfig())

#Update internal time via NTP
ntptime.host = 'us.pool.itp.org'
ntptime.settime()

#Initialize LEDs. IO15 - Red, IO13 - Green, IO12 - Blue
valR = 0
pinR = Pin(15)
pwmR = PWM(pinR)
pwmR.freq(500)
pwmR.duty(1023)
