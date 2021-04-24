import socket
from threading import Thread
import random
import time

class Server: 
    def __init__(self, host, port): 
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(5)

    def listen_for_clients(self):
        print('Serveri eshte duke pritur kerkesen: ')
        while True:
            client, addr = self.server.accept()
            print(
                'Eshte pranuar kerkesa nga: ' + str(addr[0]) + ':' + str(addr[1])
            )
            Thread(target=self.handle_client, args=(client, addr)).start()

    def handle_client(self, client_socket, address):

        def IDADDRESS():
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)
            print('Kalkulimi nga serveri: ' + str(ip_address))
            client_socket.send(("Përgjigjja: IP Adresa e klientit eshte: %s" %ip_address).encode("utf-8"))

        def PORT():
            client_socket.send(("Përgjigjja: Klienti eshte duke perdorur portin %s" %address[1]).encode("utf-8"))

        def TIME():
            metoda = time.localtime()
            metoda = time.strftime("%d.%m.%Y %I:%M:%S %p", metoda)
            client_socket.send(("Përgjigjja: Koha eshte %s " %metoda).encode("utf-8"))

        def GAME():
            randomlist = random.sample(range(1, 35), 5)
            metoda = randomlist.sort()
            metoda = str(tuple(randomlist))
            client_socket.send(("Përgjigjja: psh. %s pra 5 numra te rastesishem nga 35" %metoda).encode("utf-8"))

        def REVERZ(r1):
            s2 = r1
            def reverse(string): 
                string = string[::-1] 
                return string
            def listToString(s):  
                str1 = ""  
                for ele in s:  
                    str1 = str1  + ele + " " 
                return str1  
            s2 = metoda.split(" ")[1::]
            s2 = listToString(s2)
            s2 = reverse(s2).strip()
            client_socket.send(("Përgjigjja: Fjalia e kthyer ne reverz: %s " %s2).encode("utf-8"))

        def COUNT(r1):
            f1 = r1
            f1 = str(metoda.split(" ")[0])
            def listToString(s):  
                str1 = ""  
                for ele in s:  
                    str1 = str1  + ele + " " 
                return str1  
            f2 = metoda.split(" ")[1::]
            f2 = listToString(f2)
            vowels = 0
            consonants = 0
            for i in f2:
                if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
                   or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
                    vowels = vowels + 1
                elif i == ' ':
                    continue
                else:
                    consonants = consonants + 1
            client_socket.send(("Përgjigjja: Teksti i pranuar permban %s zanore dhe %s bashketingëllore" %(vowels,consonants)).encode("utf-8"))

        def TITLE(r1):
           x = int(r1.istitle())
           if x == 1:
                client_socket.send(("Përgjigjja: Teksti i permbahet rregullave te titullit").encode("utf-8"))
           else:
                client_socket.send(("Përgjigjja: Teksti nuk i permbahet rregullave te titullit").encode("utf-8")) 

        def PALINDROME(r1):
            string = r1
            def listToString(s):  
                str1 = ""  
                for ele in s:  
                    str1 = str1  + ele
                return str1  
            string = metoda.split(" ")[1::]
            string = listToString(string)
            if(string==string[::-1]):
                  client_socket.send("Përgjigjja: Teksti i dhene eshte palindrome".encode("utf-8")) 
            else:
                  client_socket.send("Përgjigjja: Teksti i dhene nuk eshte palindrome".encode("utf-8"))

        def CONVERT(opcioni1,numri1):
            opcioni = opcioni1
            numri = numri1
            if opcioni == "cmToFeet":
              fjaliaP = str(float(numri) / 30.48)
              client_socket.send(("Përgjigjja: Rezultati i konvertimit: %s ft" %fjaliaP).encode("utf-8"))
            elif opcioni == "FeetToCm":
              fjaliaP = str(float(numri) * 30.48)   
              client_socket.send(("Përgjigjja: Rezultati i konvertimit: %s cm" %fjaliaP).encode("utf-8"))
            elif opcioni == "kmToMiles":
              fjaliaP = str(float(numri) / 1.609)
              client_socket.send(("Përgjigjja: Rezultati i konvertimit: %s miles" %fjaliaP).encode("utf-8"))
            elif opcioni == "MileToKm":
              fjaliaP = str(float(numri) * 1.609)
              client_socket.send(("Përgjigjja: Rezultati i konvertimit: %s km" %fjaliaP).encode("utf-8"))
            else:
              fjaliaP = "Shenoni nje opsion valid"
              client_socket.send(("Përgjigjja: Rezultati i konvertimit: %s " %fjaliaP).encode("utf-8"))

        def GCF(k1,k2):
            x = k1
            y = k2
            if x > y:
                smaller = y
            else:
                smaller = x
            for i in range(1, smaller+1):
                if((x % i == 0) and (y % i == 0)):
                    hcf = i
            client_socket.send(("Përgjigjja: Pjestuesi me i madh i perbashket i numrave %s dhe %s eshte %s" %(x,y,hcf)).encode("utf-8"))
        
        def ANAGRAM(a1,a2):
            s1=a1
            s2=a2
            if(sorted(s1)==sorted(s2)):
                client_socket.send(bytes("Përgjigjja: Teksti i dhene eshte anagram.","utf-8"))
            else:
                client_socket.send(bytes("Përgjigjja: Teksti i dhene nuk eshte anagram.","utf-8"))
        size = 1024
        while True:
            try:
                data = client_socket.recv(size)
                def listToString(s):  
                    str1 = ""  
                    for ele in s:  
                        str1 = str1  + ele
                    return str1
                
                metoda = str(data.decode("utf-8")) 
                m = metoda.split(" ")[0]

                if m == "IPADDRESS":
                    IDADDRESS()

                elif m == "PORT":
                    PORT()

                elif m == "TIME":
                    TIME()

                elif m == "GAME":
                    GAME()

                elif m == "REVERZ":
                    k1 = str(metoda.split(" ")[1])
                    REVERZ(k1)

                elif m == "COUNT":
                    c1 = str(metoda.split(" ")[1])
                    COUNT(c1)

                elif m == "PALINDROME":
                    l1 = str(metoda.split(" ")[1])
                    PALINDROME(l1)

                elif m == "TITLE":
                    v1 = str(metoda.split(" ")[1::])
                    TITLE(v1)

                elif m == "CONVERT":
                    opcioni1 = str(metoda.split(" ")[1])
                    numri1 = float(metoda.split(" ")[2]) 
                    CONVERT(opcioni1,numri1)

                elif m == "GCF":
                    k1 = int(metoda.split(" ")[1])
                    k2 = int(metoda.split(" ")[2])
                    GCF(k1,k2)

                elif m == "ANAGRAM":
                    a1 = metoda.split(" ")[1]
                    a1 = listToString(a1)
                    a2 = metoda.split(" ")[2]
                    a2 = listToString(a2)
                    ANAGRAM(a1,a2)

                elif m == ' ':
                    client_socket.sendall(bytes("Nuk keni shenuar asgje","utf-8"))
                    client_socket.close()

                else:
                    client_socket.sendall(bytes("Keni shenuar gabim","utf-8"))
                    client_socket.close()

                if 'q^' in data.decode("utf-8"):    
                    print('Eshte pranuar kerkesa per te dale(exit): ' + str(
                        address[0]) + ':' + str(address[1]))
                    break

                else:
                    # send getting after receiving from client
                    print('Eshte pranuar kerkesa: ' + data.decode() + ' nga: ' + str(
                        address[0]) + ':' + str(address[1]))

            except socket.error:
                client_socket.close()
                return False
        client_socket.sendall(
            'Jane pranuar kerkesat per te dale(exit).'.encode("utf-8")
        )
        # send quit message to client too
        client_socket.sendall(
            'q^'.encode("utf-8")
        )
        client_socket.close()
if __name__ == "__main__":
    host = '127.0.0.1'
    port = 13000
    main = Server(host, port)
    # start listening for clients
    main.listen_for_clients()