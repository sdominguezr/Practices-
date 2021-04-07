import Client0
c = Client0.Client("localhost", 8080)
for i in range(0,5):
    c.talk("Message " + str(i))
#Storage of client info in list
import socket

# Configure the Server's IP and PORT
PORT = 8080
IP = "localhost"  # Esto significa a que unicamente funcionará para aquellos programas que esten en la misma maquina
# IP se puede quedar en blanco tambien
# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))
count_connection = 0
# -- Step 3: Configure the socket for listening
ls.listen()
count = +1
print ("Ther server is configured")
client_address_list = []
while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")
    try:
        (cs, client_ip_port) = ls.accept()
        client_address_list.append(client_ip_port)
        count_connection =+ 1
        print ("Connection " + str(count_connection) + ". Client IP, PORT: " + str(client_ip_port))
    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")
        # -- Close the listenning socket
        ls.close()
        # -- Exit!
        exit()

    # -- Execute this part if there are no errors
    else:

        print("A client has connected to the server!")

        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it
        # -- into a human-redeable string
        msg = msg_raw.decode()

        # -- Print the received message
        print(f"Message received: {msg}")

        # -- Send a response message to the client
        try:
            response = int(msg) ** int(msg)
            print("Response", response)

            # -- The message has to be encoded into bytes
            cs.send(str(response).encode())
        except ValueError:
            cs.send("We need a number".enconde())

        # -- Close the data socket
        cs.close()
        if count_connection == 5:
            for i in range(0, len(client_address_list)):
                print ("client "+ str(i) + ":cliente IP, PORT " + str(client_address_list[i]))
            exit(0)