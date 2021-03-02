import P01.Seq0 as seq0
filename = "sequences/ADA.txt"
with open(filename, "r") as f:
    full_list = []
    seq = next(f)
    seq = seq.replace("\n", "").replace('""', '').split(",")
print(seq0.seq_count(filename))

