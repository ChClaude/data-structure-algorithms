# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


# Implementation
def navigate(directions):
    x = 0
    y = 0

    # TODO: Implement this method.
    #       - Each character in "directions" determines a change in the X or Y value.
    #       - The characters U (up), D (down), L (left) and R (right). Any other character may be ignored.

    for letter in directions:
        if letter == 'U':
            y += 1
        elif letter == 'D':
            y -= 1
        elif letter == 'L':
            x -= 1
        elif letter == 'R':
            x += 1

    return x, y


def decrypt_secret_message(secret_message):
    message = ""

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

"""
def get_secret_message(x, y):
    messages = [
        ["Mps\u001Fsgjt\u001Fpmf\"", "Mps\u001Fsgjt\u001Fpmf\u001Ffjsgfq\"", "Xqpmh\u001Fpmf\"\u001FPpot\"",
         "Lffo\u001Fkppljmh\""],
        ["Sgjt\u001Fjt\u001Fmps\u001Fjs\"", "Lffo\u001Fhpjmh\"", "Mpof+\u001Fmp\u001Ftfdqfst\u001Fgfqf\"",
         "Dpnf\u001Fpm+\u001Fkppl\u001Fgbqcfq\""],
        ["Pg\u001Fmp+\u001Fmps\u001Fgfqf\"", "Sgjt\u001Fjt\u001Fb\u001Ftfdqfs-\u001FMps\"",
         "Cbqjfk\u001Fqpdlt---\u001FIpjm\u001Fvt\"", "Sgjt\u001Fjt\u001Fb\u001Fsqjdl\""],
        ["J\u001Fbn\u001Fmps\u001Fb\u001Ftfdqfs\u001Fnfttbhf\"", "Gfkkp+\u001Favs\u001Fmp\"",
         "Xqpmh\u001Fpmf+\u001Ftpqqz\"", "Afssfq\u001Fkvdl\u001Fmfws\u001Fsjnf\""]
    ]

    return messages[x][y]


# Application
def solution(directions):
    x, y = navigate(directions)
    secret_message = get_secret_message(x, y)
    decrypted_message = decrypt_secret_message(secret_message)
    return decrypted_message


if __name__ == '__main__':
    message = solution("URRRUULD")
    print(message)
"""

# print(navigate('URDLR'))
print(decrypt_secret_message('ABC'))
print(decrypt_secret_message('BAHHHDHJSJKDH'))
