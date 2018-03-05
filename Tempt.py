import RPi.GPIO as GPIO
from time import time as tiempo
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)

while True:
  try:
    tFile = open('/sys/class/thermal/thermal_zone0/temp')
    tArgus = open('/home/pi/Desktop/tempts.txt', 'w')
    #tFile = open('/sys/class/thermal/thermal_zone0/temp')
    temp = float(tFile.read())
    tempC = temp/1000
    #tArgus = open('/home/pi/Desktop/tempts.txt', 'w')
    s = str(tempC)
    tArgus.write(s)
    if tempC > 40:
      GPIO.output(26, 1)
      print ("HOT")
    else:
      GPIO.output(26, 0)
      print ("COLD")
    #tiempo(1)
    #tFile.close()
    #tArgus.close()

  except:
    tFile.close()
    tArgus.close()
    GPIO.cleanup()
    exit