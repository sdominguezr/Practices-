#Ejercicio 1: creacion de un modulo
#seq_ping() function

def seq_ping():
    return("ok")
    #print("ok) Se puede imprimir, ya que solo necesitamos el print
print(seq_ping())
#Ejercicio 2: open file, remove header, print 20 first
from pathlib import Path
def take_out_first_line(seq):
    return seq[seq.find("\n") + 1].replace("\n", "")

def seq_read_fasta(filename):
    sequence = take_out_first_line(Path(filename).read_text())
    return sequence

def seq_len(seq):
    return len(seq)