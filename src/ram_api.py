import requests
import windowhandler
import time

class ram():

    def __init__(self) -> None:

        # web server

        self.port = 8983 
        self.password = "YourPassForRamHere"
        
        self.url = f"http://localhost:{self.port}"

        # accounts

        self.accounts = []

        # ps99

        self.placeid = "8737899170"
        self.jobid = "https://www.roblox.com/games/8737899170/Pet-Simulator-99-UPD-5?privateServerLinkCode=87843565969671911269465106630086"

        # my windows api

        self.wapi = windowhandler.windowsAPI()


    def getAllAccounts(self) -> None:

        u = f"{self.url}/GetAccounts"

        params = {
            "Password": self.password
        }

        self.accounts = requests.get(u, params=params).text
        self.accounts = self.accounts.split(',')

    def launchAccount(self, account: str) -> None:

        u = f"{self.url}/LaunchAccount"

        params = {
            "Account": account,
            "PlaceId": self.placeid,
            "JobId": self.jobid,
            "Password": self.password
        }

        requests.get(u, params=params)
        self.wapi.update_pids(account)


if __name__ == "__main__":

    ra = ram()


    time.sleep(3)

    ra.wapi.update_pids("KosherMaf1a")
    pids = ra.wapi.pidlist

    print(pids)

    pids_dict = dict(pids)

    print(pids_dict["KosherMaf1a"])

    #ra.wapi.close_window_by_pid(pids[1])
