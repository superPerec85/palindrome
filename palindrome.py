def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


# something = input('Введите текст: ')
something = r"А роза() упала н!а л=а\\пу \Азора"
punctuation = r'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'  # r'' для обратного слеша

for sign in punctuation:
    if sign in something:
        replace_string = something.replace(sign, '')
        something = replace_string
        continue

space_string = something.replace(' ', '')
lower_string = space_string.lower()

if (is_palindrome(lower_string)):
    print("Да, это палиндром")
else:
    print("Нет, это не палиндром")
