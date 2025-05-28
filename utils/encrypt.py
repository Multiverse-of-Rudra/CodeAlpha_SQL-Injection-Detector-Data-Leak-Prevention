import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import base64

class AESEncryptor:
    def __init__(self, key_bytes):
        self.key = key_bytes

    def encrypt(self, plaintext: str) -> str:
        iv = os.urandom(16)
        padder = padding.PKCS7(128).padder()
        data = padder.update(plaintext.encode()) + padder.finalize()
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        ct = encryptor.update(data) + encryptor.finalize()
        return base64.b64encode(iv + ct).decode()

    def decrypt(self, b64_ciphertext: str) -> str:
        raw = base64.b64decode(b64_ciphertext)
        iv, ct = raw[:16], raw[16:]
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        data = decryptor.update(ct) + decryptor.finalize()
        unpadder = padding.PKCS7(128).unpadder()
        return unpadder.update(data) + unpadder.finalize()