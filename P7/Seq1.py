#----------Session06---------
import termcolor
from pathlib import Path
class Seq:
    """A class for representing sequences"""
    NULL_SEQUENCES = "NULL" #Son constantes. Las constantes siempre se escriben en mayuculas
    INVALID_SEQUENCE = "ERROR"
    def __init__(self, strbases= NULL_SEQUENCES): #Init inicia class

        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases
        if strbases == Seq.NULL_SEQUENCES:
            print("Null seq created")
            self.strbases = strbases
        else:
            print(self.strbases)
            if self.is_valid_sequence(): #if seq0.is_valid_sequence(strbases):
                self.strbases = strbases
                print("New sequence created!")
            else:
                self.strbases = Seq.INVALID_SEQUENCE
                print("Incorrect sequence detected")

    def is_valid_sequence(self):
        for c in self.strbases:
            if c != "A" and c != "C" and c != "G" and c != "T":
                return False
        return True

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases
    def len(self):
        """Calculate the length of the sequence"""
        if self.strbases == "NULL" or self.strbases  =="ERROR":
            return 0
        else:
            return len(self.strbases)
    @staticmethod
    def print_seqs(list_sequences):
        for i in range(0, len(list_sequences)):
            text  ="Sequence" +str(i) + ": length" + str(list_sequences[i].len())
            termcolor.cprint(text, "yellow")

    def print_seqs(list_sequences):
        for i in range(0, len(list_sequences)):
            print("Sequence", i, ": lenght ", list_sequences[i].len())
    def count_bases(self):
        a, c, g, t = 0, 0, 0, 0
        if self.strbases == Seq.NULL_SEQUENCES or self.strbases == Seq.INVALID_SEQUENCE:
            return  a,c,g,t
        else:
            for ch in self.strbases:
                if ch == "A":
                    a += 1
                elif ch == "C":
                    c += 1
                elif ch == "G":
                    g += 1
                else:
                    t += 1
            return a, c, g, t
    def percentage_base(self, count_bases, seq_len):
        a = "A" + str(round(count_bases[0]/ seq_len()* 100,2) + "%")
        c = "C" + str(round(count_bases[0] / seq_len() * 100, 2) + "%")
        g = "G" + str(round(count_bases[0] / seq_len() * 100, 2) + "%")
        t = "T" + str(round(count_bases[0] / seq_len() * 100, 2) + "%")
        return {'A:':a,'C:':c,'G:' :g, 'T:':t}
    def frquent_base(self, dict_count):
        return max(dict_count, key=dict_count.get)
    def generate_seqs(pattern, number):
        list_seq = []
        for i in range(0, number):
            list_seq.append(Seq(pattern * (i + 1)))
    def count(self):
        a,c,g,t = self.count_bases()
        dict_bases = {"A" : a, "C": c, "G": g, "T": t}
        return dict_bases
    def reverse(self):
        if self.strbases == Seq.NULL_SEQUENCES:
            return "NULL"
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return "ERROR"
        else:
            return self.strbases[::-1]
    def complement(self):
        if self.strbases == Seq.NULL_SEQUENCES:
            return "NULL"
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return "ERROR"
        else:
            complement = ""
            for ch in self.strbases:
                if ch == "A":
                    complement += "T"
                elif ch == "C":
                    complement += "G"
                elif ch == "G":
                    complement += "C"
                else:
                    complement += "A"
            return complement
    @staticmethod
    def take_out_first_line(seq):
        return seq[seq.find("\n") + 1:].replace("\n", "")

    def read_fasta(self, filename):
        self.strbases = Seq.take_out_first_line(Path(filename).read_text())
    def processing_genes(self, filename, all_file_within):
        if self.strbases == Seq.NULL_SEQUENCES:
            return "NULL"
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return "ERROR"
        else:
            all_file_list = []
            for element in all_file_within:
                if element == "\n":
                    None
                else:
                    element = element
                    all_file_list.append(element)
                count_a = all_file_list.count("A")
                count_c = all_file_list.count("C")
                count_g = all_file_list.count("G")
                count_t = all_file_list.count("T")
                base = ["A", "C", "G", "T"]
                count_list = [count_a, count_c, count_g, count_t]
                dict_count = dict(zip(count_list, base))
                order_count = sorted(count_list)
                return ("The most common base in " + filename + " is " + dict_count[(order_count[-1])])
def test_sequences():
    s1 = Seq()
    s2 = Seq("ACTGA")
    s3 = Seq("Invalid sequence")
    return s1,s2,s3

