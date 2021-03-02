import P01.Seq0 as seq0
from pathlib import Path
filename = "sequences/ADA.txt"
def seq_len(filename):
    without = len(Path(filename).read_text())
    return "The length of the " + str(filename) + " is"  + str(without)
print(seq0.seq_len(filename))

