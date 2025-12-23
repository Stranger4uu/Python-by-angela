alphabet = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt : ").lower()
text = input("Type your message : ").lower()
shift = int(input("Type the shift number : "))


# def caesar(original_text, shift_amount, encode_or_decode):
#     output_text = ""

#     for letter in original_text:
#         if letter in alphabet:
#             if encode_or_decode == "decode":
#                 shifted_position = alphabet.index(letter) - shift_amount
#             else:  # encode
#                 shifted_position = alphabet.index(letter) + shift_amount

#             shifted_position %= len(alphabet)
#             output_text += alphabet[shifted_position]
#         else:
#             output_text += letter  # keep spaces/symbols as it is

#     print(f"Here is the {encode_or_decode}d result : {output_text}")


# caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)



def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    for letter in original_text:
        if encode_or_decode =="decode":
            shift_amount *= -1
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result : {output_text}")


caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
