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

class MyListSub(MyList):
	class_counter = 0
	def __init__(self, start=[]):
		self.counter = 0
		MyList.__init__(self, start)
		

	def __add__(self, other):
		self.counter += 1
		#licznik dla instancji, dzięki temu że jest self, to odnosi się do każdej instancji
		MyListSub.class_counter += 1
		#licznik dla klasy	
		print('Added {}'.format(other.data), 'couner = ' + str(self.counter), 
		'class_counter = ' + str(MyListSub.class_counter))
		return MyList.__add__(self, other)		
		

if __name__ == '__main__':	
	inst1 = MyListSub([22, 8, 13])
	inst2 = MyListSub([1, 2, 3])
	print(inst1 + inst2)
	inst3 = MyListSub([9])
	inst4 = inst1 + inst2
	print(inst4.data)
	print(inst1+inst3)
	print(inst2 + inst3)





