'''Caesar Cipher'''
alphabet=['a', 'b' ,'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
         'k', 'l', 'm', 'n', 'o', 'b', 'q', 'r', 's', 't',
          'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b' ,'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
         'k', 'l', 'm', 'n', 'o', 'b', 'q', 'r', 's', 't',
          'u', 'v', 'w', 'x', 'y', 'z' ]


def ceasar(start_text, shift_amount, cipher_direction):
    end_text=""
    if cipher_direction =='decode':
            shift_amount *= -1
    for letter in start_text:
        if letter.isalpha():
            position= alphabet.index(letter)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"Here's the {direction}d result: {end_text}")


should_continue= True
while should_continue :
    direction= input("Type 'encod' to encrypt, type 'decode' to decrypt:\n")
    text= input("Type your message:\n") .lower()
    shift= int(input("Type the shift number:\n"))
    shift = shift % 26
    ceasar(text, shift, direction)

    result = input("Type 'yes' if you want to go again, Otherwise type 'no'. ")
    if result == 'no':
        should_continue = False
        print("Goodbye")




def encrypt(plain_text, shift_amount):
    cipher_text= ""
    for char in text:
        if char.isalpha():
            ind= alphabet.index(char)
            new_ind= ind + shift
            cipher_text += alphabet[new_ind]
        else:
            cipher_text += char
    print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift_amount):
    text= ""
    for char in cipher_text:
        if char.isalpha():
            ind = alphabet.index(char) + 26
            new_ind= ind - shift_amount
            text += alphabet[new_ind]
        else:
            text += char
    print(f"The decoded text is {text}")


