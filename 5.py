doxod = float(input("Введите размер выручки:"))
rasxod = float(input("Введите размер издержек:"))
profit = 0
if doxod > rasxod:
    profit = doxod - rasxod
    profitability = (profit / doxod) * 100
    print(f"Прибыль составляет: {profit} у.е. Рентабельность равна: {profitability}%")
else:
    lesion = rasxod - doxod
    print(f"Убыток составляет: {lesion} у.е.")
employees = int(input("Введите число сотрудников:"))
if profit > 0:
    employee_profit = profit / employees
    print(f"Прибыль в расчете на одного сотрудника составляет: {employee_profit} у.е.")
else:
    print("Предприятие работает в убыток.")

