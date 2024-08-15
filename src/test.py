import requests

id: int = 18197732821 # your id here love rae*

url = f"https://assetdelivery.roblox.com/v1/asset?id={id}"

try:
    response = requests.get(url)
    with open("texture.png", "wb") as file:
        file.write(response.content)
    print("saved image in src")
except:
    print(f"I am black lolz")
