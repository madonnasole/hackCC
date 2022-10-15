def encrypt_cc(original_message, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # key = 3
    # original_message = "I love programming"
    encrypted_message = ""

    original_message = original_message.upper()
    # print(original_message)

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

    # print(encrypted_message)
    return encrypted_message

key = 3
original_message = "I love programming"
encrypted_message = encrypt_cc(original_message, key)
print(encrypted_message)