import pyautogui
import time
import pydirectinput
#from MISC.IMAGE_ON_SCREEN import find_image_on_screen as find


class CraftKeys():

    def __init__(self) -> None:
        self.cooldown = .5
        #self.find = find.FindImage()    
        

    def craftBlueKeys(self, whichKey : str) -> None:
        self.find.findOnScreen('search', True)
        pydirectinput.write("key")
        time.sleep(self.cooldown)
        self.find.findOnScreen(whichKey, True)
        time.sleep(self.cooldown)
        self.find.findOnScreen('yes', True)
        time.sleep(self.cooldown)
        self.find.findOnScreen('ok', True)
        time.sleep(self.cooldown)
        


if __name__ == "__main__":
    
    ck = CraftKeys()
    time.sleep(3)
    while True:
        ck.craftBlueKeys("uppertech")


#getAndPrintMousePosition()