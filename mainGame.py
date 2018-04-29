import objects
import functions
import pygame, sys

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

field = True
store = False
buy = False
plant = False

selection = None
    
def switchStoreField():
    global field
    global store
    
    if field == True:
        field = False
        store = True
        print("store")
        return
    else:
        field = True
        store = False
        print("field")
        return
    
def switchStoreBuy():
    global store
    global buy
    
    if store == True:
        store = False
        buy = True
        print("buy")
        return
    else:
        store = True
        buy = False
        print("store")
        return
    
def switchFieldPlant():
    global field
    global plant

    if field == True:
        field = False
        plant = True
    else:
        field = True
        plant = False

def generateStore():
    for item in range(0,2):
        x = objects.store[item]
        button(x.name,213.33 + 293.33 * item,100,80,80,silver,silver,selectStore,item)
    for item in range(0,len(objects.store)):
        y = item + 2
        if y <= len(objects.store) - 1:
            x = objects.store[y]
            button(x.name,66.67 + 146.67 * item,220,80,80,silver,silver,selectStore,item)
          
def generateField():
    for plot in range(0,len(functions.field.field)):
        plot = plot
        if functions.field.field[plot] == "empty":
            button("Empty",30 + 80 * plot,150,50,50,brown,brown,selectPlot,plot)
        elif functions.field.field[plot] != "empty" and functions.field.furtTracker[plot] != 0:
            button(functions.field.field[plot],30 + 80 * plot,150,50,50,yellow,yellow,selectPlot,plot)
        elif functions.field.field[plot] != "empty" and functions.field.furtTracker[plot] == 0:
            button(functions.field.field[plot],30 + 80 * plot,150,50,50,green,green,selectPlot,plot)            

def showInv():
    for item in range(0, len(functions.player.inv)):
        x = 30 + 110 * item
        if x <= display_width:
            y = 100
        elif x > display_width:
            m = display_width/140
            m = item - m
            x = 30 + 80 * m
            y = 200 
            
        button(functions.player.inv[item].name,x,y,80,80,silver,silver,selectInv,item)
        
def selectStore(item):
    global selection
    selection = objects.store[item]

def selectPlot(plot):
    global selection
    selection = functions.field.field[plot]

def selectInv(item):
    selection = functions.player.inv[item]

def plantPick():
    if selection == "empty":
        switchFieldPlant()
    elif selection != "empty" and functions.field.furtTracker == 0:
        None
    
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def rect(x, y, w, h, color):
    pygame.draw.rect(gameDisplay, color, [x, y, w, h])

def twoButtons(text1,text2,action1, action2,x2):
    button(text1,166.67,450,150,100,silver,white,action1)
    button(text2,483.37,450,150,100,silver,white,action2,x2)

def threeButtons(text1,text2,text3, x1, x2, x3):
    
    button(text1,87.5,450,150,100,silver,white,x1)
    button(text2,325,450,150,100,silver,white,x2)
    button(text3,562.5,450,150,100,silver,white,x3)

def button(msg,x,y,w,h,ic,ac,action=None,inp=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None and inp == None:
            action()
        elif click[0] == 1 and action != None and inp != None:
            action(inp) 
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',40)
        TextSurf, TextRect = text_objects('Farm Life: Live your best farm life!', largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Farm!",350,450,100,50,silver,white,game_loop)
        button("Instructions!",350,510,100,50,silver,white,game_loop)
        
        pygame.display.update()
        clock.tick(15)

def game_loop():

    crashed = False
    functions.characterSetUp("Bobby")
    print("GAME START")
    while crashed == False:

        gameDisplay.fill(white)
        rect(0, 400, 800, 200, lightYellow)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            
        if field == True:
            threeButtons("Fertilize", "Plant/Pick", "Store",switchStoreField,plantPick,switchStoreField)
            generateField()
        elif store == True:
            threeButtons("Buy","Sell","Field", switchStoreBuy,switchStoreField,switchStoreField)
        elif buy == True:
            twoButtons("Back", "Confirm", switchStoreBuy, functions.purchase, selection)
            generateStore()
            print(functions.player.bank)
        elif plant == True:
            showInv()
            
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
