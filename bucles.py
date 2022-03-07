from cgi import print_environ
from ssl import OPENSSL_VERSION_INFO
from unicodedata import bidirectional


numero = 1
cantidad = 0
while(numero <= 100):
    cantidad += numero
    numero += 13
    
print(cantidad)
