import subprocess
try:
    subprocess.run(["pip","install","-r","requirements.txt"])
except:
    print("error occured ")
