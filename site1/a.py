from socket import *
HOST = '0.0.0.0'  # The server's hostname or IP address
PORT = 8000        # The port used by the server
with socket (AF_INET, SOCK_STREAM) as mysocket:
	mysocket.connect((HOST, PORT))
	url = str(input())
