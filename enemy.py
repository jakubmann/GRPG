class Enemy:
	objects = {}
	def __init__(self, name, hp, atk, arm, loot):
		self.name = name
		self.hp = hp
		self.atk = atk
		self.arm = arm
		self.loot = loot
		Enemy.objects[self.name] = self	
	def get_info(self):
		print("{}\n=====\n{}\nHeatlh: {}\nStrength: {}\nArmour: {}\n".format(self.name, self.description, self.hp, self.atk, self.arm))