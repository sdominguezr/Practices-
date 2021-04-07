import termcolor
def print_colored(message, color):

    print(termcolor.colored(message, color))
def format_command(command):
    return command.replace("\n", "").replace("\r", "")
def ping():
    print_colored("Ping command", "green")