def is_palindrome(word):
    letters_list = list(word)
    reverse_letters_list = list(reversed(letters_list))
    return letters_list == reverse_letters_list


print(is_palindrome('word'))
print(is_palindrome('lil'))
