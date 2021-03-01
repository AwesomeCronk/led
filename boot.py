import gc, network, time, ntptime
from machine import Pin, PWM

#Garbage collection, just in case
gc.collect()

#Connect to WiFi
def WiFiConnect(ssid, password):
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, password)
    while not station.isconnected():
        pass

    print('Connected to {}'.format(ssid))
    print(station.ifconfig())

#Update internal time via NTP
def updateTime(itpHost='us.pool.itp.org'):
    ntptime.host = itpHost
    ntptime.settime()

#Initialize LEDs. IO15 - Red, IO13 - Green, IO12 - Blue
vals = {'r': 0,              'g': 0,              'b': 0}
pins = {'r': Pin(15, Pin.OUT),        'g': Pin(13, Pin.OUT),        'b': Pin(12, Pin.OUT)}
pwms = {'r': PWM(pins['r']), 'g': PWM(pins['g']), 'b': PWM(pins['b'])}

def setLED(channel, value):
    #Type check, value should be int
    if not type(value) is int:
        raise ValueError('LED value is of wrong type.')
    #Type check, channel should be str
    if not type(channel) is str:
        raise ValueError('LED channel is of wrong type.')
    #Range check, value should be 0-1024
    if not 0 <= value <= 1024:
        raise ValueError('LED value of {} out of range.'.format(value))
    #Channel check, channel should be 'r', 'g', or 'b'
    if not channel in ('r', 'g', 'b'):
        raise ValueError('LED channel {} out of range.'.format(channel))

#LED value inputs should be 0-1024. 1024 should become 0, 1 should become 1023, and 0 should disable PWM.
    #Disable the pwm and set the pin high to turn off the led
    if value == 0:
        pwms[channel].deinit()
        pins[channel].value(1)
    else:
        if vals[channel] == 0:
            pwms[channel].init()
        pwms[channel].duty(1024-value)
        #Save the value in vals for comparison next call
        vals[channel] = value

setLED('r', 0)
setLED('g', 0)
setLED('b', 0)