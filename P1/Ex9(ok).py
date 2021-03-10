from P1.Seq1 import Seq

def print_result(i, sequence):
    print("Sequences "+ str(i) + " :(lenght: "+ str(sequence.len()) + ")" + str(sequence))
    print("Bases: ", sequence.count())
    print("Reverse: ", sequence.reverse())
    print("Complement :", sequence.complement())

PROJECT_PATH = "./PROJECT/"


print("----|PRACTICE 1, EXERCISE 9|-----")
s1 = Seq()
s1.read_fasta(PROJECT_PATH + "ADA.txt")
print_result('', s1)
print(s1.strbases)
print(s1.strbases[0:20])
