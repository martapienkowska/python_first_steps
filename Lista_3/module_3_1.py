from random import randint


def fahr_cel(f):
    c = (5/9)*f - (160/9)
    return c


def cel_fahr(c):
    f = (9/5)*c + 32
    return f

def rand_celc():
    n = int(input("n ="))
    list1 = []
    for i in range(n):
        list1.append(str(randint(-273, 1000)))
    return "\n".join(list1)



