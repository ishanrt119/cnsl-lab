import time
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


for size in [1024, 2048, 3072, 4096]:


   start = time.perf_counter()
   private = rsa.generate_private_key(65537, size)
   public = private.public_key()
   print("\nKey Size:", size, "| Key Generation:", time.perf_counter()-start)


   for n in [64, 128, 256, 512]:


       if n > (size // 8 - 66) * 8:
           print(n, "bit message: Too large")
           continue


       msg = (1 << (n-1)).to_bytes((n+7)//8, 'big')


       pad = padding.OAEP(
           mgf=padding.MGF1(hashes.SHA256()),
           algorithm=hashes.SHA256(),
           label=None
       )


       start = time.perf_counter()
       encrypted = public.encrypt(msg, pad)
       et = time.perf_counter() - start


       start = time.perf_counter()
       decrypted = private.decrypt(encrypted, pad)
       dt = time.perf_counter() - start


       print(n, "bit | Encryption:", et,
             "| Decryption:", dt,
             "| Correct:", msg == decrypted)



