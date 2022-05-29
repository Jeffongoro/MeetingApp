def reverse_integer(number):
    reversed_string = ''
    index = len(str(number)) - 1
    while index >= 0:
        reversed_string += str(number)[index]
        index = index - 1
    if reversed_string.endswith('-'):
        reversed_string = '-' + reversed_string.rstrip('-')
    return reversed_string


if __name__ == '__main__':
    print(reverse_integer(-678))
