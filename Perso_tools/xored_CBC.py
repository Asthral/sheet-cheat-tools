import argparse
import base64
import random
import hashlib

# Variable
iv = random.randbytes(16)
payload = """X18vXFxcX19fX19fXy9cXFxfX19fX19fXy9cXFxcXF9fX19fX19fX18vXFxcXFxcXFxcX19fX19fXy9cXFxcXFxcXFxcXFxcXFxfX18vXFxcXFxcXFxcXFxcX19fXyAgICAgICAgDQogX1wvLy9cXFxfX18vXFxcL19fX19fX18vXFxcLy8vXFxcX19fX19fL1xcXC8vLy8vLy9cXFxfX19fXC9cXFwvLy8vLy8vLy8vL19fX1wvXFxcLy8vLy8vLy9cXFxfXyAgICAgICANCiAgX19fXC8vL1xcXFxcXC9fX19fX19fL1xcXC9fX1wvLy9cXFxfX19cL1xcXF9fX19fXC9cXFxfX19fXC9cXFxfX19fX19fX19fX19fX1wvXFxcX19fX19fXC8vXFxcXyAgICAgIA0KICAgX19fX19cLy9cXFxcX19fX19fX18vXFxcX19fX19fXC8vXFxcX19cL1xcXFxcXFxcXFxcL19fX19fXC9cXFxcXFxcXFxcXF9fX19fX1wvXFxcX19fX19fX1wvXFxcXyAgICAgDQogICAgX19fX19fXC9cXFxcX19fX19fX1wvXFxcX19fX19fX1wvXFxcX19cL1xcXC8vLy8vL1xcXF9fX19fXC9cXFwvLy8vLy8vX19fX19fX1wvXFxcX19fX19fX1wvXFxcXyAgICANCiAgICAgX19fX19fL1xcXFxcXF9fX19fX1wvL1xcXF9fX19fXy9cXFxfX19cL1xcXF9fX19cLy9cXFxfX19fXC9cXFxfX19fX19fX19fX19fX1wvXFxcX19fX19fX1wvXFxcXyAgIA0KICAgICAgX19fXy9cXFwvLy8vXFxcX19fX19cLy8vXFxcX18vXFxcX19fX19cL1xcXF9fX19fXC8vXFxcX19fXC9cXFxfX19fX19fX19fX19fX1wvXFxcX19fX19fXy9cXFxfXyAgDQogICAgICAgX18vXFxcL19fX1wvLy9cXFxfX19fX1wvLy9cXFxcXC9fX19fX19cL1xcXF9fX19fX1wvL1xcXF9fXC9cXFxcXFxcXFxcXFxcXFxfX1wvXFxcXFxcXFxcXFxcL19fXyANCiAgICAgICAgX1wvLy9fX19fX19fXC8vL19fX19fX19fXC8vLy8vX19fX19fX19cLy8vX19fX19fX19cLy8vX19fXC8vLy8vLy8vLy8vLy8vL19fX1wvLy8vLy8vLy8vLy9fX19fXw=="""
block_len = 16
block_list = []

# Graphique
print("\n")
print(base64.b64decode(payload).decode())
print("\n")
#======================GET KEY======================#
def get_key():                                      #
    password = ((args.password).encode())           #
    md5 = hashlib.md5(password).hexdigest()[:16]    #
    if len(md5) != 16:                              #
        print("error when set password")            #
        exit()                                      #
    print(f"password : {md5}")                      #
    return md5                                      #
#=======================GET DATA=======================#
def get_data():                                        #
    if args.message:                                   #
        data = args.message.encode()                   #
        return data                                    #
    elif args.file:                                    #
        with open(args.file, 'rb') as file:            #
            data = file.read()                         #
        return data                                    #
    else:                                              #
        print("You need to specify a message (-m | --message) or file (-f | --file), use (-h | --help)")
        print("Error when set the data")               #
        exit()                                         #
#=======================GET DATA=======================#
def xor(block1, block2):
    block_list = []
    for i in range(len(block1)):
        block_list.append(block1[i] ^ block2[i])
    return bytes(block_list)

def chiffrement(data: bytes):
    data_encrypt = iv
    for i in range(0, len(data), block_len):
        block = data[i:i + block_len]
        if len(block) != block_len:
            padding = block_len - len(block)
            for i in range(padding):
                block = block + b" "

        block_xor = xor(block, iv)
        block_encrypt = xor(block_xor, password.encode())
        data_encrypt += block_encrypt

    return data_encrypt

def dechiffrement(data_encrypt):
    block_len = 16
    iv = data_encrypt[:block_len]
    block_encrypt = data_encrypt[block_len:]
    data_decrypt = b""

    for i in range(0, len(block_encrypt), block_len):
        block = block_encrypt[i:i + block_len]
        block_xor = xor(block, password.encode())
        block_decrypt = xor(block_xor, iv)
        data_decrypt += block_decrypt

    return data_decrypt.rstrip()

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', dest='file', help="File to encrypt or decrypt")
parser.add_argument('-m', '--message', dest='message', help="Message to encrypt or decrypt")
parser.add_argument('-d', '--decrypt', dest='decrypt', action='store_true', help='Decrypt message or file in XOR with CBC')
parser.add_argument('-e', '--encrypt', dest='encrypt', action='store_true', help='Encrypt message or file in XOR with CBC')
parser.add_argument('-p', '--password', dest='password', required=True, help='Password to encrypt or decrypt the data')
parser.add_argument('-o', '--output', dest='output', required=True, help='Output file after using the tool')
args = parser.parse_args()

#====DATA & PASSWORD====#
password = get_key()    #
data = get_data()       #
#====DATA & PASSWORD====#

if args.message and args.file:
    print("You can't use file (-f | --file) and message (-m | --message) in the same time, use (-h | --help)")

elif not args.message and not args.file:
    print("You need to specify a message (-m | --message) or file (-f | --file), use (-h | --help)")

if args.decrypt and args.encrypt:
    print("You can't decrypt (-d | --decrypt) and encrypt (-e | --encrypt) in the same time, use (-h | --help)")
    exit()

elif args.encrypt:
    result = chiffrement(data)
    print(f"result : {result}")

elif args.decrypt:
    result = dechiffrement(data)
    print(f"result : {result}")

else:
    print("You need to encrypt (-e | --encrypt) or decrypt (-d | --decrypt) your data, use (-h | --help)")
    exit()

print(args.output)
if args.output:
    if result:
        with open(args.output, 'wb') as output:
            output.write(result)
            print(f"file save as {args.output}")
else:
    print("You need to specify an output (-o | --outpout)")
