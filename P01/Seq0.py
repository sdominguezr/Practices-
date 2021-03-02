from pathlib import Path
def seq_ping():
    return "ok"
def seq_read_fasta(filename):
    sequence = (Path(filename).read_text())
    return sequence
def seq_read_fasta(filename): #Exercise 2
    all_file_str = Path(filename).read_text() #str
    all_file_list = all_file_str.split("\n")
    file_not_header = all_file_list[0:] #list
    all_file = str(file_not_header)
    return(all_file[1:22])
def seq_len(filename): #Ejercicio 3
    without = len(Path(filename).read_text())
    return "The length of the " + str(filename) + " is"  + str(without)
def seq_count_base(filename, file): #Ejercicio 4
    a,c,g,t = 0, 0, 0, 0
    for d in file:
        if d == "A":
            a +=1
        elif d == "C":
            c += 1
        elif d == "T":
            t += 1
        else:
            g += 1
        gene_dict = "\n" + "A: " + str(a) + "\n" + 'C: ' + str(c) + "\n" + 'G: ' + str(g) + "\n" + 'T: ' + str(t)
        return  "Gene is " + filename + gene_dict
def seq_count(seq): #Ejercicio 5
    a,c,g,t = 0, 0, 0, 0
    for d in seq:
        if d == "A":
            a +=1
        elif d == "C":
            c += 1
        elif d == "T":
            t += 1
        else:
            g += 1
        gene_dict = {"A": a, 'C': c, 'G': g, 'T': t}
    return gene_dict
def seq_reverse(filename): #Ejercicio 6
    all_file_str = Path(filename).read_text() #str
    all_file_list = all_file_str.split("\n")
    file_not_header = all_file_list[1:]
    all_file = str(file_not_header)
    extract_20_first = all_file[1:22]
    return(extract_20_first[::-1])
def seq_complement(filename): #Ejercicio 7
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
def processing_genes(filename, all_file_withn): #Ejercicio 8
    all_file_list = []
    for element in all_file_withn:
        if element == "\n":
            None
        else:
            element = element
            all_file_list.append(element)
    count_a = all_file_list.count("A")
    count_c = all_file_list.count("C")
    count_g = all_file_list.count("G")
    count_t = all_file_list.count("T")
    base = ["A", "C", "G", "T"]
    count_list = [count_a,count_c,count_g, count_t ]
    dict_count = dict(zip(count_list, base))
    order_count = sorted(count_list)
    return ("The most common base in " + filename + " is " + dict_count[(order_count[-1])])
