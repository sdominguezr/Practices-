#Ejercicio 1:
average = 0
count = 0
try:
    with open ("average.txt", "r") as f:
        for line in f:
            try:
                number = float(line.replace("\n", ""))
                average = average + number
                count += 1
            except ValueError:
                print ("A string was found: ", line.replace("\n", ""))
        f.close()
    if count > 0:
        print ("Average is: ", str(round(average / count, 3)))
except FileNotFoundError:
    print ("File not found")

#Ejercicio 2:
count_squa = 0
count_small = 0
count_adeno = 0
count_large = 0
try:
    with open("lungcancer.csv", "r") as f:
        header = next(f)
        for line in f:
            cell = line.replace('""', "").replace("\n", "").split(",")[-1]
            if cell == "1":
                count_squa = count_squa + 1
            elif cell == "0":
                count_small = count_small + 1
            elif cell == "adeno":
                count_adeno = count_adeno + 1
            else:
                count_large = count_large + 1
        f.close()
        print("The number of patiens with squamous cells is: ", str(count_squa))
        print("The number of patients with smallcell cells is: ", str(count_small))
        print("The number of patients with adeno cells is: ", str(count_adeno))
        print("The number of patients with large cells is: ", str(count_large))

except FileNotFoundError:
    print("The file is not found")

#Ejercicio 3:
high = 0
low = 100
with open ("cabbages.csv", "r") as f:
    header = next (f)
    for line in f:
        line_new = line.replace("\n", "").split(",")
        #print (line_new)
        for element in line_new:
            try:
                if int(element) > int(high):
                    high = element
            except ValueError:
                (None)
            try:
                if 30 < int(element):
                    if int(low) > int(element):
                        low = element
            except ValueError:
                None

print ("The max value is: ", high)
print ("The min value is: ", low )
f.close()

#Ejercicio 4:
n = 0
time_0 = 0
time = int(input("Introduce a number: "))
while time_0 < time:
    n = int(n)
    time_0 = int(time_0)
    n = n + 1
    solution = n * (n + 1) / 2
    time_0 = time_0 + 1
    print(solution)
    if time_0 == time:
        break





