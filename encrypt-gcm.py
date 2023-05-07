import sys
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

# entradas: primeiro o texto a ser cifrado, segundo a chave a ser utilizada na cifragem

# texto a ser cifrado, valor default eh "Cin/Embraer Security"
if len(sys.argv) > 1:
    texto_plano = sys.argv[1]
else:
    texto_plano = "CIn/Embraer Security"
# chave a ser utilizada na cifragem, valor default eh "chave_cifra_gcm"
if len(sys.argv) > 2:
    chave = sys.argv[2]
else:
    chave = "chave_cifra_gcm"

# com o texto plano e a chave, tranforma as strings do texto e da chave em uma sequencia de bytes 
# e entao transforma a chave em um hash de 256 bits, ambas transformacoes para o correto 
# funcionamento do algoritmo de cifragem e de hash
texto_plano = texto_plano.encode()
chave = chave.encode()
chave = SHA256.new(chave).digest()

# realiza a cifragem do texto plano
gcm = AES.new(chave, AES.MODE_GCM)
texto_cifrado = gcm.encrypt(texto_plano)
print(f"texto cifrado, encode em base64 = {b64encode(texto_cifrado).decode('utf-8')}")
print(f"nonce, encode em base64 = {b64encode(gcm.nonce).decode('utf-8')}")
