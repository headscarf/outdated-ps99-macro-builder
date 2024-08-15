from IMAGE_ON_SCREEN import find_image_on_screen
import time
import pydirectinput

class macrosAPI():

    def __init__(self) -> None:
        self.find = find_image_on_screen.FindImage()
        self.cooldown = 1

    def change_to_second_world_vip(self) -> None:
        self.find.findOnScreen("teleportButton", True)
        time.sleep(self.cooldown)
        self.find.findOnScreen("rocket", True)
        time.sleep(self.cooldown)
        self.find.findOnScreen("yes", True)
        time.sleep(self.cooldown * 10)
        self.find.findOnScreen("teleportButton", True)
        time.sleep(self.cooldown)
        self.find.findOnScreen("rocket", True)
        time.sleep(self.cooldown)
        self.find.findOnScreen("yes", True)

    def world_tp(self, world: str) -> None:
        self.find.findOnScreen("teleportButton", True)
        time.sleep(self.cooldown)
        self.find.findOnScreen("search", True)
        pydirectinput.write(world)
        time.sleep(self.cooldown)

    def go_to_last_area(self) -> None:
        self.world_tp("dominus vault")
        self.find.findOnScreen("dominus", True)
        time.sleep(self.cooldown*10)
        pydirectinput.press("d", presses=17)
        time.sleep(self.cooldown)
        self.find.findOnScreen("autoFarm", True)
    
    def go_and_hatch(self) -> None:
        self.world_tp("tech spawn")
        self.find.findOnScreen("spawn", True)
        time.sleep(self.cooldown*10)
        self.auto_egg()
        pydirectinput.press("a", presses=39)
        time.sleep(self.cooldown)
        pydirectinput.press("s", presses=86)
        time.sleep(self.cooldown)
        pydirectinput.press("d", presses=31)
        time.sleep(self.cooldown)
        pydirectinput.press("s", presses=5)
        time.sleep(self.cooldown)
        pydirectinput.press("e", presses=1)
        time.sleep(self.cooldown)
        self.find.findOnScreen("buy70", True)
        self.find.findOnScreen("buy76", True)
        self.find.findOnScreen("buy93", True)
        time.sleep(self.cooldown)
        pydirectinput.click()

    def auto_egg(self) -> None:
        self.find.findOnScreen("auto_egg", True)
        time.sleep(self.cooldown/2)
        self.find.findOnScreen("off", True, None, True)
        time.sleep(self.cooldown/2)
        self.find.findOnScreen("off", True, None, True)
        time.sleep(self.cooldown/2)
        self.find.findOnScreen("x", True)

    def open_inventory(self) -> None:
        self.find.findOnScreen("inventory", True)

    def search_and_use_max(self, to_search: str) -> None:
        self.find.findOnScreen("search", True)
        pydirectinput.write(to_search, interval=0)
        time.sleep(self.cooldown)
        self.find.findOnScreen(to_search, True, "Right")
        self.find.findOnScreen("eat_max", True)
        self.find.findOnScreen("place_max", True)
        self.find.findOnScreen("use_all", True)
        time.sleep(self.cooldown)
        self.find.findOnScreen("ult", True)
        self.find.findOnScreen("itemSection", True)

    def apply_boosts(self) -> None:
        self.open_inventory()
        time.sleep(self.cooldown)
        self.find.findOnScreen("itemSection", True)

        boosts = {
            
            'apple',
            'banana',
            'orange',
            'pineapple',
            'bone',
            'ball',
            'squeaky',
            'rainbow fruit',
            'fortune',
            'watermelon',
            'sprink'

        }

        for boost in boosts:
            self.search_and_use_max(boost)

    def anti_afk(self) -> None:
        pydirectinput.press("q", presses=2)



if __name__ == "__main__":

    ma = macrosAPI()
    time.sleep(2)
    ma.go_to_last_area()
    time.sleep(2)
    ma.go_and_hatch()
