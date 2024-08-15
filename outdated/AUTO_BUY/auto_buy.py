import pyautogui
import time
import pydirectinput
#from MISC.IMAGE_ON_SCREEN import find_image_on_screen as find



class AutoBuy():

    def __init__(self) -> None:
        self.cooldown = 0.5
        #self.find = find.FindImage()


    def takeAllBoosts(self) -> None:
        time.sleep(self.cooldown)
        self.find.findOnScreen('1200', True)
        time.sleep(self.cooldown)
        self.find.findOnScreen('buy1200', True)
        time.sleep(self.cooldown)
        self.find.findOnScreen('regularok', True)
        time.sleep(self.cooldown)
        self.find.findOnScreen('ok', True)
        time.sleep(self.cooldown)


if __name__ == "__main__":
    ab = AutoBuy()
    while True:
        time.sleep(5)
        ab.takeAllBoosts()


#getAndPrintMousePosition()