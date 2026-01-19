alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# -------------------------------------------------

# Encryption

# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

def encrypt(original_text , shift_amount):
    cipher_text = ""

    # TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' 
    # forwards in the alphabet by the shift amount and print the encrypted text.

    for char in original_text:
        shifted_amount = alphabet.index(char) + shift_amount
        
        # TODO-3: What happens if you try to shift z forwards by 9? Can you fix the code?

        shifted_amount %= len(alphabet) # It will keep the shift range from 0 to 25

        cipher_text += alphabet[shifted_amount]

    print(cipher_text)

# TODO-4: Call the 'encrypt()' function and pass in the user inputs. 
# You should be able to test the code and encrypt a message.

encrypt(original_text = text,shift_amount = shift)

# -------------------------------------------------

# Decryption

# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* 
# in the alphabet by the shift amount and print the decrypted text.

def decrypt(original_text , shift_amount):
    decrypt_text = ""

    for char in original_text:
        shifted_amount = alphabet.index(char) + shift_amount
        
        # TODO-3: What happens if you try to shift z forwards by 9? Can you fix the code?

        shifted_amount %= len(alphabet) # It will keep the shift range from 0 to 25

        decrypt_text += alphabet[shifted_amount]

    print(decrypt_text)

decrypt(original_text = text , shift_amount = shift)

