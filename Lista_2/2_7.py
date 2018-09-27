dict_1 = {"a": 1, 2: 3, 8: 'd'}
dict_2 = {'krzes': 7, 15: 14}
dict_3 = {7: 3, 33: 44}
dict_4 = {"a": 222, 78: 87}
dict_5 = {"a": 1, 2: 7, 22: 23}


def fun_1(x, y):
    d = {**x, **y}
    for i1 in x:
        for i2 in y:
            if i1 == i2:
                print("Same keys in two dictionaries: ", i1)
    print(d)


fun_1(dict_1, dict_2)
fun_1(dict_1, dict_3)
fun_1(dict_1, dict_4)
fun_1(dict_1, dict_5)
