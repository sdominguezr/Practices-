from P1.Seq1 import Seq
from pathlib import Path
PROJECT_PATH = "PROJECT/"
gene_list = ["U5", "ADA", "FRAT1", "FXN"]
for gene in gene_list:
    filename = PROJECT_PATH + gene + "txt"
    all_file_within =  list(Path(filename).read_text() )
    print(Seq.processing_genes())

def test_sequences():
    s1 = Seq()
    s2 = Seq("ACTGA")
    s3 = Seq("Invalid sequence")
    return s1,s2,s3