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
def opt_2(full_list, header, parameter, common_value ):
    try:
        value = int(0)
        for value in range(0, len(full_list[0])):
            total_dict = {header[0]: full_list[0][int(value)], header[1]: full_list[1][int(value)],
                          header[2]: full_list[2][int(value)], header[3]: full_list[3][int(value)],
                          header[4]: full_list[4][int(value)], header[5]: full_list[5][int(value)],
                          header[6]: full_list[6][int(value)], header[7]: full_list[7][int(value)],
                          header[8]: full_list[8][int(value)]}
            value = value + 1
            if value > len(full_list[0]):
                break
            if total_dict['"' + parameter + '"'] == common_value:
                return (total_dict)
    except Exception:
        return "The program has encountered a problem. Try again"
def opt_3(patient_id):
    try:
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
            if total_dict['"id"'] == '"' + patient_id + '"':
                information = ("The patient's id is: " + total_dict['"id"'] + "\n"
                            "The value of var npreg is: " + total_dict['"npreg"'] + "\n"
                            "The value of var glu is: " + total_dict['"glu"'] + "\n"
                            "The value of var bp is: " + total_dict['"bp"'] + "\n"
                            "The value of var skin is: " + total_dict['"skin"'] + "\n"
                            "The value of var bmi is: " + total_dict['"bmi"'] + "\n"
                            "The value of var ped is: " + total_dict['"ped"'] + "\n"
                            "The value of var age is: " + total_dict['"age"'] + "\n"
                            "The value of var type is: " + total_dict['"type"'] + "\n")
                return (information)
                break
            else:
                continue
    except Exception:
        return "There was a problem during the execution. Try again."

def opt_4(full_list, name_variable, new_value, patient_number):
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
    (total_list_dict[patient_number + 1].update({'"' + name_variable + '"': str(new_value)}))
    update_information = ("The patient's id is: " + total_list_dict[patient_number + 1] + "\n"
                          "The patient's id is: " + total_dict['"id"'] + "\n" 
                          "The patient's id is: " + total_dict['"id"'] + "\n"
                          "The patient's id is: " + total_dict['"id"'] + "\n"
                          "The patient's id is: " + total_dict['"id"'] + "\n"
                          "The patient's id is: " + total_dict['"id"'] + "\n"
                          "The patient's id is: " + total_dict['"id"'] + "\n")
    return (total_list_dict)

def opt_5(full_list, new_file_name):
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

#Main program
not_finish = False
while not not_finish:
    print(menu())
    try:
        election = int(input("Please choose an election from the menu: "))
        if election == 1:
            i = int(input("Please choose an option from the menu variable"))
            print(menu_var())
            print(opt_1(full_list, i))
        elif election == 2:
            parameter = input("Please introduce the parameter in common: ")
            common_value = input("Please introduce the value you want the parameter to have in common")
            print(opt_2(full_list, header, parameter, common_value))
        elif election == 3:
            patient_id = (input("Introduce a patient id: "))
            print(opt_3( patient_id))
        elif election == 4:
            patient_number = int(input("Introude a patient id: "))
            name_variable = input("Introduce the number for the variable you want to change: ")
            new_value = input("Intoduce a new value: ")
            print("The information is now : ")
            print(opt_4(full_list, name_variable, new_value, patient_number))
        elif election == 5:
            new_file_name = "a2"  # input("Introduce a name for the new file: ")
            print(opt_5(all_dict))
        elif election == 6:
            break
        else:
            print("Introduce a number from the menu")
    except ValueError:
        print("Introduce a number. Try again.")