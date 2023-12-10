
import time
import board
import adafruit_dht


#sensor = adafruit_dht.DHT11
#dhtDevice18 = adafruit_dht.DHT11(board.GP18)
dhtDevice28 = adafruit_dht.DHT11(board.GP28)

#temperaturemi = sensor.temperature
temperaturemi = dhtDevice28.temperature

#humiditymi = sensor.humidity
humiditymi = dhtDevice28.humidity
print (" ")
print (" temperature ")
print (temperaturemi)
print (" humidity ")
print (humiditymi)
