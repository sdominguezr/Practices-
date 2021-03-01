from pathlib import Path
filename = "sequences/ADA.txt"
all_file_withn = list(Path(filename).read_text() )#str
def processing_genes(filename):
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
print(processing_genes(filename))
