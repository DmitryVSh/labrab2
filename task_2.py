money_capital = 20000
salary = 5000
spend = 6000
increase = 0.05

months = 0

while money_capital >= max(spend - salary, 0):
    money_capital -= max(spend - salary, 0)
    spend *= (1 + increase)
    months += 1

print(f"Количество месяцев, которое можно протянуть без долгов: {months}")
