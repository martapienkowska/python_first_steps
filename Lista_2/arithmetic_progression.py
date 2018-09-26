def arithmetic_progression(a1, r, n):
    an = a1 + (n -1) * r
    Sn = ((a1 + an)*n) / 2
    print("an =", an, "Sn =", Sn)


if __name__ == "__main__":
    arithmetic_progression(0, 100, 10)
