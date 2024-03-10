import subprocess
try:
    subprocess.call([sys.executable, "-m","pip","install","-r","requirements.txt"])
except:
    print("error occured ")
