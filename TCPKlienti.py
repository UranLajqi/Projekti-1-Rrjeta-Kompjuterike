import socket
import sys, time
def main():
    target_host = '127.0.0.1'
    target_port = 13000
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print('Nuk mund te krijohej soketi')
        time.sleep(1)
        sys.exit()
    try:
        client.connect((target_host, target_port))
    except socket.error:
        print('Nuk mund te konektohej te serveri')
        time.sleep(1)
        sys.exit()
    online = True
    while online:
        data = input("Operacioni (IPADDRESS, PORT, COUNT, REVERSE, PALINDROME, TIME, GAME, GCF, CONVERT, ANAGRAM, TITLE)? ")
        client.sendall(data.encode("utf-8"))
        while True:
            message = client.recv(4096)
            print(message.decode("utf-8"))
            break
main()