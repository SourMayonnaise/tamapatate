import RPi.GPIO as GPIO

import time,random

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

A_pin = 26
B_pin = 6
C_pin = 5

GPIO.setmode(GPIO.BCM) # Use BCM pin numbering

GPIO.setup(A_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(B_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(C_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up

# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

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

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


GPIO.add_event_detect(26,GPIO.RISING,callback=button1_callback)
GPIO.add_event_detect(6,GPIO.RISING,callback=button2_callback)
GPIO.add_event_detect(5,GPIO.RISING,callback=button3_callback)
disp.begin()

# Clear display.
disp.clear()
disp.display()
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)
font = ImageFont.load_default()

draw.text((2, 2),    'Hello',  font=font, fill=255)
draw.text((2, 22), 'tamapatate', font=font, fill=255)
# Display image.
disp.image(image)
disp.display()
message = input("Press enter to quit\n\n") # Run until someone presses enter

GPIO.cleanup() # Clean up
