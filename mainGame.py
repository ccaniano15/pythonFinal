import objects
import functions

functions.characterSetUp("Bobby")

functions.purchase(objects.carrot)
functions.purchase(objects.furtilizer)

print(functions.player.bank)
print()

functions.checkInv()

print(functions.field.field)
print(functions.field.furtTracker)
print()

functions.field.plant(objects.carrot)

print(functions.field.field)
print(functions.field.furtTracker)
print()

functions.field.furtilize(0)

print(functions.field.field)
print(functions.field.furtTracker)
print()

functions.checkPlantGrowth()
