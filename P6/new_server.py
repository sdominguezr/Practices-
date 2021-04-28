#Count number of connections to the server
import socket
from P3 import server_utilities

list_sequences = ["U5" , "ADA","FRAT1",   "FXN", "RNU6_269P"]


PORT = 8081
IP = "127.0.0.1"  # Esto significa a que unicamente funcionará para aquellos programas que esten en la misma maquina
# IP se puede quedar en blanco tambien

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ls.bind((IP, PORT))
count_connection = 0
ls.listen()
client_address_list =[]
count = +1
print("The server is configured")
while True:
    print("Waiting for Clients to connect")
    try:
        (cs, client_ip_port) = ls.accept()
        count_connection =+ 1
        print("Connection " + str(count_connection) + ". Client IP, PORT: " + str(client_ip_port))

    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()
    print("A client has connected to the server!")
    msg_raw = cs.recv(2048)
    print(msg_raw)
    msg = msg_raw.decode()
    formatted_message = server_utilities.format_command(msg)
    print(formatted_message)
    formatted_message = formatted_message.split(" ")
    if len(formatted_message) ==1:
        command = formatted_message[0]
    else:
        command = formatted_message[0]
        argument = formatted_message[1]
    if command == "PING":
        server_utilities.ping()
        response = "ok"
        cs.send(str(response).encode())
    elif command == "GET":
        response = list_sequences[int(argument)]
        cs.send(response.encode())
    elif command == "INFO":
        argument = server_utilities.gene(list_sequences[0])
        response = server_utilities.info(argument)
        cs.send(str(response).encode())
    elif command == "COMP":
        argument = server_utilities.gene(list_sequences[0])
        response = server_utilities.complement(argument)
        cs.send((response.encode()))
    elif command == "REV":
        argument = server_utilities.gene(list_sequences[0])
        response = server_utilities.reverso(argument)
        cs.send(str(response).encode())
    elif command == "GENE":
        response = server_utilities.gene(argument)
        cs.send(str(response).encode())
    elif command == "EXIT":
        response = "CONNECTION HAS FINISHED"
        cs.send((str(response).encode()))
        break
    else:
        response = "Not availabe "
        cs.send(str(response).encode())
    cs.close()

