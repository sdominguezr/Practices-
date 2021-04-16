import termcolor
from pathlib import Path
PATH_NAME = "./Sequences/"
def print_colored(message, color):
    print(termcolor.colored(message, color))
def format_command(command):
    return command.replace("\n", "").replace("\r", "")
def ping():
    print_colored("Ping command", "green")
def info(argument):
    argument = argument[argument.find("\n") + 1:].replace("\n", "")
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
    print(information)
    return information
def complement(argument):
    argument = argument[argument.find("\n") + 1:].replace("\n", "")
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
    print(complement)
    return str(complement)
def reverso(argument):
    argument = argument[argument.find("\n") + 1:].replace("\n", "")
    print(str(argument[::-1]))
    return str(argument[::-1])
def gene(argument):
    try:
        PATH_NAME = "./Sequences/"
        argument = PATH_NAME + argument + ".txt"
        print(str(Path(argument).read_text()))
        return str(Path(argument).read_text())
    except IndexError:
        pass
    except FileNotFoundError:
        pass
        return "There's no file named in that way"



