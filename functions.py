from collections import Counter
import objects
import pygame, sys

viewField = True
viewStore = False
buy = False
viewSell = False
plant = False

selection = 0

pygame.init()
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Farm Life: Live your best farm life!')
clock = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)
lightYellow = (255, 250, 234)
silver = (192,192,192)
brown = (139,69,19)
yellow = (255,255,102)
green = (0,128,0)

smallText = pygame.font.SysFont("comicsansms",20)

def generateStore():
    TextSurf, TextRect = text_objects("Bank: " + str(player.bank) + "$", smallText)
    gameDisplay.blit(TextSurf, (730,10))
    TextSurf, TextRect = text_objects("Inventory: " + str(len(player.inv)) + "/20", smallText)
    gameDisplay.blit(TextSurf, (700,25))
    if selection != None:
        TextSurf, TextRect = text_objects("Item: " + selection.name, smallText)
        gameDisplay.blit(TextSurf, (10,10))
        TextSurf, TextRect = text_objects("Price: " + str(selection.cost) +"$", smallText)
        gameDisplay.blit(TextSurf, (10,25))
        
    for item in range(0,len(objects.store)):
        x = objects.store[item]
        if item == 0 or item == 1:
            button(x.name,213.33 + 293.33 * item,100,80,80,silver,silver,selectStore,item)
        else:
            m = item - 2
            button(x.name,66.67 + 146.67 * m,220,80,80,silver,silver,selectStore,item)
          
def generateField():
    for x in range(0,len(field.field)):
        print(x)
        if field.field[x] == "Empty":
            button("Empty", 30 + 80 * x, 150, 50, 50, brown, brown, selectPlot, x, None)
        elif field.field[x] != "Empty" and field.furtTracker[x] != 0:
            button(field.field[x],30 + 80 * x,150,50,50,yellow,yellow,selectPlot,x, None)
        elif field.field[x] != "Empty" and field.furtTracker[x] == 0:
            button(field.field[x],30 + 80 * x,150,50,50,green,green,selectPlot,x, None)
    if selection == None:
        TextSurf, TextRect = text_objects("Selected: None", smallText)
        gameDisplay.blit(TextSurf, (10,10))
    elif selection == "Empty":
        TextSurf, TextRect = text_objects("Selected: Empty Plot", smallText)
        gameDisplay.blit(TextSurf, (10,10))
    else:
        TextSurf, TextRect = text_objects("Selected: " + field.field[selection], smallText)
        gameDisplay.blit(TextSurf, (10,10))            

def showInv():
    for thing in range(0, len(player.inv)):
        x = 30 + 110 * thing
        if x <= display_width:
            y = 100
        elif x > display_width:
            maxItems = display_width/140
            newRowIteam = thing - maxItems - 2
            x = 30 + 110 * newRowIteam
            y = 200 
            if x > display_width:
                maxItems = display_width/140
                newRowIteam = thing - maxItems * 2
                newRowIteam = newRowIteam - 3
                x = 30 + 110 * newRowIteam
                y = 300
        button(player.inv[thing].name,x,y,80,80,silver,silver,selectInv,thing)
    if selection != None or selection != int:
        TextSurf, TextRect = text_objects("Selected: " + selection.name, smallText)
        gameDisplay.blit(TextSurf, (10,10)) 
        if viewSell == True:
            TextSurf, TextRect = text_objects("Worth: " + str(selection.worth) + "$", smallText)
            gameDisplay.blit(TextSurf, (10,25))         
    else:
        TextSurf, TextRect = text_objects("Selected: None", smallText)
        gameDisplay.blit(TextSurf, (10,10)) 

    if viewSell == True:
        TextSurf, TextRect = text_objects("Bank: " + str(player.bank) + "$", smallText)
        gameDisplay.blit(TextSurf, (730,10))
        TextSurf, TextRect = text_objects("Inventory: " + str(len(player.inv)) + "/20", smallText)
        gameDisplay.blit(TextSurf, (700,25))      

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def rect(x, y, w, h, color):
    pygame.draw.rect(gameDisplay, color, [x, y, w, h])

def twoButtons(text1,text2,action1, action2,x2,s):
    button(text1,166.67,450,150,100,silver,white,action1)
    button(text2,483.37,450,150,100,silver,white,action2,x2,s)

def threeButtons(text1,text2,text3, action1, action2, action3, x1, s):
    
    button(text1,87.5,450,150,100,silver,white,action1,x1,s)
    button(text2,325,450,150,100,silver,white,action2,)
    button(text3,562.5,450,150,100,silver,white,action3)

def button(msg,x,y,w,h,ic,ac,action=None,inp=None,s=None):
    needsSelection = ["field.furtilize", "field.pick","purchase", "sell", "objects.field.plant"]
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None and inp == None:
            if str(action) in needsSelection:
                if selection == None:
                    None
                else:
                    action()
            else:
                action()
                
            if s == True:
                resetSelection()
                
        elif click[0] == 1 and action != None and inp != None:
            if str(action) in needsSelection:
                if selection == None:
                    None
                else:
                    action(inp)
            else:
                action(inp)
            if s == True:
                resetSelection()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def resetSelection():
    global selection
    selection = None

def switchStoreField():
    global viewField
    global viewStore
    global selection

    if viewField == True:
        viewField = False
        viewStore = True
        return
    else:
        viewField = True
        viewStore = False
        selection = 1
        print("field")
        return

def switchStoreBuy():
    global viewStore
    global buy
    global selection

    if viewStore == True:
        selection = None
        viewStore = False
        buy = True
        print("buy")
        return
    else:
        viewStore = True
        buy = False
        print("store")
        return

def switchStoreSell():
    global viewStore
    global viewSell

    if viewStore == True:
        viewStore = False
        viewSell = True
        print("sell")
        return
    else:
        viewStore = True
        viewSell = False
        print("store")
        return

def switchFieldPlant():
    global viewField
    global plant

    if viewField == True:
        viewField = False
        plant = True
        return
    else:
        selection = 0
        viewField = True
        plant = False
        return

def selectStore(item):
    global selection
    selection = objects.store[item]

def selectPlot(plot):
    global selection
    selection = plot

def selectInv(item):
    global selection
    selection = player.inv[item]

def plantPick():
    global selection
    if selection == None:
        None
    if field.field[selection] == "Empty":
        selection = None
        switchFieldPlant()
    elif field.field[selection] != "Empty" and field.furtTracker[selection] == 0:
        field.pick(selection)

# initiats player object, creates inventory, creates field
def characterSetUp(x):
    global field
    global player
    player = objects.player(x,20)
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

# buy and sell items
def purchase(x): #'module' object has no attribute obj
    if player.bank !=0:
        if x.name == "plot":
            field.addPlot()
            player.bank = player.bank - x.cost
        elif len(player.inv) == 20:
            print("inv full")
        else:
            player.addInventory(x)
            player.bank = player.bank - x.cost

def sell(x):
    global selection
    player.bank = player.bank + x.worth
    player.subInventory(x)
    selection = None

