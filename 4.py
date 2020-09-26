user_str = input("Введите строку: ")
user_str = user_str.split()
num_element = 1
for el in user_str:
    if len(el) <= 10:
        print(f"{num_element} {el}")
    else:
        print(f"{num_element} {el[0:10]}")
    num_element += 1
