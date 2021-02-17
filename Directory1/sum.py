res = 0
for i in range(1, 21):
    #print("Now the result is :", res)
    res += 1
print("TOTAL SUM :", res)

#Modos para el debugger
#"Step over": ejecutar codigo linea linea
#"Step into":ejecuta el codigo linea a linea pero, entramos en la funcion.
#EJEMPLO STEP INTO
def sum(n):
    res = 0
    for i in range(1, 21):
        # print("Now the result is :", res)
        res += 1
    return res
print("sum of the 20 first", sum(20))
print("sum of the 100 first", sum(100))
#-------


