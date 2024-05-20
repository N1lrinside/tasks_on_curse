from datetime import datetime, timedelta
start, end = datetime.strptime(input(), '%d.%m.%Y'), datetime.strptime(input(), '%d.%m.%Y')
while start <= end:
    if (start.day + start.month) % 2 != 0 and start.weekday() != 0 or start.weekday() != 3:
        print(start.strftime('%d.%m.%Y'))
    elif start.weekday() == 0 or start.weekday() == 3:
        start += timedelta(days=3)
    start += timedelta(days=1)
