def polynomial(n, x, *a):
    p = 0
    for i in range(n):
        p += a[i] * (x ** i)
    print(p)


polynomial(3, 4, 2, 3, 5)
polynomial(4, 2, 1, 2, 3, 4)