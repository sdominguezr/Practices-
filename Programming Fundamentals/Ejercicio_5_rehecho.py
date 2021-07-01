def menu():
    print("""The following option is provided.
                1.- Download DNA sequence.
                2.- Validate string.
                3.- Print DNA info.
                4.- Count all the letters.
                5.- Is it a palindrome?
                6.- Exit.""")


def download_dna():  # decision 1
    import requests
    coronavirus_id = "NC_045512.2"  # input("Enter a code of a DNA sequence: ")
    api_url = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id={}&rettype=fasta&retmode=text".format(
        coronavirus_id)
    coronavirus_genome = requests.get(api_url)
    if "Error" in coronavirus_genome.text:
        return "Error"
    else:
        return coronavirus_genome.text


def check_nucleotides():  # decision 2
    coronavirus_genome = download_dna()
    coronavirus_genome = coronavirus_genome[coronavirus_genome.find("\n") + 1:].replace("\n", " ")
    for c in range(0, len(coronavirus_genome)):
        molecule = (coronavirus_genome[c] == "A" or coronavirus_genome[c] == "C" or coronavirus_genome[c] == "G" or
                    coronavirus_genome[c] == "T")
        if molecule:
            return "The sequence is correct."
        else:
            return "The sequence is not correct. "


def first_line_info():  # decision 3
    coronavirus_genome = download_dna()
    number = len(download_dna()) - len(coronavirus_genome[coronavirus_genome.find("\n")+1:])
    coronavirus_genome = coronavirus_genome[0: number]
    return coronavirus_genome


def decision_4():
    coronavirus_genome = download_dna()
    coronavirus_genome = coronavirus_genome[coronavirus_genome.find("\n") + 1:].replace("\n", " ")
    if len(download_dna()) > 5:
        coronavirus_genome = download_dna()
        adenine = coronavirus_genome.count("A")
        coronavirus_genome = download_dna()
        citosine = coronavirus_genome.count("C")
        coronavirus_genome = download_dna()
        guanine = coronavirus_genome.count("G")
        coronavirus_genome = download_dna()
        timine = coronavirus_genome.count("T")
        return ("A-> " + str(adenine) + ", C-> " + str(citosine) + ", G-> " + str(guanine) + ", T-> " + str(
            timine))
    else:
        return "Please introduce a DNA sequence"


def palindrome():  # decision 5
    coronavirus_genome = download_dna()
    coronavirus_genome = coronavirus_genome[coronavirus_genome.find("\n") + 1:].replace("\n", " ")
    if coronavirus_genome[0:] == coronavirus_genome[::-1]:
        return "The sequence is a palindrome."
    else:
        return "The sequence is not a palindrome."


'''--------------------------------------------------------'''
option = True
while option:
    menu()
    decision = input("Choose between the option: ")
    if decision == '1':
        print(download_dna())
    elif decision == "2":
        print(check_nucleotides())
    elif decision =="3":
        print(first_line_info())
    elif decision =="4":
        print(decision_4())
    elif decision == "5":
        print(palindrome())
    else:
        break
        option = False