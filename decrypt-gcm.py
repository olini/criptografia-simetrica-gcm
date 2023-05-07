import sys
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

# entradas: primeiro o texto cifrado codificado em base64, segundo a chave de cifragem,
# terceiro o nonce utilizado pelo algoritmo no momento da cifragem tambem codificado em base64

# inicialmente, checa se todos os argumentos foram passados
if len(sys.argv) != 4:
    raise RuntimeError(
        "Numero de argumentos passados invalido. Devem ser informados o texto cifrado codificado "
        "em base64, a chave, e o nonce utilizado na cifragem tambem em base64, obrigatoriamente "
        "nesta ordem."
    )
texto_cifrado = sys.argv[1]
chave = sys.argv[2]
nonce = sys.argv[3]

# realiza a decodificacao em base64 do texto cifrado e do nonce, e transforma a chave em uma 
# sequencia de bytes para entao ser transformada em um hash de 256 bits
# todas essas operacoes sao para o correto funcionamento do algoritmo de decifragem
texto_cifrado = b64decode(texto_cifrado)
nonce = b64decode(nonce)
chave = chave.encode()
chave = SHA256.new(chave).digest()

# realiza a decifragem do texto
gcm = AES.new(chave, AES.MODE_GCM, nonce=nonce)
texto_decifrado = gcm.decrypt(texto_cifrado)
print(texto_decifrado)