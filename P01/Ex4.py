import P0.Seq0 as seq0
from pathlib import Path
GENE_FOLDER = "sequences/"
gene_list = ["U5", "ADA", "FRAT1", "FXN"]
#Gene U5:Gene FXN:Gene ADA: Gene FRAT1:
for gene in gene_list:
    filename = GENE_FOLDER + gene + ".txt"
    file = (Path(filename).read_text().split("\n")[1:])
    print(seq0.seq_count_base(filename, file))

