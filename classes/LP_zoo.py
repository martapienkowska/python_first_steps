class Animal:
	def reply(self):
		self.speak()
	
	def speak(self):
		print("Spam")
	
	
class Mammal(Animal):
	pass


class Dog(Mammal):
	def speak(self):
		print("Hau Hau")


class Cat(Mammal):
	def speak(self):
		print("Mial")

	
class Primate(Mammal):
	def speak(self):
		print("Hello world")

class Hacker(Primate):
	pass


if __name__ == '__main__':
	inst1 = Cat()
	inst1.reply()
	inst2 = Dog()
	inst2.reply()
	inst3 = Hacker()
	inst3.reply()
	inst4 = Animal()
	inst4.reply()


