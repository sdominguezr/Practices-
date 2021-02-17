dna = "CATGTAfGACTAG"
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
a, c, g, t = count_nucleo(dna)
correct_dna = correct_sequence(dna)
if correct_dna:
    print("A: ", str(a))
    print("C: ", str(c))
    print("G: ", str(g))
    print("T: ", str(t))
else:
    print("Not a valid DNA sequence")