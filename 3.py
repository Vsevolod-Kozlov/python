user_number = input("Введите целое положительное число")
first_term = int(user_number)
second_term = int(f"{user_number}{user_number}")
third_term = int(f"{user_number}{user_number}{user_number}")
result = first_term + second_term + third_term
print("Число = n. Сумма n + nn + nnn =", result)