alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


def encrypt(plain_text, shift_amount):
  cipher_text_list = []
  for letter in plain_text:
    new_index = alphabet.index(letter) + shift_amount
    print(new_index)
    cipher_text_list.append(alphabet[new_index])

  cipher_text_string = ''.join(cipher_text_list)
  print(f"The encoded text is {cipher_text_string}")
  
def decrypt(cipher_text, shift_amount):
  plain_text_list = []
  for letter in cipher_text:
    new_index = alphabet.index(letter) - shift_amount
    print(new_index)
    plain_text_list.append(alphabet[new_index])

  plain_text_string = ''.join(plain_text_list)
  print(f"The encoded text is {plain_text_string}")


if direction == "encode":
  encrypt(plain_text = text, shift_amount = shift)
elif direction == "decode":
  decrypt(cipher_text = text, shift_amount = shift)