import time,random
import RPi.GPIO as GPIO

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
