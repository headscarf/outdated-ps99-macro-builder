import ram_api as ram
import windowhandler as windows
import macros
import time

class accounthandlerapi():

    def __init__(self):
        self.ram_api = ram.ram()
        self.win_api = windows.windowsAPI()
        self.macro = macros.macrosAPI()
        

if __name__ == "__main__":
    accountmanager = accounthandlerapi()
    windowsapi = accountmanager.win_api
    ramapi = accountmanager.ram_api
    macro = accountmanager.macro

    while True:
        #pids = windowsapi.pidlist
        #pids_dict = dict(pids)
        #print(pids_dict)

        pids = [37616, 43236, 27432] # temp pids, just doing anti afk
        for pid in pids: #pids_dict.values():
            #print(pid)
            windowsapi.switch_to_window_by_pid(pid)
            macro.anti_afk()
            time.sleep(5) 
        
        time.sleep(5*60) # sleeps for 5 mins


    #accountmanager.ram_api.launchAccount("kosherMaf1a")