import requests
class efapi():
    def __init__(self):
        self.addr = "https://enemyfear.xyz/api/"
        print(f"[Enemyfear API] Connected to server ({self.addr})")
    def createKey(self, password):
        print(f"[Enemyfear API] Generated key")
        return requests.get(f"{self.addr}create-key.php?password={password}").text
