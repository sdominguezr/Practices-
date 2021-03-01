from pathlib import Path
filename = "sequences/U5.txt"
def seq_reverse(filename):
    all_file_str = Path(filename).read_text() #str
    all_file_list = all_file_str.split("\n")
    file_not_header = all_file_list[1:]
    all_file = str(file_not_header)
    extract_20_first = all_file[1:22]
    return(extract_20_first[::-1])
print(seq_reverse(filename))