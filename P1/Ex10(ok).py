from P1.Seq1 import Seq
from pathlib import Path
def print_result(i, sequence):
    print("Sequences "+ str(i) + " :(lenght: "+ str(sequence.len()) + ")" + str(sequence))
    print("Bases: ", sequence.count())
    print("Reverse: ", sequence.reverse())
    print("Complement :", sequence.complement())
    print("Common base: ", sequence.processing_genes())


print("----|PRACTICE 1, EXERCISE 10|-----")
s1 = Seq()
print_result('', s1)
PROJECT_PATH = "./PROJECT/"
gene_list = ["U5", "ADA", "FRAT1", "FXN"]
for gene in gene_list:
    filename = PROJECT_PATH + gene + ".txt"
    all_file_within = list(Path(filename).read_text() )#str
    print("Common base: ", Seq.processing_genes(filename, all_file_within))

