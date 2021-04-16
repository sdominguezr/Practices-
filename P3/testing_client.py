import socket
import termcolor
from termcolor import colored
import colorama
PORT = 8081
IP = "127.0.0.1"
class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def ping(self):
        print("ok")

    def advanced_ping(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.ip, self.port))
            print("Server is up")
            s.close()
        except ConnectionRefusedError:
            print("Could not connect to server. Is it running?")

    def __str__(self):
        return "Connection to server at "+ self.ip+ ",port "+ str(self.port)
    def talk(self, command): #create connection
        # -- Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))

        # Send data.
        s.send(str.encode(command))

        # Receive data
        response = s.recv(2048).decode("utf-8")

        # Close the socket
        s.close()

        # Return the response
        return "From server: " + response
    def debug_talk(self, command): #Ejercicio 4
        colorama.init(strip="False")
        print(termcolor.colored("Message", end=""))
        new_msg = colored(command, "red")
        return new_msg

c = Client(IP, PORT)
while True:
    command = input("Write an option: ")
    print(c.talk(command))
    if command == "EXIT":
        break

