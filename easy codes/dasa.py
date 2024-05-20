str_vov = 'а, у, о, ы, и, э, я, ю, ё, е'.replace(', ', '')
h = [i for i, c in enumerate(input()) if c in str_vov]
for i in range(int(input())):
    input_str = input()
    if [i for i, c in enumerate(input_str) if c in str_vov] == h:
        print(input_str)
