alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrpt(text, shift):
    encrypted_text = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift) % 25  
            encrypted_text += alphabet[new_position]
        else:
            encrypted_text += letter
    
    print(f"The encoded text is {encrypted_text}")

def decrypt(text, shift):
    decrypted_text = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position - shift) % 25  
            decrypted_text += alphabet[new_position]
        else:
            decrypted_text += letter
    
    print(f"The decoded text is {decrypted_text}")


if direction == "encode":
    encrpt(text, shift)
else:
    decrypt(text, shift)
    