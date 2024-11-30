def numberOne(array_input, target_input):
    array_output = []
    is_done = False

    for i in range(0, len(array_input)):
        for j in range(i+1, len(array_input)):
            if array_input[i] + array_input[j] == target_input:
                array_output.append(i)
                array_output.append(j)
                is_done = True
                break
        if is_done:
            break

    if is_done:
        print(array_output)
    else:
        print("Penjumlahan target tidak ditemukan")


print('--- Contoh 1: ')
numberOne([2, 7, 11, 15], 9)
print('--- Contoh 2: ')
numberOne([3, 2, 4], 6)
print('--- Contoh 3: ')
numberOne([3, 3], 6)
print('--- Contoh 4: ')
numberOne([3, 3], 9)
