salary = 5000
spend = 6000
months = 10
increase = 0.03
money_capital = 0

for month in range(months):
    money_capital += max(spend - salary, 0)
    spend *= (1 + increase)

money_capital = int(money_capital)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)