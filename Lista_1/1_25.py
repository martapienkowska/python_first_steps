a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))


def fun_delta():
    delta = (b**2) - (4 * a * c)
    return delta


if fun_delta() > 0:
    X1 = (- b - (fun_delta() ** (1/2))) / (2 * a)
    X2 = (- b + (fun_delta() ** (1/2))) / (2 * a)
    print("X1 =", X1)
    print("X2 =", X2)
elif fun_delta() == 0:
    X1 = - b / (2 * a)
    print("X1 =", X1)
else:
    print("delta<0, no solutions")

    

