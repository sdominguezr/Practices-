import P01.Seq0 as seq0
from pathlib import Path
header = "sequences/"
gene_list = ["U5", "ADA", "FRAT1", "FXN"]
for gene in gene_list:
    filename = header + gene + ".txt"
    all_file_withn = list(Path(filename).read_text() )#str
    print(seq0.processing_genes(filename, all_file_withn))
