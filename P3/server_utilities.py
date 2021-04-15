import termcolor
from pathlib import Path
def print_colored(message, color):

    print(termcolor.colored(message, color))
def format_command(command):
    return command.replace("\n", "").replace("\r", "")
def ping():
    print_colored("Ping command", "green")

def info(argument):
    a, c, g, t = 0, 0, 0, 0
    for ch in argument:
        if ch == "A":
            a += 1
        elif ch == "C":
            c += 1
        elif ch == "G":
            g += 1
        else:
            t += 1
    information = "Total length: " + str(len(argument)) + "\n" +\
                  "A: " + str(a)+ " (" + str(a*100/len(argument))+ '%)' + "\n"+ "C: " + str(c) + " (" + str(c*100/len(argument))+ '%)' +\
                  "\n"+ "G: "+ str(g) + " (" + str(g*100/len(argument)) + '%)' + "\n"+ "T: " + str(t) + " (" + str(a*100/len(argument))+ '%)'
    return information
def complement(argument):

    complement = ""
    for ch in argument:
        if ch == "A":
            complement += "T"
        elif ch == "C":
            complement += "G"
        elif ch == "G":
            complement += "C"
        elif ch == "T":
            complement += "A"
        else:
            complement = "It is not a proper DNA chain"
    return str(complement)
def reverso(argument):
    return str(argument[::-1])
def gene(argument):
    PATH_NAME = "./Sequences/"
    argument = PATH_NAME + argument + ".txt"
    return str (Path(argument).read_text())