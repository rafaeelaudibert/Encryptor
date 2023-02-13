import math
from flask import jsonify

class Transposition:

    @staticmethod
    def encrypt(key, message):
        ciphertext = [] 
        for col in range(key):
            position = col
            while position < len(message):
                ciphertext.append(message[position])
                position += key
        return ''.join(ciphertext)

    @staticmethod
    def decrypt(key, message):
        numOfRows = math.ceil(len(message) / key)
        plaintext = []
        cipher = [*message]
        remainder = len(message)%key
        count=0
        if(remainder != 0):
            for i in range(0,len(message),numOfRows):
                count += 1
                if(count > remainder):
                    cipher.insert(i+numOfRows-1,'#')
            cipher.append('#')
            for row in range(numOfRows):
                position = row
                while(position < len(cipher)):
                    plaintext.append(cipher[position])
                    position += numOfRows
            plaintext = [ele for ele in plaintext if ele != '#']
        else:
            for row in range(numOfRows):
                position = row
                while(position < len(message)):
                    plaintext.append(message[position])
                    position += numOfRows
        return ''.join(plaintext)