from collections import Counter
import objects

# initiats player object, creates inventory, creates field
def characterSetUp(x):
	global player
	global field
	player = objects.player(x, 20)
	player.createInventory()
	field = objects.field(3)
	field.createField()
	print("CHARA CREATED")

# checks and counts how many things you have in your inventory
def checkInv():

	listCheck = []
	itemSort = []

	for x in player.inv:
		listCheck.append(x.name)
	
	for x in listCheck:
		if x not in itemSort:
			itemSort.append(x)

	invCheck = Counter(listCheck)

	for x in itemSort:
		print(x + " x" +str(invCheck[x]))

def checkPlantGrowth():
	for x in field.furtTracker:
		if x == 0:
			y = field.furtTracker.index(x)
			print("your " + field.field[y] + " is ready to harvest!")

# buy and sell items
def purchase(x):
	player.bank = player.bank - x.cost #'module' object has no attribute obj
	if x.name == "plot":
		field.addPlot()
	else:
		player.addInventory(x)

def sell(x):
	player.bank = player.bank + x.worth
	player.subInventory(x)
