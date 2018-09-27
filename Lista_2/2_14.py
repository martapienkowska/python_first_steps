n = int(input("Insert number: "))
dict_1 = {}


for i in range(1, n + 1):
    dict_1[i] = []
    for i2 in range(1, (i + 1)):
        if i % i2 == 0:
            dict_1[i].append(i2)

print(dict_1)

