profit = int(input("Введите сумму выручки вашей компании: "))
costs = int(input("Введите сумму издержек вашей компании: "))
rent = profit - costs
rent_2 = float(profit / costs)
print(f"Ваша рентабельность составляет {rent_2}")
if profit == costs:
    print("Ваша фирма выходит в ноль")
if profit > costs:
    workers_count = int(input("Назовите число сотрудников вашей компании: "))
    print(f"На одного сотрудника вашей компании приходится {rent / workers_count} прибыли")
if profit < costs:
    print(f'Ваша фирма имеет отрицательный финансовый результат (издержки больше выручки)')
