from enum import Enum
from datetime import date
class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
class NextDate:
    def __init__(self,today,weekday,after_today=False):
        self.today=today
        self.weekday=weekday
        self.after_today=after_today

    def days_until(self):
        return Weekday[1]

today = date(2023, 4, 17)                              # понедельник
next_friday = NextDate(today, Weekday.FRIDAY)          # следующая пятница
print(next_friday.days_until())