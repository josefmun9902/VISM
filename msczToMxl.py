import subprocess, sys

def convertFile(currentpath):
    p = subprocess.Popen(["powershell.exe", "C:\\Users\\Josef\\Desktop\\VISM-main\\convert.ps1"], stdout=sys.stdout)
    p.communicate()