# raspberryPicoLoraExternTempSensor
how to connect an esternal DHT11 sensor to the raspberry pico MakeZurich board

what we need

hardware

1 makeZurich board
1 test board
1 dht11 sensor

software

the raspi pico is already with circuit python installed.

we need to install adafruit_dht in the lib directory

connect your raspi pico to your comüuter with usb

it woill appear in the ls /dev an ttyACME

so the rasp pico is attached to your computer

now with strt the command

pyserail-miniterm

it show all connection you have and choose the ttyACME

so the program on the raspi pico will start already

this the porgram code.py ad if you need a library you must install the library with 

circup install

in our case we ust install adafruit_dht

circup install addfruit_dht

our program



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


result

Press any key to enter the REPL. Use CTRL-D to reload.
soft reboot

Auto-reload is on. Simply save files over USB to run them or enter REPL to disable.
code.py output:
␛]0;🐍Wi-Fi: off | code.py | 8.1.0␛\ 
 temperature 
24
 humidity 
74
␛]0;🐍Wi-Fi: off | Done | 8.1.0␛\
Code done running.

Press any key to enter the REPL. Use CTRL-D to reload.





