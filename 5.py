example_list = [8, 6, 2]
print(example_list)
user_element = int(input("Введите целое число от 0 до 9. Для завершения программы введите целое число от 10 и более или 0 и менее:"))
while user_element < 10 and user_element > 0:
    for el in range(len(example_list)):
        if example_list[el] == user_element:
            example_list.insert(el + 1, user_element)
            break
        elif example_list[0] < user_element:
            example_list.insert(0, user_element)
        elif example_list[-1] > user_element:
            example_list.append(user_element)
            break
        elif example_list[el] > user_element and example_list[el + 1] < user_element:
            example_list.insert(el + 1, user_element)
            break
    print(f"Текущий результат {example_list}")
    user_element = int(input("Введите целое число от 0 до 9. Для завершения программы введите целое число от 10 и более или 0 и менее:"))
