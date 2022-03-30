
test_list = ['Virgin', 'Islands', 123455]

for elements in test_list:
        lenght = len(test_list) - 1
        test_list[0:lenght] = [' '.join(test_list[0:lenght])]

print(test_list)