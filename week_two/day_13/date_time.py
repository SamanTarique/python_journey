from datetime import date, datetime, time

todays_date = date.today()
print(todays_date)
print(todays_date.day)
print(todays_date.month)
print(todays_date.year)

print(type((date(2010, 10, 10)).isoformat()))

print(time(10, 10, 10))
print(time(10, 14, 18).minute)

print(datetime(10, 10, 10).month)
