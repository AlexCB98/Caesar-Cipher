from ascii_art import logo
print(logo)

lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
digits = ['0','1','2','3','4','5','6','7','8','9']

def caesar(encode_or_decode, original_text, shift_amount):

    cipher_text = ''

    if encode_or_decode == 'decode':
        shift_amount *= -1

    for letter in original_text:
        if letter in lowercase:
            shifted_position = lowercase.index(letter) + shift_amount
            shifted_position %= len(lowercase)
            cipher_text += lowercase[shifted_position]
        elif letter in uppercase:
            shifted_position = uppercase.index(letter) + shift_amount
            shifted_position %= len(uppercase)
            cipher_text += uppercase[shifted_position]
        elif letter in digits:
            shifted_position = digits.index(letter) + shift_amount
            shifted_position %= len(digits)
            cipher_text += digits[shifted_position]
        else:
            cipher_text += letter
    print(f'Your cipher text is: {cipher_text}')

again = 'yes'

while again == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    caesar(encode_or_decode = direction, original_text = text, shift_amount = shift)
    again = input('Type "yes" if you want to continue or "no" if you want to stop:\n').lower()


print("Thanks for using Caesar Cipher. Goodbye! ^^")
