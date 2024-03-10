import pyfiglet
import socket
word=pyfiglet.figlet_format("HostFinder")
print(word)
try:
    host = input("Enter website name:")
    ip=socket.gethostbyname(host)
    print("Ip address for",host,ip)


except:
    print("Invalid website")
