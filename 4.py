user_number = int(input("Введите целое положительное число"))
big = 0
while user_number > 0:
    temp = user_number % 10
    if temp > big:
        big = int(temp)
    user_number = (user_number - temp) / 10
print("Наибольшая цифра в числе:", big)


