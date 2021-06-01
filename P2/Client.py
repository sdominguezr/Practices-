import socket

# SERVER IP, PORT
# Write here the correct parameter for connecting to the
# Teacher's server
PORT = 1200 #Constante de PORT que va a conectar dos partes cliente-servidor
IP = "127.0.0.1"


# First, create the socket
# We will always use this parameters: AF_INET y SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AD_INET es el seocket por default
#SOCK_STREAM

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

# Send data. No strings can be send, only bytes
# It necesary to encode the string into bytes
s.send(str.encode("HELLO FROM THE CLIENT!!!")) #LA STRING ESTA SIENDO CODIFICADA EN BINARIO!!!

# Closing the socket
s.close()