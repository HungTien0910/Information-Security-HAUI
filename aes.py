from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
import base64

def encrypt_AES(key, data):
    cipher = AES.new(key, AES.MODE_CBC, IV)
    ciphertext = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
    return base64.b64encode(ciphertext), base64.b64encode(IV)

def decrypt_AES(key, ciphertext, IV):
    cipher = AES.new(key, AES.MODE_CBC, base64.b64decode(IV))
    decrypted_data = unpad(cipher.decrypt(base64.b64decode(ciphertext)), AES.block_size)
    return decrypted_data.decode('utf-8')

# Generate a random 16-byte key
key = get_random_bytes(16)

# Generate a random 16-byte Initialization Vector (IV)
IV = get_random_bytes(16)

data = "Hello, world!"
print("Original data:", data)

# Encrypt the data
encrypted_data, IV = encrypt_AES(key, data)
print("Encrypted data:", encrypted_data)

# Decrypt the data
decrypted_data = decrypt_AES(key, encrypted_data, IV)
print("Decrypted data:", decrypted_data)
