def fact(a):
    if a == 0:
        return 1
    if type(a) == int and a == abs(a):
        num = 1
        for i in range(1, a+1, 1):
            num *= i
        return num
    else:
        return "your number must be a non-negative integer"