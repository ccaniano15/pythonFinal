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
			self.field.append("empty")
			self.furtTracker.append("null")
			self.healthTracker.append('null')
	def addPlot(self):
		self.field.append("empty")
		self.furtTracker.append('null')
		self.healthTracker.append('null')
	def plant(self, obj):
		if obj in functions.player.inv:
			if "empty" in self.field:
				x = self.field.index("empty")
				print(x)
				self.field.remove("empty")
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
	def pick(self, seed, plot):
		allPlants = [carrotGrown, greenBeanGrown]
		if self.furtTracker[plot] == 0:
			self.furtTracker[plot] = "null"
			self.healthTracker[plot] = "null"
			self.field[plot] = "empty"
			for x in allPlants:
				if x.seedName == seed.name:
					functions.player.inv.append(x)
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

furtilizer = items("furtilizer", 5)
plot = items("plot", 20)
carrotSeed = seed("carrot seed", 1, 1, 50)
greenBeanSeed = seed("green bean seed", 3, 2, 20)
onionSeed = seed("onion seed", 3, 2, 50)
appleSeed = seed("apple seed", 2, 5, 120)
tomatoSeed = seed("tomato seed", 1, 1, 20)

carrotGrown = plant("carrot", 'null', 7, "carrot seed")
greenBeanGrown = plant("green bean", 'null', 25, "green bean seed")
onionGrown = plant("onion", 'null', 20, "onion seed" )
appleGrown = plant("apple tree", 'null', 40, "apple seed")
tomatoGrown = plant("tomato", 'null', 10, "tomato seed")


store = [furtilizer, plot, carrotSeed,greenBeanSeed,onionSeed,appleSeed,tomatoSeed]


