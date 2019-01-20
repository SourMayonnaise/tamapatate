# yolo

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

def button1_callback(channel):
    print("Button 1 was pushed!")

def button2_callback(channel):
    print("Button 2 was pushed!")

def button3_callback(channel):
    print("Button 3 was pushed!")

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(10,GPIO.RISING,callback=button1_callback) # Setup event on pin 10 rising edge

GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 12 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(12,GPIO.RISING,callback=button2_callback) # Setup event on pin 12 rising edge

GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 16 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(16,GPIO.RISING,callback=button2_callback) # Setup event on pin 16 rising edge


message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up
