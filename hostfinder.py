import socket
try:
    host = input("Enter website name:")
    ip=socket.gethostbyname(host)
    print("Ip address for given",host,"is",ip)


except:
    print("Invalid website")
