**Chiffrement et déchiffrement en XOR avec algo CBC**

__/\\\_______/\\\________/\\\\\__________/\\\\\\\\\_______/\\\\\\\\\\\\\\\___/\\\\\\\\\\\\____        
 _\///\\\___/\\\/_______/\\\///\\\______/\\\///////\\\____\/\\\///////////___\/\\\////////\\\__       
  ___\///\\\\\\/_______/\\\/__\///\\\___\/\\\_____\/\\\____\/\\\______________\/\\\______\//\\\_      
   _____\//\\\\________/\\\______\//\\\__\/\\\\\\\\\\\/_____\/\\\\\\\\\\\______\/\\\_______\/\\\_     
    ______\/\\\\_______\/\\\_______\/\\\__\/\\\//////\\\_____\/\\\///////_______\/\\\_______\/\\\_    
     ______/\\\\\\______\//\\\______/\\\___\/\\\____\//\\\____\/\\\______________\/\\\_______\/\\\_   
      ____/\\\////\\\_____\///\\\__/\\\_____\/\\\_____\//\\\___\/\\\______________\/\\\_______/\\\__  
       __/\\\/___\///\\\_____\///\\\\\/______\/\\\______\//\\\__\/\\\\\\\\\\\\\\\__\/\\\\\\\\\\\\/___ 
        _\///_______\///________\/////________\///________\///___\///////////////___\////////////_____

usage: ok.py [-h] [-f FILE] [-m MESSAGE] [-d] [-e] -p PASSWORD -o OUTPUT

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  File to encrypt or decrypt
  -m MESSAGE, --message MESSAGE
                        Message to encrypt or decrypt
  -d, --decrypt         Decrypt message or file in XOR with CBC
  -e, --encrypt         Encrypt message or file in XOR with CBC
  -p PASSWORD, --password PASSWORD
                        Password to encrypt or decrypt the data
  -o OUTPUT, --output OUTPUT
                        Output file after using the tool