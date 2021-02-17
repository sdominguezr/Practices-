
def correct_sequence(dna):
    for c in dna:
        if c != "A" and c != "C" and c !="G" and c != "T":
            return False
    return True

def count_nucleo(dna):
    a = 0
    c = 0
    g = 0
    t = 0
    for i in dna:
        if i == "A":
            a +=1
        elif i == "C":
            c +=1
        elif i == "G":
            g +=1
        elif i == "T":
            t +=1
    return a, c, g, t

def read_from_file(filename):
    with open(filename, "r") as f:
        dna = f.read()
        dna.replace("\n", "")
        return dna

dna = read_from_file("dna.txt")
a, c, g, t = count_nucleo(dna)
correct_dna = correct_sequence(dna)
if correct_dna:
    print("A: ", str(a))
    print("C: ", str(c))
    print("G: ", str(g))
    print("T: ", str(t))
else:
    print("Not a valid DNA sequence")