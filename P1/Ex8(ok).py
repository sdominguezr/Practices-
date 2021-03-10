from P1.Seq1 import test_sequences

def print_result(i, sequence):
    print("Sequences "+ str(i) + " :(lenght: "+ str(sequence.len()) + ")" + str(sequence))
    print("Bases: ", sequence.count())
    print("Reverve: ", sequence.reverse())
    print("Complement :", sequence.complement())


print("----|PRACTICE 1, EXERCISE 8|-----")
list_sequences = list(test_sequences())
for i in range(0, len(list_sequences)):
    print_result(i, list_sequences[i])