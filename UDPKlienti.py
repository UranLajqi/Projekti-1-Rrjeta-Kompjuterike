import socket
from socket import * 
serverPort = 13000
ip = '127.0.0.1'
clientS = socket(AF_INET, SOCK_DGRAM) 
message = input("Operacioni (IPADDRESS, PORT, COUNT, REVERSE, PALINDROME, TIME, GAME, GCF, CONVERT, ANAGRAM, TITLE)? ")
clientS.sendto(message.encode('utf-8'),(ip, serverPort)) 
modifiedMessage, serverAddress = clientS.recvfrom(2048) 
print(modifiedMessage.decode('utf-8')) 
clientS.close()




