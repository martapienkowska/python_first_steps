class Adder:
    def __init__(self, x=None):
        self.x = x

    def add(self, x, y):
        print("Not implemented")

    def __add__(self, other):
        return self.add(self.x, other)


class ListAdder(Adder):
    def add(self, x, y):
        a = x + y
        return a


class DictAdder(Adder):
    def add(self, x, y):
        c = {}
        for i, j in x.items():
            c[i] = j
        for i, j in y.items():
            c[i] = j
        return c


dict1 = {7: 'a', 8: 'b'}
dict2 = {1: '7', 2: 'p'}
list1 = [6, 7, 'a']
list2 = [15, 'c', 12]

inst1 = DictAdder(dict1)
inst2 = ListAdder(list1)
list3 = inst2 + list2
dict3 = inst1 + dict2
print(list3)
print(dict3)

x = ListAdder()
print(x.add(list1, list2))
y = DictAdder()
print(y.add(dict1, dict2))