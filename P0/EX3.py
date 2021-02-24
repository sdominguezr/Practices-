import P0.Seq0 as seq0
GENE_FOLDER = "./Sequences/"
gene_list = ["U5, ADA, FRAT1, FXN"]
for gene in gene_list:
    sequence = seq0.seq_read_fasta(GENE_FOLDER + gene + '.txt')
    print('Gene' + gene + "-----> lenght: " + seq0.seq_len(sequence))
