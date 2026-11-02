
import hashlib

# Original message
text = input("Enter a message: ")

# Calculate SHA-1 digest
hash1 = hashlib.sha1(text.encode()).hexdigest()

print("\nOriginal Message:", text)
print("SHA-1 Digest:", hash1)

# Modify the message
modified_text = text + "1"

# Calculate modified digest
hash2 = hashlib.sha1(modified_text.encode()).hexdigest()

print("\nModified Message:", modified_text)
print("Modified SHA-1 Digest:", hash2)

# Compare hashes
if hash1 == hash2:
    print("\nMessages are same")
else:
    print("\nMessages are different")
    print("Change detected! Integrity verification failed.")


