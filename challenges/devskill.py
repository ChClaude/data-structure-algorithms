from datetime import datetime
import re


def friday13(year):
    """
    For a given year, calculate the number of Friday 13th's will be in the year.
    """

    count = 0
    for month in range(1, 13):
        date = datetime(year, month, 13)

        if date.strftime("%A") == "Friday": count += 1
    return count


def react(polymer_string):
    """
    There is a processing plant that needs to be optimized, and we need your help.

    The processing plant creates chemical polymers made of 26 monomers, and 26 reactive monomers. When a monomer, and it's corresponding reactive monomer touch, they will react, and disappear from the chain.

    Each monomer has a symbol corresponding to a lower case letter in the alphabet ie: `a-z`.
    Each monomer's reactive cousin is given an upper case letter, ie: `A-Z`.

    In a chain, when a reactive pair, ie `Aa` or `aA` touch, they will disappear and the chain will re-attach.

    This means that in a polymer chain like `AaefxxXXB`, it will react to form: `efB`. It forms this by the following process:
    1. `Aa` will react, creating `efaaAAB`
    2. `xX` will react, creating `efxXB`
    3. `xX` will react, creating `efB`
    4. `efB` is now stable and will no longer react.

    Your task is to code an algorithm that prints out the stable and fully reacted polymer given any polymer chain input.

    To help you, here are some examples:

    1. `vRaKkNgeUYTt` will become `vRaNgeUY`
    2. `WySrKeqEzAYyYUQqYuIicrRClZGrjfdEvSxYcCQxcCTqpUu` will become `WySrKeqEzAYUYulZGrjfdEvSxYQxTqp`
    3. `mJYBPpluUqQrleJjgGUWwTtsywWdDuMmNOSsLlfXxOtTCcFfgXxZGgthHb` will become `mJYBlrleUsyuNOfOgZtb`

    Must return the string of reacted polymer.
    """

    # result = re.findall('[a-zA-Z][a-zA-Z]', polymer_string)

    # for x,y in re.findall(r'((a-zA-Z))(?!\2)(?i:\2)', polymer_string):

    while bool(re.search(r'([a-zA-Z])(?!\1)(?i:\1)', polymer_string)):
        for x in re.finditer(r'([a-zA-Z])(?!\1)(?i:\1)', polymer_string):
            polymer_string = polymer_string.replace(x.group(), '')
            # print(x.group())
    return polymer_string


# print(friday13(2015))
# print(react('vRaKkNgeUYTt'))  # vRaNgeUY
# print(react('WySrKeqEzAYyYUQqYuIicrRClZGrjfdEvSxYcCQxcCTqpUu'))  # WySrKeqEzAYUYulZGrjfdEvSxYQxTqp
# print(react('mJYBPpluUqQrleJjgGUWwTtsywWdDuMmNOSsLlfXxOtTCcFfgXxZGgthHb'))  # mJYBlrleUsyuNOfOgZtb

# myinput = 'AaefxxXXB'
#
# while re.match(r'([a-zA-Z])(?!\1)(?i:\1)', myinput):
#     for x in re.finditer(r'([a-zA-Z])(?!\1)(?i:\1)', myinput):
#         myinput = myinput.replace(x.group(), '')
#         print(x.group())

# print([x.group() for x in re.finditer(r'([a-zA-Z])(?!\1)(?i:\1)', 'AaefxxXXB')])
# print([x.group() for x in re.finditer(r'([a-zA-Z])(?!\1)(?i:\1)', 'aADFfGcCgs')])
# print([x for x, y in re.findall(r'(([a-zA-Z])(?!\2)(?i:\2))', 'aADFfGcCgs')])
