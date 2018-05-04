from collections import Counter
import objects
import pygame, sys

# creates variables that set pages to true or false
viewField = True
viewStore = False
buy = False
viewSell = False
plant = False

#holds what item is selected
selection = 0

pygame.init()
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Farm Life: Live your best farm life!')
clock = pygame.time.Clock()

#sets colors
black = (0,0,0)
white = (255,255,255)
lightYellow = (255, 250, 234)
silver = (192,192,192)
brown = (139,69,19)
yellow = (255,255,102)
green = (0,128,0)

#sets font size
smallText = pygame.font.SysFont("comicsansms",20)

def generateStore():
#creates text that shows players bank and inentory information
#if an item is selected shows items information
#for each iteam in store list, create a new button that when clicked runs selectStore
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
#for each item in field list in field object creates a button that when clicked runs selectPlot
#if a field is selected display field info
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
#for each item in inventory, creates a new button
#if item is selected show item info
#if inv empty display text "inventory empty"
    if len(player.inv) > 0:
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
            if plant == True and player.inv[thing].name == "Fertilizer":
                    None
            else:
                button(player.inv[thing].name,x,y,80,80,silver,silver,selectInv,thing)
        if selection == None:
            TextSurf, TextRect = text_objects("Selected: None", smallText)
            gameDisplay.blit(TextSurf, (10,10)) 

        elif selection != None or selection != int:
            TextSurf, TextRect = text_objects("Selected: " + selection.name, smallText)
            gameDisplay.blit(TextSurf, (10,10)) 
            if viewSell == True:
                TextSurf, TextRect = text_objects("Worth: " + str(selection.worth) + "$", smallText)
                gameDisplay.blit(TextSurf, (10,25))         

        if viewSell == True:
            TextSurf, TextRect = text_objects("Bank: " + str(player.bank) + "$", smallText)
            gameDisplay.blit(TextSurf, (730,10))
            TextSurf, TextRect = text_objects("Inventory: " + str(len(player.inv)) + "/20", smallText)
            gameDisplay.blit(TextSurf, (700,25))      
    else: 
        TextSurf, TextRect = text_objects("Inventory Empty", smallText)
        gameDisplay.blit(TextSurf, ((350),((display_height - 400)/2)))

def text_objects(text, font, c = black):
    textSurface = font.render(text, True, c)
    return textSurface, textSurface.get_rect()

def rect(x, y, w, h, color):
    pygame.draw.rect(gameDisplay, color, [x, y, w, h])

def twoButtons(text1,text2,action1, action2,x2,s):
    #generates two buttons
    button(text1,166.67,450,150,100,silver,white,action1)
    button(text2,483.37,450,150,100,silver,white,action2,x2,s)

def threeButtons(text1,text2,text3, action1, action2, action3, x1, s):
    #generates three buttons
    button(text1,87.5,450,150,100,silver,white,action1,x1,s)
    button(text2,325,450,150,100,silver,white,action2,)
    button(text3,562.5,450,150,100,silver,white,action3)

def button(msg,x,y,w,h,ic,ac,action=None,inp=None,s=None):
    #creates buttons
    #takes arguments: message, x cord, y cord, width, height, action, variable that is passed through action, and if selection needs to be reset
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
    #changes page variables to change what is visible on display
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
    #changes page variables to change what is visible on display
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
    #changes page variables to change what is visible on display
    global viewStore
    global viewSell
    global selection

    if viewStore == True:
        viewStore = False
        selection = None
        viewSell = True
        print("sell")
        return
    else:
        viewStore = True
        viewSell = False
        print("store")
        return

def switchFieldPlant():
    #changes page variables to change what is visible on display
    global viewField
    global plant
    global selection

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
#sets selection to object in store
    global selection
    selection = objects.store[item]

def selectPlot(plot):
#sets selection to plot number (list possition)
    global selection
    selection = plot

def selectInv(item):
#sets selection to object at position item in plater.inv
    global selection
    selection = player.inv[item]

def plantPick():
#if a plot is selected, if an empty plot runs switchFieldPlant, if grown plant runs field.pick
    global selection
    if selection == None:
        None
    elif field.field[selection] == "Empty":
        selection = None
        switchFieldPlant()
    elif field.field[selection] != "Empty" and field.furtTracker[selection] == 0:
        field.pick(selection)

def characterSetUp(x):
# creates player object, creates inventory, creates field
    global field
    global player
    player = objects.player(x,20)
    player.createInventory()
    field = objects.field(3)
    field.createField()
    print("CHARA CREATED")

# buy and sell items
def purchase(x):
#if sufficient funds and inv space, add item to inventory and subtracts cost from bank
    if player.bank - x.cost >= 0:
        if x.name == "Plot":
            field.addPlot()
            player.bank = player.bank - x.cost
        elif len(player.inv) == 20:
            print("inv full")
        else:
            player.addInventory(x)
            player.bank = player.bank - x.cost

def sell(x):
#removes item from inventory and adds worth to player bank
    global selection
    player.bank = player.bank + x.worth
    player.subInventory(x)
    selection = None

