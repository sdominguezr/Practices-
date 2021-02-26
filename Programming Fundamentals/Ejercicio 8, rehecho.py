import statistics
def menu():
    main_menu = (" Main menu:" + "\n"
    "1.- Calculate statistics" + "\n"
    "2.- Get patients under value" + "\n"
    "3.- Find patient info" + "\n"
    "4.- Change patient data" + "\n"
    "5.- Clone the file" + "\n"
    "6.- Exit")
    return main_menu
print(menu())
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
# print(full_list)
def menu_var():
    menu = (" Menu of varibales:" + "\n"
           "1.- Npreg: number of pregnancies." + "\n"
            "2.- Glu: plasma glucose in oral glucose tolerance test" + "\n"
            "3.- Bp: diastolic pressure" + "\n"
             "4.- Skin: triceps skin fold thickness" + "\n"
             "5.- BMI: body  mass index ( weigth in kg / height in m ^ 2)" + "\n"
             "6.- Ped: diabetes pedigree function" + "\n"
             "7.- Age: age in years" + "\n"
             "8.- Type: 'yes' or 'no' for diabetic according to WHO criteria")
    return menu
def opt_1(full_list, i):
    high = 0
    low = 10 ** 10
    div = 0
    add = 0
    aux_list = []
    yes = 0
    no = 0
    try:
        for value in full_list[i]:
            if value.isdigit():
                (add) = float(add) + float(value)
                div += 1
                average = add / div
                aux_list.append(float(value))
                med = statistics.median(aux_list)
                if float(value) > float(high):
                    high = value
                if float(value) < float(low):
                    low = value
            else:
                if value.lower() == '"yes"':
                    yes = int(yes) + 1
                if value.lower() == '"no"':
                    no = int(no) + 1
        yes_count = ("There are " + str(yes) + " yes")
        no_count = ("There are " + str(no) + " no")
        max_val = ("The maximum value is: " + str(high))
        min_val = ("The minimum value is: " + str(low))
        average_val = ("The maximun value is: " + str(average))
        med_val = "The median value is: " + str(med)
        frase = max_val + "\n" + min_val + "\n" + average_val + "\n" + med_val + "\n" + yes_count + '\n' + no_count
        # print(frase)
        return frase
    except TypeError:
        return "It does not exit a variable named like that. Try again."

    except NameError:
        return "The name introduced is not defined."
igual = 5
list_values = []
all_dict = dict(zip(header[1:], full_list[1:]))
print(all_dict)
def opt_2(full_list, i ):
    for index in range(0, len(full_list[i])):
        if full_list[i][index] == str(igual):
            index
            a = 1
            while a <= len(header):
                try:
                    print(str(header[a] + "; " + str(full_list[a][index])))
                    a += 1
                except IndexError:
                    break
                    a = 0
patient_id = 1 #int(input("Introduce a patient id: "))
#def opt_3(all_dict, patient_id):
index = 0
while index <= len(header):
    try:
        index += 1
        key = header[index]
        info = ("The value for the variable: " + header[index] , all_dict[key][patient_id - 1])
        print(info)#return(info)
    except IndexError:
        break
    except ValueError:
        continue
patient_id_4 = 1#input("Introude a patient id: ")
number_variable = 1 #input("Introduce the number for the variable you want to change: ")
new_variable = 1  #input("Intoduce a new variable: ")
#def opt_4(full_list, number_variable, new_variable, patien_id_4):
index = 0
values_list = full_list[index]
values_list[patient_id - 1: patient_id] = [new_variable]
print("The information is now : " )
while index <= len(header):
    try:
        index += 1
        info = "The value for the variable: " + header[index] + full_list[index][patient_id_4]
        print(info)
    except IndexError:
        break
def opt_5(all_dict):
    new_file_name =  "a2" #input("Introduce a name for the new file: ")
    new_file = open(new_file_name, "w")
    index_list = 0
    i = 0
    ok_i = False
    while not ok_i:
        try:
            written = new_file.write(str(full_list[i][index_list]) + ", ")
            i += 1
        except IndexError:
            written = new_file.write("\n")
            i = 0
            index_list += 1
            if index_list > len(full_list[i]):
                break
            else:
                continue
            new_file.close()
        return "Copy"