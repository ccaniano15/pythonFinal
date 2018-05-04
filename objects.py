import functions
import random

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
		self.worth = cost

# specifically seed team, inherits from iteam
class seed(items):
	def __init__ (self, name, cost, furtilizerNeeded, health):
		items.__init__(self, name, cost)
		self.growth = furtilizerNeeded
		self.health = health

class plant(items):
	def __init__ (self, name, cost, worth, seedName):
		items.__init__(self, name, cost)
		self.worth = worth
		self.seedName = seedName

# field. has plots. has methods that create the field, 
# add a plot to the field, plant a plat in a plot, furtilize the plant, pick the plant
class field:
	def __init__ (self, plots):
		self.plots = plots
	def createField(self):
		self.field = [] 
		self.furtTracker = []
		self.healthTracker = []
		for plots in range(self.plots):
			self.field.append("Empty")
			self.furtTracker.append("null")
			self.healthTracker.append('null')
	def addPlot(self):
		self.field.append("Empty")
		self.furtTracker.append('null')
		self.healthTracker.append('null')
	def plant(self, obj):
		global selection
		if obj in functions.player.inv:
			if "Empty" in self.field:
				x = self.field.index("Empty")
				print(x)
				self.field.remove("Empty")
				self.field.insert(x, obj.name)
				self.furtTracker.remove("null")
				self.furtTracker.insert(x, obj.growth)
				self.healthTracker.remove("null")
				self.healthTracker.insert(x, obj.health)
				functions.player.inv.remove(obj)
			else:
				print("no empty plots")
		else:
			print("no object in inv")

	def furtilize(self, plot):
		global selection
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

	def pick(self, plot):
		global selection
		allPlants = [carrotGrown, soybeanGrown, onionGrown, appleGrown, tomatoGrown]
		if self.furtTracker[plot] == 0:
			for x in allPlants:
				if x.seedName == self.field[plot]:
					functions.player.inv.append(x)
			self.furtTracker[plot] = "null"
			self.healthTracker[plot] = "null"
			self.field[plot] = "Empty"
		else:
			print("plant not grown")

#class the creates weather objects
class weather:
	def __init__ (self, name, verb, damage):
		self.name = name
		self.verb = verb
		self.damage = damage

	def randomWeather(self):
		allWeather = []
		chosenWeather = random.choice(allWeather)
		damage = chosenWeather.damage
		plant = random.choice(field.field)
		#chose a plant, subtract damage from the plants health



#dcreating objectsx

furtilizer = items("Fertilizer", 5)
plot = items("Plot", 20)
carrotSeed = seed("Carrot Seed", 1, 1, 50)
soybeanSeed = seed("Soybean Seed", 3, 2, 20)
onionSeed = seed("Onion Seed", 3, 2, 50)
appleSeed = seed("Apple Seed", 2, 5, 120)
tomatoSeed = seed("Tomato Seed", 1, 1, 20)

carrotGrown = plant("Carrot", 'null', 7, "Carrot Seed")
soybeanGrown = plant("Soybean", 'null', 25, "Soybean Seed")
onionGrown = plant("Onion", 'null', 20, "Onion Seed" )
appleGrown = plant("apple tree", 'null', 40, "apple seed")
tomatoGrown = plant("Tomato", 'null', 10, "Tomato Seed")


store = [furtilizer, plot, carrotSeed,soybeanSeed,onionSeed,appleSeed,tomatoSeed]


