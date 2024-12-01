import base64
import socket
import re
import argparse
import time

print('''Enter a number between 1-8 :
[1] Forensic
[2] Crypto
[3] Network
[4] Reverse
[5] Stegano
[6] Web
[7] Osint
[8] Pwn
[0] Exit
''')
put = int(input("> "))

Forensic_paylaod = "X18vXFxcXFxcXFxcXFxcXFxcX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fXyAgICAgICAgCiBfXC9cXFwvLy8vLy8vLy8vL19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fICAgICAgIAogIF9cL1xcXF9fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fXy9cXFxfX19fX19fX19fX19fX18gICAgICAKICAgX1wvXFxcXFxcXFxcXFxfX19fX19fX18vXFxcXFxfX19fXy9cXC9cXFxcXFxcX19fX19fL1xcXFxcXFxcX19fL1xcL1xcXFxcXF9fX18vXFxcXFxcXFxcXF9cLy8vX19fX19fL1xcXFxcXFxcXyAgICAgCiAgICBfXC9cXFwvLy8vLy8vX19fX19fX18vXFxcLy8vXFxcX19cL1xcXC8vLy8vXFxcX19fL1xcXC8vLy8vXFxcX1wvXFxcLy8vL1xcXF9fXC9cXFwvLy8vLy9fX18vXFxcX19fL1xcXC8vLy8vL19fICAgIAogICAgIF9cL1xcXF9fX19fX19fX19fX19fL1xcXF9fXC8vXFxcX1wvXFxcX19fXC8vL19fXy9cXFxcXFxcXFxcXF9fXC9cXFxfX1wvL1xcXF9cL1xcXFxcXFxcXFxfXC9cXFxfXy9cXFxfX19fX19fX18gICAKICAgICAgX1wvXFxcX19fX19fX19fX19fX1wvL1xcXF9fL1xcXF9fXC9cXFxfX19fX19fX19cLy9cXC8vLy8vLy9fX19cL1xcXF9fX1wvXFxcX1wvLy8vLy8vL1xcXF9cL1xcXF9cLy9cXFxfX19fX19fXyAgCiAgICAgICBfXC9cXFxfX19fX19fX19fX19fX1wvLy9cXFxcXC9fX19cL1xcXF9fX19fX19fX19cLy9cXFxcXFxcXFxcX1wvXFxcX19fXC9cXFxfXy9cXFxcXFxcXFxcX1wvXFxcX19cLy8vXFxcXFxcXFxfIAogICAgICAgIF9cLy8vX19fX19fX19fX19fX19fX19cLy8vLy9fX19fX1wvLy9fX19fX19fX19fX19cLy8vLy8vLy8vL19fXC8vL19fX19cLy8vX19cLy8vLy8vLy8vL19fXC8vL19fX19fXC8vLy8vLy8vX18="
Web_paylaod = ""
Pwn_paylaod = ""
Stegano_paylaod = ""
Reverse_paylaod = ""
Network_paylaod = ""
Crypto_paylaod = ""
Osint_paylaod = ""


while put == 0:
    print("ez")
    exit()
if put == 1:
    print(base64.b64decode(Forensic_paylaod).decode())
    print('''\nWhat do you want ?
    [1] Tools
    [2] Lists
    [0] Back
    ''')
    put = int(input("> "))







    
#parser = argparse.ArgumentParser()
#parser.add_argument("-a")
#agrs = parser.parse_args()