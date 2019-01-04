import time,random



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
        
    
if __name__ == '__main__':
    

    tamapatate = Tamagotchi("patate")
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
        time.sleep(1)
        raise
