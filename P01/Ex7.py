from pathlib import Path
filename = "sequences/ADA.txt"
def seq_complement(filename):
    all_file_str = Path(filename).read_text()  # str
    all_file_list = all_file_str.split("\n")
    file_not_header = all_file_list[0:]  # list
    all_file = str(file_not_header)
    extract = all_file[2:21] #str
    extract_list = list(extract)
    complement = []
    for element in extract_list:
        if element == "A":
            element = "T"
            complement.append(element)
        elif element == "C":
            element = "G"
            complement.append(element)
        elif element == "T":
            element = "A"
            complement.append(element)
        elif element == "G":
            element = "C"
            complement.append(element)
        else:
            break
    return complement, extract_list
complement, extract_list = seq_complement(filename)

print (extract_list)
print(complement)