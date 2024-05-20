n = int(input("Введите число от 1900 до 3000"))
if n < 1900 or n > 3000:
    print('Неверный ввод')
else:
    if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
        print('Високосный')
    else:
        print('Обычный')
    
