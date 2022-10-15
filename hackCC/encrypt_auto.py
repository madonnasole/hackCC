# VARIABLE
# need a variable to store alphabet
# need a variable to store original message
# need a variable to store KEY
# need a variable to store result - encrypted_message

# ALGORITHM
# for every alphabet character inside original message we shift KEY times to the right of alphabet
# w/ character not in alphabet we keep it as is

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = 3
# original_message = "I love programming"
original_message = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
encrypted_message = ""

original_message = original_message.upper()
print(original_message)

for character in original_message:
    new_character = ""
    if character in alphabet:
        original_position = alphabet.find(character)
        new_position = original_position + key
        # //special case
        # // z = 25 --> 28
        # // 28 - 26 = 2
        if new_position > len(alphabet) - 1:
            new_position = original_position + key - len(alphabet)
        new_character = alphabet[new_position]
    else:
        new_character = character
    encrypted_message = encrypted_message + new_character

print(encrypted_message)
