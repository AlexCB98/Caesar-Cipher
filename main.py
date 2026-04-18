alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

try_again = 'yes'
while try_again == 'yes':
     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
     text = input("Type your message:\n").lower()
     shift = int(input("Type the shift number:\n"))

     caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
     try_again = input('Type "yes" if you want to repeat or "no" to exit:\n ').lower()

print('Goodbye!')
