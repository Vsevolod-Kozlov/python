year_list = ["Зима", "Зима", "Весна","Весна", "Весна", "Лето", "Лето", "Лето", "Осень", "Осень", "Осень", "Зима"]
user_month = int(input("Введите номер месяца: ")) - 1
if user_month <= 0 or user_month > 11:
    print("Неверный формат месяца")
else:
    print(year_list[user_month])