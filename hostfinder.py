import socket
import subprocess

try:
    import pyfiglet
except ImportError:
    try:
        subprocess.run(["pip","install","-r","requirements.txt"])
        import pyfiglet
    except:
        print("error occured")
except:
    print("error occured")

word=pyfiglet.figlet_format("HostFinder")
print(word)
try:
    host = input("Enter website name:")
    ip=socket.gethostbyname(host)
    print("Ip address for",host,ip)


except:
    print("Invalid website")
