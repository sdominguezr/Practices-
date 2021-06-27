def data():
    try:
        with open("Pima_tr.csv", "r") as f:
            full_list = []
            header = next(f)
            header = header.replace("\n", "").replace('""', '').split(",")
            for i in range(0, len(header)):
                full_list.append([])
            for line in f:
                element = line.replace("\n", "").replace('""', '').split(",")
                for i in range(0, len(header)):
                    full_list[i].append(element[i])
            f.close()
        return header, full_list
    except FileNotFoundError:
        return "There is no file named in that form."
header, full_list = data()
total_dict = {}
parameter = input("Introduce a parameter ")
common_value = input("Introduce a common value ")
total_list_dict = []
value = int(0)
for value in range(0, len(full_list[0])):
    total_dict = {'"id"': full_list[0][int(value)], header[1]: full_list[1][int(value)],
                  header[2]: full_list[2][int(value)], header[3]: full_list[3][int(value)],
                  header[4]: full_list[4][int(value)], header[5]: full_list[5][int(value)],
                  header[6]: full_list[6][int(value)], header[7]: full_list[7][int(value)],
                  header[8]: full_list[8][int(value)]}
    value = value + 1
    if value > len(full_list[0]):
        break
    else:
        total_list_dict.append(total_dict)
print((total_list_dict[0]['"id"']))
(total_list_dict[0].update({'"' + parameter + '"':str(common_value)}))
print(total_list_dict[0])













