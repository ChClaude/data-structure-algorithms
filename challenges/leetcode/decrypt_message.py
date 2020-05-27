
def decrypt_secret_message(secret_message):
    # TODO: Implement this method.
    #       Every character in a string has a corresponding ASCII value which is an int. For example A=65, B=66, C=67 and so on.
    #
    #       For each character in the secretMessage get the numeric value:
    #       - if the numeric value is an even number, subtract 1 from it and append the new character value to 'message'
    #       - if the numeric value is an odd number, add 1 to it and append the new character value to 'message'
    #
    #       Example: ABC (65,66,67) will become BAD (66,65,68)

    message_nums = [ord(letter) for letter in secret_message]
    message_new_nums = [num - 1 if num % 2 == 0 else num + 1 for num in message_nums]
    message = ''.join([chr(num) for num in message_new_nums])

    return message
