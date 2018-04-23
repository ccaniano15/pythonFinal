import functions

# player object, contains inventory and bank
class player:
	def __init__ (self, name, bank):
		self.name = name
		self.bank = bank
	def createInventory (self):
		self.inv = []
	def addInventory (self, obj):
		self.inv.append(obj)
	def subInventory (self, obj):
		self.inv.remove(obj)

# general iteam object
class items:
	def __init__ (self, name, cost):
		self.name = name
		self.cost = cost

# specifically plant team, inherits from iteam
class plant(items):
	def __init__ (self, name, cost, worth, furtilizerNeeded, health):
		items.__init__(self, name, cost)
		self.worth = worth
		self.growth = furtilizerNeeded
		self.health = health

# field. has plots.
class field:
	def __init__ (self, plots):
		self.plots = plots
	def createField(self):
		self.field = []  #make this a dictionary ?? those two lists need to line up
		self.furtTracker = []
		for plots in range(self.plots):
			self.field.append("empty")
			self.furtTracker.append("null")
	def addPlot(self):
		self.field.append("empty")
		self.furtTracker.append('null')
	def plant(self, obj):
		if obj in functions.player.inv:
			if "empty" in self.field:
				x = self.field.index("empty")
				print(x)
				self.field.remove("empty")
				self.field.insert(x, obj.name)
				self.furtTracker.remove("null")
				self.furtTracker.insert(x, obj.growth)
				functions.player.inv.remove(obj)
			else:
				print("no empty plots")
		else:
			print("no object in inv")
	def furtilize(self, plot):
		if furtilizer in functions.player.inv:
			if self.furtTracker[plot] == 0:
				print("already grown")
			elif self.furtTracker[plot] == 'null':
				print("nothing planted")
			else:
				x = self.furtTracker[plot]
				self.furtTracker.pop(plot)
				self.furtTracker.insert(plot, x - 1)
				functions.player.inv.remove(furtilizer)


furtilizer = items("furtilizer", 5)
carrot = plant("carrot", 1, 7, 1, 50)
greenBean = plant("green bean", 3, 20, 2, 20)

# store = [furtilizer, carrot, greenBean]


