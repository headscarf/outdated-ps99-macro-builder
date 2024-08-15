
import time
#from MISC.IMAGE_ON_SCREEN import find_image_on_screen as find

class Boosts():

    def __init__(self) -> None:

        self.clickCooldown = 0.2

        #self.f = find.FindImage()

        self.boosts = {
            
            'apple',
            'banana',
            'orange',
            'pineapple',
            'bone',
            'ball',
            'duck',
            'rainbow',
            'cane',
            'fortune',
            'sprink'

        }

        self.events = {
            
            'piniata',
            'party'
            
        }


    def takeBoosts(self) -> None:
        for boost in self.boosts:
            self.f.findOnScreen(boost, True)
            time.sleep(self.clickCooldown)
            self.f.findOnScreen("ok", True)
            time.sleep(self.clickCooldown)
        for event in self.events:
            self.f.findOnScreen(event, True)
            time.sleep(self.clickCooldown)
            self.f.findOnScreen("ok", True)







