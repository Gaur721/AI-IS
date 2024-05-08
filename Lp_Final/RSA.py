from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def generate_key_pair(key_size=2048):
    key = RSA.generate(key_size)
    return key

def encrypt_rsa(public_key, plaintext):
    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def decrypt_rsa(private_key, ciphertext):
    cipher = PKCS1_OAEP.new(private_key)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

def main():
    # Generate RSA key pair
    key_pair = generate_key_pair()

    # Get public and private keys
    public_key = key_pair.publickey()
    private_key = key_pair

    # Message to encrypt
    plaintext = b"Hello, World!"

    # Encryption
    ciphertext = encrypt_rsa(public_key, plaintext)
    print("Encrypted:", ciphertext.hex())

    # Decryption
    decrypted_text = decrypt_rsa(private_key, ciphertext)
    print("Decrypted:", decrypted_text.decode())

if __name__ == "__main__":
    main()