
def encrypt(text, key):
    result = []

    for i in range(len(text)):
        p = ord(text[i])
        k = ord(key[i % len(key)])

        c = (p + k) % 256
        e = c ^ k

        result.append(e)

    return bytes(result)


def decrypt(cipher, key):
    result = ""

    for i in range(len(cipher)):
        e = cipher[i]
        k = ord(key[i % len(key)])

        c = e ^ k
        p = (c - k) % 256

        result += chr(p)

    return result


# Main program
message = input("Enter plaintext: ")
key = input("Enter secret key: ")

cipher = encrypt(message, key)

print("Encrypted Text (Hex):", cipher.hex())

decrypted = decrypt(cipher, key)

print("Decrypted Text:", decrypted)


