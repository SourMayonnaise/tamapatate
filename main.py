import time,random
import epd1in54b
import Image
import ImageFont
import ImageDraw
from gpiozero import Button,LED


button1 = Button(24)
button2 = Button(12)
button3 = Button(18)
led = LED(23)

COLORED = 1
UNCOLORED = 0

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
    
    epd = epd1in54b.EPD()
    epd.init()
    # clear the frame buffer
    frame_black = [0xFF] * (epd.width * epd.height / 8)
    frame_red = [0xFF] * (epd.width * epd.height / 8)
    
    # draw background
    epd.draw_filled_rectangle(frame_black, 30, 55, 170, 80, COLORED);
    
    # write strings to the buffer
    font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 18)
    epd.display_string_at(frame_black, 30, 30, "Welcome to", font, COLORED)
    epd.display_string_at(frame_red, 30, 60, "TAMAPATATE", font, UNCOLORED)
    epd.display_frame(frame_black, frame_red)
    epd.sleep()
    
    tamapatate = Tamagotchi("patate")
    alert = False
    print('Press Ctrl+C to exit')
    
    try:
        while(True):
             
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
                epd.display_string_at(frame_black, 70, 150, "popo", font, COLORED)
                epd.display_frame(frame_black, frame_red)
                epd.sleep()
               
            if((tamapatate.miam==0) or (tamapatate.joy==0) or (tamapatate.poo<2)) and alert==False:
                alert=True
                epd.display_string_at(frame_black, 45, 120, "ALERT", font, UNCOLORED)
                epd.draw_filled_rectangle(frame_red, 30, 115, 170, 140, COLORED)
                epd.display_frame(frame_black, frame_red)
                epd.sleep()
            
            time.sleep(0.2)
    except KeyboardInterrupt:
        time.sleep(1)
        raise
