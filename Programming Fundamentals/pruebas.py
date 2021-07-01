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
#parameter = input("Introduce a parameter ")
#common_value = input("Introduce a common value ")
total_list_dict = []
value = int(0)




#print((total_list_dict[0]['"id"']))
#(total_list_dict[0].update({'"' + parameter + '"':str(common_value)}))
#print(total_list_dict)

def data():
    full_list = []
    with open("melanoma.csv", "r") as f:
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

def option_2(patient_number):
    i = 0
    values = []
    finished =False
    while not finished:
        try:
            value = full_list[i][patient_number]
            values.append(value)
            i = i+1
        except IndexError:
            finished = True
    return values

patient_number = int(1) #int(input('Select a patient id:'))
print(option_2(patient_number))




