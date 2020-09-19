initial = float(input("Введите результат бега за первый день в км:"))
final = float(input("Введите требуемую дистанцию бега в км:"))
count = 1
while initial <= final:
    print(f"{count}-й день: {initial}")
    initial = initial * 1.1
    count = count + 1
print(f"{count}-й день: {initial}")
print(f"Ответ: на {count}-й день спортсмен достиг результата - не менеее {final} км.")