import socket
import sys 
import os
 
#Create a TCP server socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

#Prepare the sever socket
#FillInStart
serverPort = 2424
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
#FillInEnd 

while True:    
    print('Ready to serve...') 
    #Set up a new connection from the client
    connectionSocket, addr = serverSocket.accept()

    #If an exception occurs during the execution of try clause
    #the rest of the clause is skipped
    #If the exception type matches the word after except
    #the except clause is executed
    try: 
        #Receive the request message from the client
        message = connectionSocket.recv(1024).decode() #FillInStart #FillInEnd 
        #Extract the path of the requested object from the message
        #The path is the second part of HTTP header, identified by [1]
        filename = message.split()[1]
        #Because the extracted path of the HTTP request includes 
        #a character '\', we read the path from the second character 
        f = open(filename[1:])     
        #Store the entire content of the requested file in a buffer
        outputdata = f.read()
        
        #Send the HTTP response header line to the connection socket
        #FillInStart
        httpHeader = "HTTP/1.1 200 OK \r\n"
        connectionSocket.send(httpHeader.encode())       
        #FillInEnd

        #Send the content of the requested file to the client 
        for i in range(0, len(outputdata)): 
            connectionSocket.send(outputdata[i].encode())               
        
        connectionSocket.send("\r\n".encode()) 
        connectionSocket.close() 
    
    except IOError:
        #Send HTTP response message for file not found
        #FillInStart
        errorMessage = "HTTP/1.1 404 Not Found\r\n"
        connectionSocket.send(errorMessage.encode())
        #FillInEnd 
        
        #Close client socket 
        connectionSocket.close()

#Terminate the program
serverSocket.close()
sys.exit()
