import time,random
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
mlevel = 0 #main level


class Tamagotchi:
    def __init__(self,name):
        self.name=name
        self.miam=4
        self.joy=4
        self.poo=2
        self.weight=2

    def manger(self):
        self.miam+=1
        self.weight+=1

    def clean(self):
        self.poo=2

    def play(self):
        self.joy+=2
        self.weight-=3

    def snack(self):
        self.joy+=2
        self.weight+=5


tamapatate = Tamagotchi("patate")

def button1_callback(channel):
    global mlevel
    if mlevel<=10:
        mlevel+=1
    else:
        mlevel=0

def button2_callback(channel):
    global mlevel, tamapatate
    if mlevel==1:
        print("menu1")
    elif mlevel==2:
        print("menu2")
    elif mlevel==3:
        print("clean")
        tamapatate.clean()

def button3_callback(channel):
    global mlevel
    mlevel=0


if __name__ == '__main__':

    global tamapatate
    #------------DISPLAY SETTING ---------------
    # 128x32 display with hardware I2C:
    disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
    # Initialize library.
    disp.begin()
    # Clear display.
    disp.clear()
    disp.display()
    # Clear display.
    disp.clear()
    disp.display()
    # Create blank image for drawing.
    # Make sure to create image with mode '1' for 1-bit color.
    width = disp.width
    height = disp.height
    image = Image.new('1', (width, height))
    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)
    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    # Draw some shapes.
    # First define some constants to allow easy resizing of shapes.
    padding = 2
    shape_width = 20
    top = padding
    bottom = height-padding
    # Move left to right keeping track of the current x position for drawing shapes.
    x = padding
    # Load default font.
    font = ImageFont.load_default()
    #------------BUTTONS SETTING ---------------
    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
    GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
    GPIO.add_event_detect(10,GPIO.RISING,callback=button1_callback) # Setup event on pin 10 rising edge

    GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 12 to be an input pin and set initial value to be pulled low (off)
    GPIO.add_event_detect(12,GPIO.RISING,callback=button2_callback) # Setup event on pin 12 rising edge

    GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 16 to be an input pin and set initial value to be pulled low (off)
    GPIO.add_event_detect(16,GPIO.RISING,callback=button3_callback) # Setup event on pin 16 rising edge


    alert = False
    print('Press Ctrl+C to exit')
    draw.text((x, top),    'Hello',  font=font, fill=255)
    draw.text((x, top+20), 'tamapatate', font=font, fill=255)
    # Display image.
    disp.image(image)
    disp.display()
    try:
        while(True):

            statMiam=random.randint(0,100)
            statJoy=random.randint(0,100)
            statPoo=random.randint(0,100)

            if(statMiam>=98) and (tamapatate.miam>0):
                tamapatate.miam-=1
            if(statJoy>=98) and (tamapatate.joy>0):
                tamapatate.joy-=1
            if(statPoo>=97) and (tamapatate.poo>0):
                tamapatate.poo-=1
                print('poopoo')


            if((tamapatate.miam==0) or (tamapatate.joy==0) or (tamapatate.poo<2)) and alert==False:
                alert=True
                print('ALERT')

            time.sleep(0.2)
    except KeyboardInterrupt:
        GPIO.cleanup()
        time.sleep(1)
        raise
