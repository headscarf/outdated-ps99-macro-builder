from AUTO_AFK.auto_afk import AutoAfk
from MISC.IMAGE_ON_SCREEN import find_image_on_screen as find
import pyautogui
import time
import pydirectinput
from ahk import AHK

COOLDOWN = 5

ahk = AHK()


def returnBoostsPosition() -> tuple:

    return tuple

def rejoin() -> None:


    f = find.FindImage()
    f.findOnScreen('leaveMessage', True)
    time.sleep(COOLDOWN)
    f.findOnScreen('servers', True)
    time.sleep(COOLDOWN)
    f.findOnScreen('joinButton', True)
    time.sleep(COOLDOWN)
    f.findOnScreen('teleportButton', True)
    time.sleep(COOLDOWN)
    ahk.click(1505, 318)
    time.sleep(COOLDOWN)
    ahk.mouse_drag(1505, 783, relative=True)
    time.sleep(COOLDOWN)
    f.findOnScreen('lastWorld', True)
    time.sleep(COOLDOWN)
    pydirectinput.press('d', presses=40)
    time.sleep(COOLDOWN)
    f.findOnScreen('autoFarm', True)


if __name__ == "__main__":
    while True:
        time.sleep(COOLDOWN)
        rejoin()
