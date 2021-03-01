import P0.Seq0 as seq0
GENE_FOLDER = "./Sequences/"
gene_list = ["U5, ADA, FRAT1, FXN"]
base_list = ["A", 'C', 'T', 'G']
#Gene U5:Gene FXN:Gene ADA: Gene FRAT1:

for gene in gene_list:
    sequence = seq0.seq_read_fasta(GENE_FOLDER + gene + '.txt')
    print("Gene", gene)
    for base in base_list:
        print(base + ":", seq0.seq_count_base(sequence, base))
print('Gene' + gene + "-----> lenght: " + seq0.seq_len(sequence))
