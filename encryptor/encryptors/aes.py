from Crypto.Cipher import AES

class Aes:
    KEY = 'pure mathematics' # 16 byte key

    @staticmethod
    def encrypt(text: str, key: str = KEY):
        key_bytes = bytes(key, 'utf-8')
        text_bytes = bytes(text, 'utf-8')

        cipher = AES.new(key_bytes, AES.MODE_EAX)
        nonce = cipher.nonce
        ciphertext, tag = cipher.encrypt_and_digest(text_bytes)
        return ciphertext.hex(), nonce.hex()
    
    @staticmethod
    def decrypt(data: str, key: str = KEY, nonce: str = None):
        key_bytes = bytes(key, 'utf-8')
        data_bytes = bytes.fromhex(data)
        nonce_bytes = bytes.fromhex(nonce)

        cipher = AES.new(key_bytes, AES.MODE_EAX, nonce=nonce_bytes)
        plaintext = cipher.decrypt(data_bytes)

        try:
            plaintext = plaintext.decode('utf-8')
        except UnicodeDecodeError:
            return str(plaintext)
        return plaintext