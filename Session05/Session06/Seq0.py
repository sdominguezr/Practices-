#----------Session06---------
import termcolor
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
            text  ="Sequence" +str(i) + ": length" + str(list_sequences[i].len())
            termcolor.cprint(text, "yellow")

    def is_valid_sequence(self):
        for c in self.strbases:
            if c != "A" and c != "C" and c != "G" and c != "T":
                return False

    def print_seqs(list_sequences):
        for i in range(0, len(list_sequences)):
            print("Sequence", i, ": lenght ", list_sequences[i].len())
def generate_seqs(pattern, number):
    list_seq = []
    for i in range(0, number):
        list_seq.append(Seq(pattern * (i + 1)))
    return list_seq


