s = input("The operation to be done:\n")
plain_text =cipher_text= input("Type your text:\n")
key = input("Type the key here:\n")

def letter_to_number(c):
    if c.islower():
        return ord(c.lower()) - ord('a')
    else :
        return ord(c.upper()) - ord('A')
def number_to_letter(n):
        return chr(n % 26 + ord('A'))

def repeat_string(key, plain_text):
    number_of_repeats = plain_text // len(key) + 1
    a_string_repeated = key * number_of_repeats
    a_string_repeated_to_target = a_string_repeated[:plain_text]
    return a_string_repeated_to_target
repeated_string = repeat_string(key, len(plain_text))

if s == "encrypt":
    def encrypt_letter(repeated_string, plaintext):
        if plaintext == " ": return plaintext
        repeated_string = letter_to_number(repeated_string)
        plaintext = letter_to_number(plaintext)
        return number_to_letter((plaintext + repeated_string) % 26)


    def encrypt(repeated_string, plaintext):
        return "".join(encrypt_letter(k, p) for (k, p) in zip(repeated_string, plaintext))


    print(encrypt(repeated_string, plain_text))


elif s == "decrypt":
    def decrypt_letter(repeated_string, cipher_text):
        if cipher_text == " ": return cipher_text
        repeated_string = letter_to_number(repeated_string)
        cipher_text = letter_to_number(cipher_text)
        return number_to_letter((cipher_text - repeated_string + 26) % 26)


    def decrypt(repeated_string, cipher_text):
        return "".join(decrypt_letter(h, i) for (h, i) in zip(repeated_string, cipher_text))


    print(decrypt(repeated_string, cipher_text))


else : print("Not possible")
