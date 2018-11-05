import RPi.GPIO as GPIO
import time,random
from gpiozero import Button

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(23,GPIO.OUT)
GPIO.setup(18,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24,GPIO.IN, pull_up_down=GPIO.PUD_UP)

class Tamagotchi: 
    def __init__(self,name):
        self.name=name
        self.miam=4
        self.joy=4
        self.poo=2
        
    def manger(self):
        self.miam+=1
        
if __name__ == '__main__':
    print('Welcome to Tamapatate')
    tamapatate = Tamagotchi("patate")
    alert = False
    print('Press Ctrl+C to exit')
    try:
        while(True):
            Button3 = GPIO.input(18)
            Button2 = Button(12)
            Button1 = GPIO.input(24)
                
            if Button1==False:
                print('Button1 Pressed')
                
                #if Button2==False:
                    #print('Button2 Pressed')


            statMiam=random.randint(0,100)
            #print('miam')
            #print(statMiam)
            statJoy=random.randint(0,100)
            #print('joy')
            #print(statJoy)
            statPoo=random.randint(0,100)
            #print('poo')
            #print(statPoo)
            if(statMiam>=98) and (tamapatate.miam>0):
                tamapatate.miam-=1
            if(statJoy>=98) and (tamapatate.joy>0):
                tamapatate.joy-=1
            if(statPoo>=97) and (tamapatate.poo>0):
                tamapatate.poo-=1
                print('poopoo')
                
            if((tamapatate.miam==0) or (tamapatate.joy==0) or (tamapatate.poo<2)) and alert==False:
                alert=True
                GPIO.output(23,GPIO.HIGH)

            
            time.sleep(0.2)
    except KeyboardInterrupt:
        GPIO.output(23,GPIO.LOW)
        time.sleep(1)
        raise
