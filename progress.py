from datetime import datetime

start_day = 13
start_month = 11

day = datetime.today().day
month = datetime.today().month

start = start_month * 30 + start_day
end = month * 30 + day

print("Прошло дней: ", end - start)
print("Осталось дней: ", 365 - (end - start))
print()
print("Прогрес", (end - start) / 365 * 100,"%")
