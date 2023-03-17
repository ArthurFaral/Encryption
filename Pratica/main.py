import random
import string

##crypt = string.whitespace + string.punctuation + string.digits + string.ascii_letters
crypt = " " + string.punctuation + string.digits + string.ascii_letters
##crypt = "0123456789abcdefghijklmnopqrstuvxwyzABCDEFGHIJKLMONPQRSTUVXWYZ"

crypt = list(crypt)
key = crypt.copy()

random.shuffle(key)

# print(f"crypt; {crypt}")
# print(f"key : {crypt}")


## Encrypt

plain_text = input("Enter a massage to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = crypt.index(letter)
    cipher_text += key[index]

print(f"Mensagem original: {plain_text}")
print(f"Mensagem Encriptada: {cipher_text}")


## Dencrypt

cipher_text = input("Enter a massage to encrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += crypt[index]

print(f"Mensagem Encriptada: {cipher_text}")
print(f"Mensagem original: {plain_text}")