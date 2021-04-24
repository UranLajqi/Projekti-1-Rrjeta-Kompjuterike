import datetime
import random
from socket import * 
serverPort = 13000 
serverS = socket(AF_INET, SOCK_DGRAM) 
serverS.bind(('', serverPort)) 
print('Serveri eshte gati qe te pranoj kerkesa: ') 

def IDADDRESS(address):
    ip_address = address[0]
    serverS.sendto(("Përgjigjja: IP Adresa e klientit eshte: %s" %ip_address).encode("utf-8"),address)

def PORT():
    serverS.sendto(("Përgjigjja: Klienti eshte duke perdorur portin %s" %address[1]).encode("utf-8"),address)

def TIME():
    metoda = datetime.datetime.now()
    metoda = metoda.strftime("%d.%m.%Y %I:%M:%S %p")
    serverS.sendto(("Përgjigjja: Koha eshte %s " %metoda).encode("utf-8"),address)

def GAME():
    randomlist = random.sample(range(1, 35), 5)
    metoda = randomlist.sort()
    metoda = str(tuple(randomlist))
    serverS.sendto(("Përgjigjja: psh. %s pra 5 numra te rastesishem nga 35" %metoda).encode("utf-8"),address)

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
    serverS.sendto(("Përgjigjja: Fjalia e kthyer ne reverz: %s " %s2).encode("utf-8"),address)

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
    serverS.sendto(("Përgjigjja: Teksti i pranuar permban %s zanore dhe %s bashketingëllore" %(vowels,consonants)).encode("utf-8"),address)

def TITLE(r1):
   x = int(r1.istitle())
   if x == 1:
        serverS.sendto(("Përgjigjja: Teksti i permbahet rregullave te titullit").encode("utf-8"),address)
   else:
        serverS.sendto(("Përgjigjja: Teksti nuk i permbahet rregullave te titullit").encode("utf-8"),address)

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
        serverS.sendto("Përgjigjja: Teksti i dhene eshte palindrome".encode("utf-8"),address)
    else:
        serverS.sendto("Përgjigjja: Teksti i dhene nuk eshte palindrome".encode("utf-8"),address)

def CONVERT(opcioni1,numri1):
    opcioni = opcioni1
    numri = numri1
    if opcioni == "cmToFeet":
      fjaliaP = str(float(numri) / 30.48)
      serverS.sendto(("Përgjigjja: Rezultati i konvertimit: %s ft" %fjaliaP).encode("utf-8"),address)
    elif opcioni == "FeetToCm":
      fjaliaP = str(float(numri) * 30.48)  
      serverS.sendto(("Përgjigjja: Rezultati i konvertimit: %s cm" %fjaliaP).encode("utf-8"),address)
    elif opcioni == "kmToMiles":
      fjaliaP = str(float(numri) / 1.609)
      serverS.sendto(("Përgjigjja: Rezultati i konvertimit: %s miles" %fjaliaP).encode("utf-8"),address)
    elif opcioni == "MileToKm":
      fjaliaP = str(float(numri) * 1.609)
      serverS.sendto(("Përgjigjja: Rezultati i konvertimit: %s km" %fjaliaP).encode("utf-8"),address)
    else:
      serverS.sendto(("Shenoni nje opsion valid").encode("utf-8"),address)

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
    serverS.sendto(("Përgjigjja: Pjestuesi me i madh i perbashket i numrave %s dhe %s eshte %s" %(x,y,hcf)).encode("utf-8"),address)

def ANAGRAM(a1,a2):
    s1=a1
    s2=a2
    if(sorted(s1)==sorted(s2)):
        serverS.sendto(bytes("Përgjigjja: Teksti i dhene eshte anagram.","utf-8"),address)
    else:
        serverS.sendto(bytes("Përgjigjja: Teksti i dhene nuk eshte anagram.","utf-8"),address)

while True:    
    message, address = serverS.recvfrom(2048)    
    print('---------------------------------------')
    print('Klienti u lidh me %s ne portin %s' %address)
    metoda = message
    print('Kerkesa nga klienti:' + str(metoda.decode("utf-8")))

    def listToString(s):  
        str1 = ""  
        for ele in s:  
            str1 = str1  + ele
        return str1
    
    metoda = str(metoda.decode("utf-8")) 
    m = metoda.split(" ")[0]

    if m == "IPADDRESS":
        IDADDRESS(address)

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
        clientS.send(bytes("Nuk keni shenuar asgje","utf-8"))
        clientS.close()

    else:
        clientS.send(bytes("Keni shenuar gabim","utf-8"))
        clientS.close()

    
    

