from P1.Seq1 import Seq
def print_result(i, sequence):
    print("Sequences "+ str(i) + " :(lenght: "+ str(sequence.len()) + ")" + str(sequence))
    print("Bases: ", sequence.count())
    print("Reverse: ", sequence.reverse())
    print("Complement :", sequence.complement())
    #print("Common base: ", sequence.processing_genes())

PROJECT_PATH = "./PROJECT/"
print("----|PRACTICE 1, EXERCISE 9|-----")
s1 = Seq()
print_result('', s1)
print(s1.strbases)
print(s1.strbases[0:20])
gene_list = ["U5", "ADA", "FRAT1", "FXN"]
for gene in gene_list:
    print(s1.read_fasta(PROJECT_PATH + gene + ".txt"))


