import statistics
def menu():
    configuration = (
                "Choose an option: " + " \n " + "1- Get the Stadistics." + " \n " + "2- Find Patient." + " \n " + "3- Number of People who Die because of Melanoma." + " \n " + "4- Clone the File." + " \n " + "5- Exit.")
    return configuration


print(menu())


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


header, full_list = data()
time_list = full_list[1]
status_list = full_list[2]
sex_list = full_list[3]
age_list = full_list[4]
year_list = full_list[5]
thickness_list = full_list[6]
ulcer_list = full_list[7]
entire_list = full_list[0:]
def option_1():
    high = 0
    low = 10 ** 5
    div = 0
    add = 0
    if item == "1" or item.lower() == "time":  # average, low, high
        for element in (time_list):
            (add) = int(add) + int(element)
            div += 1
            average = add / div
            if int(element) > int(high):
                high = element
            if int(element) < int(low):
                low = element
            med = statistics.median(time_list)

            have = None
            dont = None
            fem = None
            male = None

    elif item == "2" or item.lower() == "status":
        for element in status_list:
            add = int(add) + int(element)
            div += 1
            average = add / div
            if int(element) > int(high):
                high = element
            if int(element) < int(low):
                low = element
            med = statistics.median(time_list)

            have = None
            dont = None
            fem = None
            male = None

    elif item == "4" or item.lower() == "age":
        for element in (age_list):
            (add) = int(add) + int(element)
            div += 1
            average = add / div
            if int(element) > int(high):
                high = element
            if int(element) < int(low):
                low = element
            med = statistics.median(time_list)

            have = None
            dont = None
            fem = None
            male = None

    elif item == "5" or item.lower() == "year":
        for element in (year_list):
            (add) = int(add) + int(element)
            div += 1
            average = add / div
            if int(element) > int(high):
                high = element
            if int(element) < int(low):
                low = element
            med = statistics.median(time_list)

            have = None
            dont = None
            fem = None
            male = None

    elif item == "6" or item.lower() == "thickness":
        for element in (thickness_list):
            (add) = float(add) + float(element)
            div += 1
            average = add / div
            if float(element) > float(high):
                high = element
            if float(element) < float(low):
                low = element
            med = statistics.median(time_list)

            have = None
            dont = None
            fem = None
            male = None

    elif item == "7" or item.lower() == "ulcer":
        have = ulcer_list.count("1")
        dont = ulcer_list.count("0")
        med = None
        average = None
        high = None
        low = None
        fem = None
        male = None
    elif item == "3" or item.lower() == "sex":
        fem = sex_list.count("1")
        male = sex_list.count("0")
        med = None
        average = None
        high = None
        low = None
        have = None
        dont = None
    return high, low, average, med, have, dont, fem, male


def option_2(patient_number):
    i = 0
    values = []
    finished =False
    while not finished:
        try:
            value = full_list[i][patient_number - 1]
            values.append(value)
            i = i+1
        except IndexError:
            finished = True
    information =("Data for patient: " + str(values[0]) + "\n"
                  "Value for time: " + str(values[1]) + "\n"
                  "Value for status: " + str(values[2]) + "\n"
                  "Value for sex: " + str(values[3]) + "\n"
                  'Value for age: ' + str(values[5]) + "\n" +
                  'Value for year: ' + str(values[6]) + "\n" +
                  'Value for thickness: ' + str(values[7]) + "\n" +
                  'Value for ulcer: ' + str(values[8]) + "\n" )
    return information


def option_3():
    element_dm = 0
    element_l = 0
    element_dd = 0
    for element in status_list:
        if element == "1":
            element_dm = int(element_dm) + 1
    for element in status_list:
        if element == "2":
            element_l = int(element_l) + 1
    for element in status_list:
        if element == "3":
            element_dd = int(element_dd) + 1
    information = ("Patients who have died from melanoma: " + str(
        element_dm) + "\n" + "Patinents who were still alive: " + str(
        element_l) + "\n" + "Patients who have died from other reasons: " + str(element_dd))
    return information


def option_4():
    new_name = input("Introduce a new name: ")
    f_2 = open(new_name, "w")
    line = ""
    for i in range(0, len(entire_list[0])):
        for j in range(0, len(header)):
            line += entire_list[j][i] + ","
            f_2.write(line)
    return line
    f_2.close()


'''-------------------'''

with open("melanoma.csv", "r") as f:
    header = next(f)
    header = header.replace("\n", "").replace('""', '').split(",")
    for i in range(0, len(header)):
        full_list.append([])
        for line in f:
            element = line.replace("\n", "").replace('""', '').split(",")
            election = False
            while not election:
                menu()
                option = input("User's election is: ")
                print(option)
                if option == "1":
                    choose = False
                    while not choose:
                        item = input(
                            "Defined the item to get stadistic: " + " \n " + "To get ou tof the option introduced 'exit'.")
                        if item.lower() == "exit" or item == "0":
                            choose = True
                        else:
                            high, low, average, med, have, dont, fem, male = option_1()
                            if item != "7" and item != "3":
                                print("The maximun value is: ", high)
                                print("The minimum value is: ", low)
                                print("The average is: ", average)
                                print("The median is: ", med)
                            elif item == "7":
                                print("The patients with ulceration: ", have)
                                print("The patients with no ulceration:", dont)
                            elif item == "3":
                                print("The patients who are females are: ", fem)
                                print("The patiens who are males are: ", male)

                elif option == "2":
                    print(option_2())
                elif option == "3":
                    print(option_3())
                elif option == "4":
                    option_4()
                    print("Done")
                elif option == "5":
                    print("You have finisehd the program")
                    election = True
            break
        break
    f.close()

f.close()