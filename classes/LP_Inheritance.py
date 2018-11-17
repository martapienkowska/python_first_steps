class Adder:
    def add(self, x, y):
        print("Not implemented")


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

inst1 = DictAdder()
print(inst1.add(dict1, dict2))


