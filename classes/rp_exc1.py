class Dog:

    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
a = Dog("a", 5)
b = Dog("b", 7)
c = Dog("c", 4)

def get_biggest_number(*args):
	a = max(args)
	print("The oldest dog is {} years old.".format(a))
	
get_biggest_number(a.age, b.age, c.age)
