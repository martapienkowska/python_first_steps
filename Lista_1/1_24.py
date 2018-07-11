def fib_iter2():
    n = int(input("Insert number: "))
    a, b = 0, 1
    print(a)
    print(b)
    for i in range(n - 2):
        a, b = b, a + b
        print(b)


fib_iter2()
