import json
from os import urandom

import blowfish

config = {
    'CIPHER_key' : b'\xf4\'\xc3(L\xd0\xcfD"B/g', 
    'initialization_vector' : b'7Cp\x95\x85\x029#',
}


class BlowfishException(werkzeug.exceptions.BadRequest):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return str(self.message)


class Blowfish:
    AVAILABLE_MODES = ['cbc_cts', 'cfb', 'ofb', 'ecb_cts']
    DEFAULT_MODE = 'cbc_cts'
    CIPHER = blowfish.Cipher(config['CIPHER_key'])
    IV = config['initialization_vector']

    #This shouldn't really be called directly - it's just a way to shorten code. 
    #Rather just use encrypt_data() and decrypt_data()
    @staticmethod
    def _handle_data(action, data, mode = None):
        if not mode: mode = Blowfish.DEFAULT_MODE

        elif mode not in Blowfish.AVAILABLE_MODES: 
            raise BlowfishException('Mode not supported: ' + str(mode))

        if action not in ['encrypt', 'decrypt']:
            raise BlowfishException("Called _handle_data() with action: ' + str(action) + '. Must be `encrypt` or `decrypt`. Protip: You probably shouldn't directly call _handle_data. ")

        action = '%s_%s' % (action, mode)

        #There might be a better way to implement this, which will also allow us to support multiple modes. 
        args = [data, Blowfish.IV]
        if mode == 'ecb_cts' : 
            args = [data]

        handled_data = b"".join(getattr(Blowfish.CIPHER, action)(*args))
        return handled_data

    @staticmethod
    def encrypt(data, mode = None):
        data = data.encode('utf-8')
        encrypted_data = Blowfish._handle_data('encrypt', data, mode)
        encrypted_data = encrypted_data.hex()
        return encrypted_data

    @staticmethod
    def decrypt(data, mode = None):
        data = bytes.fromhex(data)
        decrypted_data = Blowfish._handle_data('decrypt', data, mode)
        print ('Data : ', decrypted_data)
        try:
            decrypted_data = decrypted_data.decode('utf-8')
        except UnicodeDecodeError:
            return str(decrypted_data)
        return decrypted_data
