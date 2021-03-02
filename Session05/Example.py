#init creará una instance de cada
#init es llamado un consturctor y es ejecutado cada vez que declaremos una class
class Dog:
    #Una clase es un conjunto de funciones que nosotors definimos
    def __init__(self, name, age):
        #self: lugar donde se guardan los atributos
        #self simepre tendrá que aparecer que definamos funciones dentro de un class
        self.name = name
        self.age = age
    def sit(self): #En programa orientada a objetos, esto no son funciones son metodos
        print("This is a line")
    def set_name(self, name):
        self.name = name
    def sitdown(self):
        print("WOOF!!")
ares = Dog('ares', 10)
toby = Dog("toby", 21)
ares.name = "trueno" #si utilizamos ares.set_name("trueno) aestariamos usando un if
ares.age = 1
ares.sitdown() #imprime woof!!
pass