
from subprocess import Popen, PIPE

with Popen("ifconfig", stdout=PIPE, encoding="utf8") as ifcfg:
    for line in ifcfg.stdout:
        if 'inet ' in line:
            print(line.split()[1])

