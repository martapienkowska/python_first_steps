class MyList:
    def __init__(self, start=[]):
        self.data = start[:]

    def __add__(self, other):
        return MyList(self.data + other.data)

    def __getitem__(self, item):
        return self.data[item]

    def append_met(self, obj):
        return self.data.append(obj)

    def sort_met(self, rev=False):
        return self.data.sort(reverse=rev)


inst1 = MyList([22, 8, 13])
inst2 = MyList([1, 2, 3])
print(inst1 + inst2)
print(inst1[1])
inst1.append_met(11)
print(inst1.data)
inst1.sort_met(True)
print(inst1.data)
inst3 = MyList([1, 2, 5, 66, 11, 22, 1])

print(inst3[1::2])