def nod(a, b):
    if a == 0 or b == 0:
        return 1

    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    return a + b

