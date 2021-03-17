from Client0 import Client
from pathlib import Path
from Seq1 import Seq

PRACTICE = 2
EXERCISE  = 1
PORT = 8081
IP = "127.0.0.1"
c = Client(IP,PORT)
print("-----|EXERCOSE1|------", {PRACTICE}, "AND",  {EXERCISE})
s =Seq()
PROJECT_PATH = "./PROJECT/"
s.read_fasta(PROJECT_PATH +"U5.txt")
count = 0
i =0
while i < len(s.strbases) and count < 5:
    fragment = s.strbases[i: i + 10]
    count = count + 1
    i =+10
    print("fragment ", count, ": ", fragment)
    print(c.talk(fragment))