a = [1, 2, 3, 4, 5]


def fun(x):
    i = 0
    b = [[]]
    while i < len(a):
        j = i + 1
        while j <= len(a):
            b.append(a[i:j])
            j += 1
        i += 1
    print(b)


fun(a)
