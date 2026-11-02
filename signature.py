

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


# Generate RSA keys
private = rsa.generate_private_key(65537, 2048)
public = private.public_key()


# Input message
msg = input("Enter tender message: ").encode()


# Sign message using private key
signature = private.sign(
   msg,
   padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
               salt_length=padding.PSS.MAX_LENGTH),
   hashes.SHA256()
)


print("\nDigital Signature Generated!")


# Verify original message
try:
   public.verify(signature, msg,
       padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                   salt_length=padding.PSS.MAX_LENGTH),
       hashes.SHA256())
   print("Original Message: Signature Verified!")
except Exception:
   print("Original Message: Verification Failed!")


# Modify message and verify again
modified = msg + b" Modified"


try:
   public.verify(signature, modified,
       padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                   salt_length=padding.PSS.MAX_LENGTH),
       hashes.SHA256())
   print("Modified Message: Signature Verified!")
except Exception:
   print("Modified Message: Verification Failed!")
   print("Message has been tampered with!")




