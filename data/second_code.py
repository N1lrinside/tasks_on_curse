from datetime import date

andrew = date(1992, 8, 24)

print(andrew.strftime('%Y-%m'))   # выводим дату в формате YYYY-MM
print(andrew.strftime('%B'))   # выводим дату в формате month_name (YYYY)
print(andrew.strftime('%Y-%A'))   # выводим дату в формате YYYY-day_number
