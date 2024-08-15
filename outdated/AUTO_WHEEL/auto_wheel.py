import pyautogui
import time
import pydirectinput
#from MISC.IMAGE_ON_SCREEN import find_image_on_screen as find


class AutoWheel():

    def __init__(self) -> None:
        self.cooldown = .5
        #self.find = find.FindImage()
        

    def autoSpinWheel(self) -> None:
        time.sleep(self.cooldown)
        self.find.findOnScreen('spin', True)
        time.sleep(self.cooldown*10)
        self.find.findOnScreen('ok', True)
        time.sleep(self.cooldown)
        pydirectinput.press('s', presses=5)
        time.sleep(self.cooldown)
        pydirectinput.press('w', presses=5)
        time.sleep(self.cooldown)
        


if __name__ == "__main__":
    aw = AutoWheel()
    time.sleep(3)
    while True:
        aw.autoSpinWheel()


#getAndPrintMousePosition()