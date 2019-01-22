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

GPIO.setup(A_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Input with pull-up
GPIO.setup(B_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Input with pull-up
GPIO.setup(C_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Input with pull-up

# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

mlevel = 0 #main level
validate = False #enter menu

def button1_callback(channel):
    global mlevel
    print("Button 1 was pushed!")
    if mlevel<=10:
        mlevel+=1
    else:
        mlevel=0

def button2_callback(channel):
    global mlevel, validate
    print("Button 2 was pushed!")
    validate=True

def button3_callback(channel):
    global mlevel
    print("Button 3 was pushed!")
    mlevel=0
    validate = False

class Tamagotchi:
    def __init__(self,name):
        self.name=name
        self.miam=4
        self.joy=4
        self.poo=1
        self.weight=2
        self.alert=False

    def manger(self):
        self.miam+=1
        self.weight+=1

    def clean(self):
        self.poo=1

    def play(self):
        self.joy+=2
        self.weight-=3

    def snack(self):
        self.joy+=2
        self.weight+=5

if __name__ == '__main__':
    # Initialize library.
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
    tamapatate = Tamagotchi("patate")

    #------------BUTTONS SETTING ---------------

    GPIO.add_event_detect(A_pin,GPIO.RISING,callback=button1_callback)
    GPIO.add_event_detect(B_pin,GPIO.RISING,callback=button2_callback)
    GPIO.add_event_detect(C_pin,GPIO.RISING,callback=button3_callback)


    alert = False
    print('Press Ctrl+C to exit')
    draw.text((2, 2),    'Hello',  font=font, fill=255)
    draw.text((2, 22), 'tamapatate', font=font, fill=255)
    # Display image.
    disp.image(image)
    disp.display()
    try:
        while(True):
            #--- Action management---
            if validate==True:
                if mlevel==1:
                    print("menu 1 : informations")
                elif mlevel==2:
                    print("menu 2 : food")
                    tamapatate.manger()
                elif mlevel==3:
                    print("menu 3 : clean")
                    tamapatate.clean()
                elif mlevel==4:
                    print("menu 4 : game")
                    tamapatate.play()
            validate==False
            #---State management of the vitual pet---
            statMiam=random.randint(0,100)
            statJoy=random.randint(0,100)
            statPoo=random.randint(0,100)
            if(statMiam>=98) and (tamapatate.miam>0):
                tamapatate.miam-=1
            if(statJoy>=98) and (tamapatate.joy>0):
                tamapatate.joy-=1
            if(statPoo>=99) and (tamapatate.poo>0):
                tamapatate.poo-=1

            #---Alert management---------
            if tamapatate.joy>0 and tamapatate.miam>0 and tamapatate.poo==1:
                tamapatate.alert=False
            else :
                tamapatate.alert=True
                print("alert")
                draw.text((2, 42), 'Alert', font=font, fill=255)


            #---Display on screen at the end of the tik---
            disp.image(image)
            disp.display()
            time.sleep(0.2)

    except KeyboardInterrupt:
        # Draw a black filled box to clear the image.
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        disp.image(image)
        disp.display()

        GPIO.cleanup()
        time.sleep(1)
        raise
