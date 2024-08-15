import pyautogui
from ahk import AHK
import os



class FindImage:
    
    def __init__(self) -> None:
       
       self.ahk = AHK()
       self.IMG_PATH = 'D:\ps99_automatic\src\IMAGE_ON_SCREEN\IMAGES_TO_FIND'
       self.confidence = 0.85

    def findOnScreen(self, img_name: str, click: bool, mouse: None | str = None, scale: None | bool = None) -> None | bool:
        
        file_path = os.path.join(self.IMG_PATH, img_name + '.png')

        if not os.path.isfile(file_path): # checks if file exists -> avoiding problems
            img_name = img_name.upper()
            print(f"\t[-] '{img_name}' DOES NOT EXIST")
            return False

        try:
            if scale is None:
                button_pos = pyautogui.locateOnScreen(f'{self.IMG_PATH}\\{img_name}.png',grayscale=False, confidence=self.confidence)
            else:
                #print(scale)
                button_pos = pyautogui.locateOnScreen(f'{self.IMG_PATH}\\{img_name}.png',grayscale=scale, confidence=self.confidence)
            button_point = pyautogui.center(button_pos)
            if click:
                if mouse is not None:
                    self.ahk.click(button_point.x, button_point.y, mouse)
                else:
                    self.ahk.click(button_point.x, button_point.y)
            else:
                return button_point
                
            
        except:
            img_name = img_name.upper()
            print(f"\t[-] FAIED TO FIND '{img_name}' ON SCREEN") 
    



   
