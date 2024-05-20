from datetime import datetime


def num_of_sundays(integer):
    h = datetime(integer, 1, 1).toordinal()
    return h


print(num_of_sundays(int(input())))