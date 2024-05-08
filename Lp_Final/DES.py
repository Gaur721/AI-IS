from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

def encrypt_des(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_plaintext = _pad(plaintext)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def decrypt_des(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = cipher.decrypt(ciphertext)
    return _unpad(decrypted_text)

def _pad(plaintext):
    padding_length = 8 - (len(plaintext) % 8)
    return plaintext + bytes([padding_length] * padding_length)

def _unpad(padded_text):
    padding_length = padded_text[-1]
    return padded_text[:-padding_length]

def main():
    key = get_random_bytes(8)  # 64-bit key
    plaintext = b"Hello, World!"

    # Encryption
    ciphertext = encrypt_des(key, plaintext)
    print("Encrypted:", ciphertext.hex())

    # Decryption
    decrypted_text = decrypt_des(key, ciphertext)
    print("Decrypted:", decrypted_text.decode())

if __name__ == "__main__":
    main()