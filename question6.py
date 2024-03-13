from aes.aes import AES

Ciphertext = 0x1a7392e3fbdbe317df61d96fb8bc1df2
Key = 0x4a6f736875612053776f726466697368

key = Key.to_bytes(16, 'big')
cipher_text = Ciphertext.to_bytes(16, 'big')
aes = AES(key)

cipher_state = aes.decrypt_block_first_round(cipher_text)
cipher_hex = cipher_state.hex()
print(f'AES block after first round: 0x{cipher_hex}')