from Client0 import Client
from pathlib import Path
from Seq1 import Seq

PRACTICE = 2
EXERCISE  = 1
PORT = 8081
PORT_2 = 1200
IP = "127.0.0.1"
c = Client(IP,PORT)
c_2 = Client(IP, PORT_2)
print("-----|EXERCOSE1|------", {PRACTICE}, "AND",  {EXERCISE})
s =Seq()
PROJECT_PATH = "./PROJECT/"
s.read_fasta(PROJECT_PATH +"U5.txt")
count = 0
i =0
while i < len(s.strbases) and count < 10:
    fragment = s.strbases[i: i + 10]
    count = count + 1
    i =+10
    print("fragment " + str(count) + ": " + str(fragment))
    if count % 2 == 0:
        print(c_2.talk("fragment " + str(count) + ": " + str(fragment)))
    else:
        print(c.talk("fragment " + str(count) + ": " + str(fragment)))