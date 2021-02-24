filename = "ADA.txt"
with open('ADA', "r") as f:
    full_list = []
    seq = next(f)
    seq = seq.replace("\n", "").replace('""', '').split(",")

def seq_count(seq):
    a,c,g,t = 0, 0, 0, 0
    for d in seq:
        if d == "A":
            a +=1
        elif d == "C":
            c += 1
        elif d == "T":
            t += 1
        else:
            g += 1
    gene_dict = {"A": a, 'C': c, 'G': g, 'T': t}

