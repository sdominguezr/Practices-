import socket

# Configure the Server's IP and PORT
PORT = 8080
IP = "localhost" #Esto significa a que unicamente funcionará para aquellos programas que esten en la misma maquina
                #IP se puede quedar en blanco tambien

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()

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
            cs.send("We nedd a number". enconde())

        # -- Close the data socket
        cs.close()