from math import cos, sin, atan2, acos, pi


def check_coord(b):
    if b == 1:
        while True:
            X = input("Insert X: ")
            Y = input("Insert Y: ")
            Z = input("Insert Z: ")
            try:
                X = float(X)
                Y = float(Y)
                Z = float(Z)
            except ValueError:
                print("Incorrect coordinates, insert float number")
            else:
                break
        return X, Y, Z
    elif b == 2:
        while True:
            fi = input("Insert fi: ")
            lamb = input("Insert lambda: ")
            r = input("Insert r: ")
            try:
                fi = float(fi)
                lamb = float(lamb)
                r = float(r)
            except ValueError:
                print("Incorrect coordinates, insert float number r>=0, fi (−π, +π] and lambda [0, +π])")
            else:
                if r < 0 or fi < (-pi) or fi >= pi or lamb < 0 or lamb > pi:
                    print("Incorrect coordinates, insert float number r>=0, fi (−π, +π] and lambda [0, +π])")
                else:
                    break
        return fi, lamb, r


def spher_cart(fi, lamb, r):
    x_1 = r * (sin(lamb)) * (cos(fi))
    y_1 = r * (sin(lamb)) * (sin(fi))
    z_1 = r * (cos(lamb))
    print("X=", x_1)
    print("Y=", y_1)
    print("Z=", z_1)


def cart_spher(x, y, z):
    fi_1 = atan2(y , x)
    r_1 = ((x**2) + (y**2) + (z**2)) ** (1/2)
    lamb_1 = acos(z / r_1)
    print("fi=", fi_1)
    print("lambda=", lamb_1)
    print("r=", r_1)


def choose_cord_sys():
    while True:
        a = input("Choose:\nCartesian-Spherical - 1\nSpherical-Cartesian - 2\n1/2: ")
        if "1" == a or "2" == a:
            break
        else:
            print("Choose 1 or 2")
    return int(a)


def execute(a):
    if a == 2:
        spher_cart(*(check_coord(2)))
    elif a == 1:
        cart_spher(*(check_coord(1)))


execute(choose_cord_sys())

