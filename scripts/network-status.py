import subprocess

output = subprocess.check_output("nmcli -t -f name connection show --active", shell=True)                               
print("\uf1eb  " + output[:-1].decode())
