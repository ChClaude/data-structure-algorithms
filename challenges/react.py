import re


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

    while bool(re.search(r'([a-zA-Z])(?!\1)(?i:\1)', polymer_string)):
        for x in re.finditer(r'([a-zA-Z])(?!\1)(?i:\1)', polymer_string):
            polymer_string = polymer_string.replace(x.group(), '')
    return polymer_string


print(react('vRaKkNgeUYTt'))  # vRaNgeUY
print(react('vRGnKkNgeyUuYTt'))  # vRe
print(react('WySrKeqEzAYyYUQqYuIicrRClZGrjfdEvSxYcCQxcCTqpUu'))  # WySrKeqEzAYUYulZGrjfdEvSxYQxTqp
print(react('mJYBPpluUqQrleJjgGUWwTtsywWdDuMmNOSsLlfXxOtTCcFfgXxZGgthHb'))  # mJYBlrleUsyuNOfOgZtb
