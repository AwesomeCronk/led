#Open a TCP socket and listen. When there is a connection, do the following:
#Get commands
#Parse commands
#Take actions
#send results to client
#If the client is still there, get the next set of commands and repeat. Otherwise, wait for a new client.

print('\n\n==========main.py running==========\n\n')

setLED('r', 512)
time.sleep(0.5)
setLED('g', 512)
time.sleep(0.5)
setLED('b', 512)
time.sleep(2)
setLED('r', 1024)
time.sleep(0.5)
setLED('g', 1024)
time.sleep(0.5)
setLED('b', 1024)
time.sleep(2)
setLED('r', 512)
time.sleep(0.5)
setLED('g', 512)
time.sleep(0.5)
setLED('b', 512)
time.sleep(2)
setLED('r', 0)
time.sleep(0.5)
setLED('g', 0)
time.sleep(0.5)
setLED('b', 0)
#time.sleep(2)