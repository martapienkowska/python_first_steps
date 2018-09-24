def polynomial(x, *a):
    p = 0
    for i in range(len(a)):
        p += a[i] * (x ** i)
    print(p)


polynomial(4, 2, 3, 5)
polynomial(2, 1, 2, 3, 4)
polynomial(2, 1, 0, 4)

