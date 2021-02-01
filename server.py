#Implementing a simple HTTP/1.0 Server

import socket

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

# Create socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)

print('Listening on port: %s ...' % SERVER_PORT)

while True:    
	# Wait for client connections
	client_connection, client_address = server_socket.accept()
    
    # Get the client request
	request = client_connection.recv(1024).decode()
	
	#request contains address of file
	
	#Parse HTTP headers
	#headers = request.split('\n')
	
	print(request)
	
	#n=3
	#filename='/'.join(request.split('/', n)[n:]) 
	#print("filename---------"+filename)
	# Get the content of the file
	
	headers = request.split('\n')
	filename = headers[0].split()[1]

	#print("#####:"+filename)

	if filename == '/':
		filename = './index.html'

	try:
		#fin = open('/home/somyalalwani9/Documents/ias/server' + filename,"rb")
		fin = open('.'+filename,"rb")
		content = fin.read()
		fin.close()

		response = 'HTTP/1.0 200 OK\n\n'
	except FileNotFoundError:
		response = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'
	
	# Send HTTP response
	client_connection.sendall(response.encode())
	client_connection.sendall(content)
	
	client_connection.close()

# Close socket
server_socket.close()
