class Item:
	objects = {}
	def __init__(self, name, description, value, weight):
		self.name = name
		self.description = description
		self.value = value
		self.weight = weight
		Item.objects[self.name] = self	

	def get_info(self):
		print("{}\n=====\n{}\nValue: {}\nWeight: {}\n".format(self.name, self.description, self.value, self.weight))

class Weapon(Item):
	def __init__(self, name, description, value, weight, atk):
		self.name = name
		self.description = description
		self.value = value
		self.weight = weight
		Item.objects[self.name] = self
		self.atk = atk

class Armour(Item):
	def __init__(self, name, description, value, weight, arm):
		self.name = name
		self.description = description
		self.value = value
		self.weight = weight
		Item.objects[self.name] = self
		self.arm = arm

class Potion(Item):
	def __init__(self, name, description, value, weight, potency):
		self.name = name
		self.description = description
		self.value = value
		self.weight = weight
		Item.objects[self.name] = self
		self.potency = potency
