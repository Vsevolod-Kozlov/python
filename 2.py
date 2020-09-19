user_seconds = int(input("Введите количество секунд"))
seconds = user_seconds % 60
hours = user_seconds // 3600
minutes = (user_seconds - hours * 3600) // 60
print(f"Время в формате чч:мм:сс {hours}:{minutes}:{seconds}")