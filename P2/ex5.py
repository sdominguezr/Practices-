from Client0 import Client
from pathlib import Path

PRACTICE = 2
EXERCISE  = 1
PORT = 8081
IP = "127.0.0.1"
c = Client(IP,PORT)
print("-----|EXERCOSE1|------", {PRACTICE}, "AND",  {EXERCISE})
print("Sending U5...")
print(c.talk(Path("U5.txt").read_text()))
