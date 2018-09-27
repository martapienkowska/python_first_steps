list_1 = ['akkia', 'krzeslo', 'stol', 'dookjd', 'fkkjokf', 'sttkjes']


def fun_1():
    d = 0
    for i in list_1:
        if i[0] == i[-1]:
            d += 1
    print(d)

fun_1()

list_1.append('dood')

fun_1()

