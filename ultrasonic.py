#import libaries
import RPi.GPIO as GPIO
import time

#set up the mode
GPIO.setmode(GPIO.BCM)

#set up pin
TRIG = 23
ECHO = 17
LED = 20

#set up input output
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

#function to calculate the distance
def distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    
    #get the time
    start = time.time()
    stop = time.time()

    #start time
    while GPIO.input(ECHO) ==0:
        start = time.time()

    #finish time
    while GPIO.input(ECHO) ==1:
        stop = time.time()

    #calculate the distance
    distance= ((stop - start) *17000)
    return distance

if __name__ =='__main__':
    try:
        while True:
            dist = distance()
            #print out the distance
            print ("%.1f cm" %dist)
            
            #the LED will blink faster when the object is closer
            GPIO.output(LED,GPIO.HIGH)
            time.sleep(dist/10)
            GPIO.output(LED,GPIO.LOW)
            time.sleep(dist/10)

            #measure every second
            time.sleep(1)
    #stop the program when user press ctrl + C
    except KeyboardInterrupt:
        print("Stop")
        GPIO.cleanup()