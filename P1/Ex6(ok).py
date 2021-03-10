from P1.Seq1 import Seq, test_sequences

def print_result(i, sequence):
    print("Sequences "+ str(i) + " :(lenght: "+ str(sequence.len()) + ")" + str(sequence))

    print("Bases: ", sequence.count())
print("----|PRACTICE 1, EXERCISE 6|-----")
#Se ha creado una funcion que tenga los valores guardados
list_sequences = list(test_sequences())
for i in range(0, len(list_sequences)):
    print_result(i, list_sequences[i])
