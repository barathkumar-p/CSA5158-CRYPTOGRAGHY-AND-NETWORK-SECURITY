vernam_dict = dict((i, chr(i + 96)) for i in range(1, 27))
def vernam_encrypt(plain, key):
    plain = plain.lower()
    ckey = ''.join([(key[i % len(key)]) for i in range(len(list(plain)))])
    print(ckey)
    cipher = ''
    for i in range(len(plain)):
        if plain[i] == ' ':
            cipher += ' '
        else:
            cipher += vernam_dict[(ord(plain[i]) + ord(ckey[i])) % 26]
    print(cipher, plain)

plaintext=input("ENter the plain text:")
keyword=input("ENter the key:")

print(vernam_encrypt(plaintext,keyword))