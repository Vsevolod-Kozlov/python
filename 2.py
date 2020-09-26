element_number = int(input("Введите количество элементов списка"))
temp_number = 1
user_list = []
result_list = []
temp_value = 0
while temp_number <= element_number:
    new_el = input("Введите элемент списка")
    user_list.append(new_el)
    print(user_list)
    temp_number = temp_number + 1
user_list_1 = user_list[0::2]
user_list_2 = user_list[1::2]
for el in user_list_2:
    result_list.append(el)
    result_list.append(user_list_1[0 + temp_value])
    temp_value = temp_value + 1
if element_number % 2 != 0:
    result_list.append(user_list_1[-1])
print(result_list)


