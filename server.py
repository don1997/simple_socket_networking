#SERVER
import socket
import random
#Client Accept integer between 1 and 100 from keyboard

#Open TCP socket to your server and send message 
#1 A string containing your name 
#2 the entered integer value and then wait for a server reply

#Server will create a string containing its name 
#THen accept connections from clients/
#on recipt of a client message SERVER SHOULD 
    #1. print client name and server name
    #2. itself randomly pick an integer between 1 and 100 and display 
    #client's number, it's number, and the sum of those numbers.
    #3.send its name string and the server chosen integer value back to the client 

#Gets name of host
def get_host():
    return socket.gethostname()

def get_ip():
    return socket.gethostbyname(get_host())

def get_number():
    return input("Enter an integer please: ")
    
print("HOSTNAME : " + get_host())
print("IP address: ")

print("IP address: " + get_ip())

get_number()


