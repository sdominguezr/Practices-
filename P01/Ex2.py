from pathlib import Path
filename = "sequences/ADA.txt"
def seq_read_fasta(filename):
    all_file_str = Path(filename).read_text() #str
    all_file_list = all_file_str.split("\n")
    file_not_header = all_file_list[0:] #list
    all_file = str(file_not_header)
    return(all_file[1:22])
print(seq_read_fasta(filename))