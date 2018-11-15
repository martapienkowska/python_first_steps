# Parent class
class Pets:

    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs
    def walk(self):
        for dog in self.dogs:
            print( "{} walks".format(dog.name))
        
# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    def walk(self):
        return "{} walks".format(self.name)

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

for dogs in my_dogs:
    dogs.eat()

are_my_dogs_hungry = False
for dog in my_pets.dogs:
    if dog.is_hungry:
        are_my_dogs_hungry = True


if are_my_dogs_hungry:
    print("My dogs are hungry.")
else:
    print("My dogs are not hungry.")

for dog in my_dogs:
    a = dog.walk()
    print(a)

my_pets.walk()


