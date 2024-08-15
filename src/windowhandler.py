import psutil
from pywinauto import Application

class windowsAPI():

    def __init__(self) -> None:

        self.pidlist = []
        self.windowname = 'RobloxPlayerBeta'


    def update_pids(self, account: None | str) -> None:
        new_pids = []
        for proc in psutil.process_iter(['pid', 'name']):
            if self.windowname in proc.info['name']:
                new_pids.append(proc.info['pid'])

        different = []
        for element in new_pids:
            if (account, element) not in self.pidlist:
                different.append((account, element))

        self.pidlist.extend(different)

    def switch_to_window_by_pid(self,pid) -> None:
        
        window = Application().connect(process=pid)
        window.top_window().maximize().set_focus()
    
    def close_window_by_pid(self,pid):

        window = psutil.Process(pid)
        window.terminate()


