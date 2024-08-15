import pyautogui
import time
import pydirectinput
#from MISC.IMAGE_ON_SCREEN import find_image_on_screen as find
from AUTO_FRUIT import boosts 


class AutoBoosts():

    def __init__(self) -> None:
        self.cooldown = .5
       #self.find = find.FindImage()
        self.boosts = boosts.Boosts()

    def takeAllBoosts(self) -> None:
        time.sleep(self.cooldown)
        self.find.findOnScreen('inventory', True)
        time.sleep(self.cooldown)
        self.find.findOnScreen('toggleGridMode', True)
        time.sleep(self.cooldown)
        self.find.findOnScreen('itemSection', True)
        time.sleep(self.cooldown)
        self.boosts.takeBoosts()
        time.sleep(self.cooldown)
        self.find.findOnScreen('x', True)
        time.sleep(self.cooldown)
        pydirectinput.press('q')    
        time.sleep(self.cooldown)
        pydirectinput.press('q')
        time.sleep(self.cooldown)
        pydirectinput.press('r')   


if __name__ == "__main__":
    ab = AutoBoosts()
    while True:
        time.sleep(5)
        ab.takeAllBoosts()


#getAndPrintMousePosition()