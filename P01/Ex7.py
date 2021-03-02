import P01.Seq0 as seq0
filename = "sequences/ADA.txt"
complement, extract_list = seq0.seq_complement(filename)
print ("The original sequence is : " + str(extract_list))
print("The complement sequence is: " + str(complement))