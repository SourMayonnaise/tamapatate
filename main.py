import time,random


from gpiozero import Button,LED
button1 = Button(24)
button2 = Button(12)
button3 = Button(18)
led = LED(23)


class Tamagotchi: 
    def __init__(self,name):
        self.name=name
        self.miam=4
        self.joy=4
        self.poo=2
        
    def manger(self):
        self.miam+=1
    
    def clean(self):
        self.poo=2
    
if __name__ == '__main__':
    
    print('Welcome to Tamapatate')
    tamapatate = Tamagotchi("patate")
    alert = False
    print('Press Ctrl+C to exit')
    
    try:
        while(True):
             
            if(button1.ispressed()):
                print('menu')
                
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

            
            time.sleep(0.2)
    except KeyboardInterrupt:
        time.sleep(1)
        raise

