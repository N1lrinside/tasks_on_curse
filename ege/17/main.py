with open('17.txt')as f:
    numbers = [int(x) for x in f]
    s = []
    for i in range(1, len(numbers)):
        if numbers[i] % 15 == 0 or numbers[i-1] % 15 == 0 and numbers[i] - numbers[i-1] % 60 == 0:
            s.append(numbers[i] - numbers[i-1])
    print(len(s), max(s))
