import pyautogui as pag
import time
import random

# Moves the cursor automatically after 2 minutes of inactivity
def moveMouse():
    while True:
        pag.moveTo(random.randint(0, 1920), random.randint(0, 1080))
        time.sleep(120)
 
    # Make a dialog box to warn the user
    # Move the mouse to a random location if the user is inactive for 2 minutes
        if pag.position() == pag.position():
            pag.moveTo(random.randint(0, 1920), random.randint(0, 1080))
            time.sleep(120)
            
        elif pag.position() != pag.position():
            time.sleep(120)
            
    
        # Ends program by using ctrl + e
        if pag.keyDown('ctrl') and pag.keyDown('e'):
            pag.alert(text='The program has stopped'\
                  ,title="Mouse Alert" \
                  ,button='OK')
            break

# Run the program
moveMouse()