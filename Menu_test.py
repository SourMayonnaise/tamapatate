from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)# button 1
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)# button 2
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)# button 3


# set global variables used
update = 1 # causes LCD to be updated while set to 1
mlevel = 1 # current menu level
blevel = 1 # last menu level

def level1():
    #main menu
    
def level2():
    #sub menu 
    
def level3():
    #sub menu 
    
def level4():
    #sub menu
    
def level5():
    #sub menu 
    
def level6():
    #sub menu 
    
def level7():
    #sub menu    
    
def option1(channel):
    global mlevel, update, blevel
    blevel = mlevel
    mlevel = mlevel*2
    update = 1
    
    
def option2(channel):
    global mlevel, update, blevel
    blevel = mlevel  
    mlevel = (mlevel*2) + 1
    update = 1  
    
def goback(channel):
    global mlevel, update, blevel
    mlevel = blevel
    blevel = int(mlevel/2)
    update = 1     
    
GPIO.add_event_detect(26, GPIO.RISING, callback=option1, bouncetime=200)    
GPIO.add_event_detect(19, GPIO.RISING, callback=option2, bouncetime=200)   
GPIO.add_event_detect(20, GPIO.RISING, callback=goback, bouncetime=200)    
        

#loop to update menu on LCD
while True:
    while update ==0:
        time.sleep (0.1)
        
     
    lcd.clear()
    
    if mlevel == 1: level1()
    if mlevel == 2: level2()
    if mlevel == 3: level3()
    if mlevel == 4: level4()
    if mlevel == 5: level5()
    if mlevel == 6: level6()
    if mlevel == 7: level7()
            
    update = 0
 
