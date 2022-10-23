from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

class Des:
    KEY = 'hello123'

    @staticmethod
    def encrypt(text: str, key: str = KEY):
        key_bytes = bytes(key, 'utf-8')
        text_bytes = bytes(text, 'utf-8')

        cipher = DES.new(key_bytes, DES.MODE_ECB)
        ciphertext = cipher.encrypt(pad(text_bytes, 8))
        return ciphertext.hex()
    
    @staticmethod
    def decrypt(data: str, key: str = KEY):
        key_bytes = bytes(key, 'utf-8')
        data_bytes = bytes.fromhex(data)

        cipher = DES.new(key_bytes, DES.MODE_ECB)
        plaintext = unpad(cipher.decrypt(data_bytes), 8)

        try:
            plaintext = plaintext.decode('utf-8')
        except UnicodeDecodeError:
            return str(plaintext)
        return plaintext