import math


def numberTwo(int_input):
    if not isinstance(int_input, int):
        return 'Input harus integer'
    if int_input < 0:
        return False

    is_palindrome = True
    string_input = str(int_input)
    string_length = len(string_input)
    max_iter = math.floor(string_length / 2)

    for i in range(max_iter):
        if string_input[i] != string_input[string_length - 1 - i]:
            is_palindrome = False
            break
    return is_palindrome


print('--- Contoh 1: ')
print(numberTwo(121))
print('--- Contoh 2: ')
print(numberTwo(-121))
print('--- Contoh 3: ')
print(numberTwo(10))
print('--- Contoh 4: ')
print(numberTwo(1234521))
print('--- Contoh 5: ')
print(numberTwo('1234a'))
