import P01.Seq0 as seq0
class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases): #Init inicia class

        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases
        if self.is_valid_sequence(): #if seq0.is_valid_sequence(strbases):
            self.strbases = strbases
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
    @staticmethod
    def print_seqs(list_sequences):
        for i in range(0, len(list_sequences)):
            print("Sequence", i, ": lenght ", list_sequences[i].len())
class Gene(Seq): #Child class de SEQ class
    """This class is derived from the Seq Class
       All the objects of class Gene will inherite
       the methods from the Seq class
    """
    pass
# --- Main program
s1 = Seq("AGTACACTGGT")
s2 = Seq("CGTAAC")

# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")