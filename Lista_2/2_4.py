list_1 = [1, 'cos', 5, 'stol']
list_2 = ['cos', 1, 'stol', 7, 9]
list_3 = [15, 14, 'sdasda']
list_4 = [20, 21, 1]


def fun_1(x, y):
    d = 0
    for i in x:
        for i2 in y:
            if i == i2:
                d += 1
    if d != 0:
        print(True)
        return True


fun_1(list_1, list_2)
fun_1(list_2, list_3)
fun_1(list_1, list_4)

print("fun_2")


def fun_2(x, y):
    a = set(x)
    b = set(y)
    if len(a & b) != 0:
        print(True)
        return True


fun_2(list_1, list_2)
fun_2(list_2, list_3)
fun_2(list_1, list_4)


