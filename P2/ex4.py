from Client0 import Client
PRACTICE = 2
EXERCISE  = 1
PORT = 8081
IP = "127.0.0.1"
c = Client(IP,PORT)
c.debug_talk("Hello")
print("-----|EXERCOSE1|------", {PRACTICE}, "AND",  {EXERCISE})

#Para colorear hay que seguir
import termcolor
import colorama
colorama.init(strip ="False")
print(termcolor.colored("Message", end=""))
