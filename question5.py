from aes.aes import AES, pad

key = pad(b'this is my key') # need to pad to 16, 24, or 32 bytes
iv = pad(b'this is my iv') # need to pad to 16 bytes

cipher_text = AES(key).encrypt_cbc(b'this is my plain text for question 5', iv)
print(cipher_text)

plain_text = AES(key).decrypt_cbc(cipher_text, iv)
print(plain_text)