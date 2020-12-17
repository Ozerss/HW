profit = int(input("Введите сумму выручки вашей компании: "))
costs = int(input("Введите сумму издержек вашей компании: "))
rent = profit - costs
while profit > costs:
    workers_count = int(input("Назовите число сотрудников вашей компании: "))
    print(f"На одного сотрудника вашей компании приходится {rent / workers_count} прибыли")
    break
else:
    print(f'Ваша фирма имеет отрицательный финансовый результат (издержки больше выручки)')
