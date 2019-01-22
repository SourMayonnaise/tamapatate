# yolo

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

mlevel = 0 #main level


def button1_callback(channel):
    global mlevel
    print("Button 1 was pushed!")
    if mlevel<=10:
        mlevel+=1
    else:
        mlevel=0

def button2_callback(channel):
    global mlevel
    print("Button 2 was pushed!")
    if mlevel==1:
        print("menu1")
    elif mlevel==2:
        print("menu2")
    elif mlevel==3:
        print("menu3")

def button3_callback(channel):
    global mlevel
    print("Button 3 was pushed!")
    mlevel=0

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(10,GPIO.RISING,callback=button1_callback) # Setup event on pin 10 rising edge

GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 12 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(12,GPIO.RISING,callback=button2_callback) # Setup event on pin 12 rising edge

GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 16 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(16,GPIO.RISING,callback=button3_callback) # Setup event on pin 16 rising edge


message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up
