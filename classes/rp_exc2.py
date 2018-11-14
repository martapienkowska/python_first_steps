# Parent class
class Pets:

    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs
        
        
# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True
    
    def eat(self):
        self.is_hungry = False

    # Instance method
    def description(self):
        return self.name, self.age

    # Instance method
    def speak(self, sound):
        return "%s says %s" % (self.name, sound)

    # Instance method
    def eat(self):
        self.is_hungry = False


# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)


# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)
        



my_dogs = [Dog("Tom", 6), Dog("Fletcher", 7), Dog("Larry", 9)]

my_pets = Pets(my_dogs)

print("I have {} dogs".format(len(my_pets.dogs)))

for dog in my_dogs:
	print("{} is {}".format(dog.name, dog.age))
	
print("And they're all {}s, of course.".format(Dog.species))

not_feeded = Dog("every", "none").is_hungry
print(not_feeded)

feeded = not_feeded.eat()
feeded = feeded.is_hungry
print(feeded)



