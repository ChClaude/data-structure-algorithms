
def challenge_one(secretMessage):
    # @author: Elvis Gene
    letters = [letter for letter in secretMessage]
    msg_len = len(secretMessage)

    for i in range(msg_len):
        # Get numeric value of the letter
        num = ord(letters[i])
        if num % 2 == 0:
            num = num - 1
        else:
            num = num + 1

        # Get the letter of the new value
        new_letter = chr(num)

        # Appending or replacing the new character
        letters[i] = new_letter

    secretMessage = ''.join(letters)

    print(secretMessage)
# Append or replace?
# Only capital letters?

challenge_one('ABC')
challenge_one('BAHHHDHJSJKDH')

