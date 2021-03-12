#Ejercicio 1: creacion de un modulo
#seq_ping() function
import P0.Seq0 as seq0
print("ok")
#Ejercicio 2
import P0.Seq0 as seq0
U5_seq = seq0.seq_read_fasta("../P1/PROJECT/U5.txt")
print ( "The 20 first are: ", U5_seq[0:20])
#Ejercicio 3: total number of bases
#usaremos el import mencionado en el ejercicio 2
#----
def seq_len(seq):
    return len(seq)

def seq_count_base(seq_base):
    return seq.count(base)
