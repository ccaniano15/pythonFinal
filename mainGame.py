import objects
import functions
import pygame, sys

black = (0,0,0)
white = (255,255,255)
lightYellow = (255, 250, 234)
silver = (192,192,192)
brown = (139,69,19)
yellow = (255,255,102)
green = (0,128,0)

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        functions.gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',40)
        TextSurf, TextRect = functions.text_objects('Farm Life: Live your best farm life!', largeText)
        TextRect.center = ((functions.display_width/2),(functions.display_height/2))
        functions.gameDisplay.blit(TextSurf, TextRect)

        functions.button("Farm!",350,450,100,50,silver,white,game_loop)
        functions.button("Instructions!",350,510,100,50,silver,white,instructions)
        
        pygame.display.update()
        functions.clock.tick(15)
        
def instructions():
    instructions = True

    while instructions:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        functions.gameDisplay.fill(white)
        functions.button("Back",350,510,100,50,silver,white,game_intro)
        pygame.display.update()
        functions.clock.tick(15)
                    
def game_loop():

    crashed = False
    functions.characterSetUp("Bobby")
    print("GAME START")
    while crashed == False:

        functions.gameDisplay.fill(white)
        functions.rect(0, 400, 800, 200, lightYellow)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            
        if functions.viewField == True:
            functions.threeButtons("Fertilize", "Plant/Pick", "Store", functions.field.furtilize, functions.plantPick, functions.switchStoreField, functions.selection,True)
            functions.generateField()
        elif functions.viewStore == True:
            functions.threeButtons("Buy","Sell","Field", functions.switchStoreBuy,functions.switchStoreSell,functions.switchStoreField, None, None)
        elif functions.buy == True:
            functions.button("Back",166.67,450,150,100,silver,white,functions.switchStoreBuy)
            if functions.selection != None:
                functions.button("Buy",483.37,450,150,100,silver,white,functions.purchase,functions.selection,True)
            functions.generateStore()
            print(functions.player.bank)
        elif functions.viewSell == True:
            functions.button("Back",166.67,450,150,100,silver,white,functions.switchStoreSell)
            if functions.selection != None:
                functions.button("Sell",483.37,450,150,100,silver,white,functions.sell,functions.selection)
            functions.showInv()
        elif functions.plant == True:
            functions.showInv()
            functions.button("Back",166.67,450,150,100,silver,white,functions.switchFieldPlant)
            if functions.selection != None:
                functions.button("Plant",483.37,450,150,100,silver,white,functions.field.plant,functions.selection,True)
        pygame.display.update()
        functions.clock.tick(60)

game_intro()
game_loop()
