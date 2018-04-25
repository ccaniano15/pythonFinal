import objects
import functions

functions.characterSetUp("Bobby")

functions.purchase(objects.carrotSeed)
functions.purchase(objects.carrotSeed)
functions.purchase(objects.furtilizer)

print(functions.player.bank)
print()

functions.checkInv()

print(functions.field.field)
print(functions.field.furtTracker)
print()

functions.field.plant(objects.carrotSeed)
functions.field.plant(objects.carrotSeed)

print(functions.field.field)
print(functions.field.furtTracker)
print()

functions.field.furtilize(0)

print(functions.field.field)
print(functions.field.furtTracker)
print()

functions.checkPlantGrowth()

print(functions.player.inv)

functions.field.pick(objects.carrotSeed, 0)

print(functions.field.field)
print(functions.field.furtTracker)
print()

print(functions.player.inv)
functions.checkInv()

print(functions.player.bank)

functions.sell(objects.carrotGrown)

print(functions.player.bank)


