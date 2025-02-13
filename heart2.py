import os
import time


# Lista con diferentes tamaños de corazón para la animación
heart_frames = [
    """
        *****     *****    
      ********* *********  
     *********************  
    *********************** 
    *********************** 
     *********************  
       *****************    
         *************      
            *******         
              ***          
               *           
    """,
    """
        ***     ***    
       ****** ******  
      ***************  
     ***************** 
     ***************** 
      ***************  
        ***********    
          *******      
            ***        
             *         
    """,
   
]

def clear_screen():
    """Limpia la pantalla en Windows y Linux/macOS"""
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    for frame in heart_frames:
        clear_screen()
        print(frame)
        time.sleep(0.3)  

    time.sleep(0.1)  
