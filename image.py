
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

# Generate secret key
key = AESGCM.generate_key(bit_length=256)
aes = AESGCM(key)

# Read image
path = input("Enter image path: ")
with open(path, "rb") as f:
    image = f.read()

# Encrypt image
nonce = os.urandom(12)
encrypted = aes.encrypt(nonce, image, None)

with open("encrypted.bin", "wb") as f:
    f.write(nonce + encrypted)

print("\nImage Encrypted Successfully!")

# Decrypt image
try:
    data = open("encrypted.bin", "rb").read()
    decrypted = aes.decrypt(data[:12], data[12:], None)

    with open("decrypted_image.png", "wb") as f:
        f.write(decrypted)

    print("Image Decrypted Successfully!")
    print("Saved as decrypted_image.png")

except Exception:
    print("Decryption Failed! Data Tampered or Wrong Key.")



