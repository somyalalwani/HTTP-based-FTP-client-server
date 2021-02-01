from socket import *

HOST = '0.0.0.0'  # The server's hostname or IP address
PORT = 8000        # The port used by the server

with socket (AF_INET, SOCK_STREAM) as mysocket:
	mysocket.connect((HOST, PORT))
	url = str(input())

	req=url.split()
	if(req[0]!="GET"):
		print("Invalid input")
	else:
		mysocket.sendall(('./'+req[1]).encode()) 
		data=mysocket.recv(1024*7000,MSG_WAITALL)
		
		b=data.split(b"\n\n")[1]

		extension=url[-4:]
		new_file="new_file"+extension
		with open(new_file,'wb') as f:
				req1=f.write(b)


		mysocket.close()
