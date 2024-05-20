import time


def get_the_fastest_func(args, arg):
    d = {}
    l1 = 10000000
    for i in args:
        start_time = time.perf_counter()
        i(arg)
        end_time = time.perf_counter()
        l = end_time-start_time
        d[i] = d.get(i, l)
        l1 = min(l, l1)
    for l in d.keys():
        if d[l] == l1:
            return l


def slow():
    time.sleep(3)


def fast():
    time.sleep(1)


funcs = [slow, fast]
print(get_the_fastest_func(funcs, 0))
