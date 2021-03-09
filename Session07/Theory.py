class Seq:
    """A class for representing sequences"""

    def __init__(self, bases): #Init inicia class

        # Initialize the sequence with the value
        # passed as argument when creating the object
        if self.is_valid_sequence():
            self.strbases = bases #No tiene porque ser igual
            print("New sequence created!")

        else:
            self.strbases = "Error"
            print("Incorrect sequence detected")

    def is_valid_sequence(self):
        for c in self.strbases:
            if c != "A" and c != "C" and c != "G" and c !="T":
                return False
        return True

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases
    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)
class Gene(Seq): #Child class de SEQ class
    """This class is derived from the Seq Class
       All the objects of class Gene will inherite
       the methods from the Seq class

    """
    def __init__(self, strbases, name=""):
        super().__init__((strbases))#Estamos haciendo que python vuelva a la class principal, en este caso es
        #la class Seq
        self.name = name
        print("new gene created")
    def __str__(self):
        #Print the gene name wiht the sequence
        return self.name + "-" + self.strbases
    def len(self):
        #Calcular la longitud de la secuencia y decir si es larga
        if len(self.strbases) < 10 :
            return "sequence " + self.strbases + " is not long "
        else:
            return "Sequence " + self.strbases+ " is long"
    pass
# --- Main program
s1 = Seq("AGTACACTGGT")
s2 = Seq("CGTAAC")
g = Gene("CGTATATTACG", "FRAT1")
# strbases = CGTA... || name = "FRAT1"

# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f"  Length: {s1.len()}")
print(f"Sequence 2: {s2}")
print(f"  Length: {s2.len()}")
#-------- Session 09/03 -------
#Para comunicarnos con los objetos usamos los metodos
#Diferences between self.strbases and strbases
    #strbases = informacion que damos a la class
    #self.strbases = informacion que nosotros damos como objeto

#def __init__(self): es lafuncion instructor en otros lenguajes
#en python esta funcion se llama initialator
#cuando damos los metodos, estamos haciendo que la funcion se haga mas espeficida

#Dentro de una clase podemos encontrar class atributes, valores comunes para todas las funciones
#[Nota: las class atributes no son muy usados]
#Para poder usarlo, dentro de los metodos tendremos que escibir:
#---> self.__class__.(nombre de la variable a la que nos referimso

#Inheritance es lo que hay en Gene(Seq), es una forma de reusar los parametros de otra classs sin tener que escibrilo
#la sequencia entera otra vez[Reusamos entero el codigo principal]
# [Nota: no debemos olvidarnos de inicializar la class que estamos reusando]

#------> CLIENT SERVERS <------
#Client server is the most common paradigms para cuando estamos usando internet
#Identifiquemos todas las partes:
    #-Ip adress: it adresses the client. The adress is not unique. Commonly we have around 2 or 3 that will be
    # deliver random. They have 32 characters. Para ver ip: ipconfig in linuxis wiht f
    #-Ping: test the conectivity. [DNS: capacidad de transformar un domain a ip adress]
    #-URLS: tranformadores de domain a IP adress, IP adress es el lenguaje que la maquina entiende,
    #-Port: en un servidor que esta funcionando en un port,
    #-Socket: way to indentify IP and port. Mech that is used yo connect to one server
    
