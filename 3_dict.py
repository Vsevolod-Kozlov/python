seasons_dict = {"winter" : "Зима", "spring" : "Весна", "summer" : "Лето", "autumn" : "Осень"}
user_month = int(input("Введите номер месяца: "))
if user_month <= 0 or user_month > 12:
    print("Неверный формат месяца")
elif user_month == 1 or user_month == 2 or user_month == 12:
    print(seasons_dict.get("winter"))
elif user_month == 3 or user_month == 4 or user_month == 5:
    print(seasons_dict.get("spring"))
elif user_month == 6 or user_month == 7 or user_month == 8:
    print(seasons_dict.get("summer"))
elif user_month == 9 or user_month == 10 or user_month == 11:
    print(seasons_dict.get("autumn"))

