alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = 3
original_message = ""
encrypted_message = "L ORYH SURJUDPPLQJ"
encrypted_message = encrypted_message.upper()

for encrypted_character in encrypted_message:

    original_character = ""

    if encrypted_character in alphabet:
        encrypted_character_pos = alphabet.find(encrypted_character)
        original_character_pos = encrypted_character_pos - key
        # special case when encrypted_character_pos < key
        if original_character_pos < 0:
            original_character_pos = original_character_pos + len(alphabet)

        original_character = alphabet[original_character_pos]
    else:
        original_character = encrypted_character

    original_message = original_message + original_character

print(original_message)
