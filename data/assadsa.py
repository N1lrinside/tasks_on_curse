from datetime import date
# присваиваем самую раннюю дату урагана в переменную first_date
first_date = date(1992, 10, 2)

# конвертируем дату в ISO и RU формат
iso = 'Дата первого урагана в ISO формате: ' + first_date.strftime('%x')
ru = 'Дата первого урагана в RU формате: ' + first_date.strftime('%x')
us = 'Дата первого урагана в US формате: ' + first_date.strftime('%x')

print(iso)
print(ru)
print(us)
