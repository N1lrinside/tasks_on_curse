s = 2022*'1'

while '11111' in s or '555' in s:
    if '11111' in s:
        s = s.replace('11111', '555')
    else:
        s = s.replace('555', '5')
print(s)