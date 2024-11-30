def numberThree(roman_input):
    roman = roman_input.upper()
    roman_int_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    int_output = 0
    prev_int = 0

    for roman_char in reversed(roman):
        try:
            current_int = roman_int_map[roman_char]
        except KeyError:
            return 'Input roman tidak valid'

        if current_int < prev_int:
            int_output -= current_int
        else:
            int_output += current_int

        prev_int = current_int

    return int_output


print('--- Contoh 1: ')
print(numberThree('III'))
print('--- Contoh 2: ')
print(numberThree('LVIII'))
print('--- Contoh 3: ')
print(numberThree('MCMXCIV'))
print('--- Contoh 4: ')
print(numberThree('ACMXCIV'))
