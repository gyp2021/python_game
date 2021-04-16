import datetime

today = datetime.date.today()

birth0 = datetime.date(1981, 3, 30)
birth1 = datetime.date(2020, 4, 16)
birth2 = datetime.date(2021, 4, 15)
birth3 = datetime.date(2021, 4, 16)

print(today - birth0)
print(today - birth1)
print(today - birth2)
print(today - birth3)
