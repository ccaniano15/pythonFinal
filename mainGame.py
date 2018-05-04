#Base pygame code (general format of the game_looop, text_objects, base of button, and rect functions) from https://pythonprogramming.net/pygame-python-3-part-1-intro/

import objects
import functions
import pygame, sys

#creates colors
black = (0,0,0)
white = (255,255,255)
lightYellow = (255, 250, 234)
silver = (192,192,192)
brown = (139,69,19)
yellow = (255,255,102)
green = (0,128,0)
red = (255, 0, 0)

#creates text sizes
largeText = pygame.font.Font('freesansbold.ttf',40)
smallText = pygame.font.SysFont("comicsansms",20)

def game_intro():
#start the game_intro loop. generates two buttons, one that runs main game_loop one that runs instructions
    
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        functions.gameDisplay.fill(white)
        TextSurf, TextRect = functions.text_objects('Farm Life: Live your best farm life!', largeText)
        TextRect.center = ((functions.display_width/2),(functions.display_height/2))
        functions.gameDisplay.blit(TextSurf, TextRect)

        functions.button("Farm!",350,450,100,50,silver,white,game_loop)
        functions.button("Instructions!",350,510,100,50,silver,white,instructions)
        
        pygame.display.update()
        functions.clock.tick(15)
        
def instructions():
#displays instruction text on new display
    
    instructions = True

    while instructions:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        functions.gameDisplay.fill(white)
        
        TextSurf, TextRect = functions.text_objects("Welcome to Farm Life! A relaxing game about farming!", smallText)
        functions.gameDisplay.blit(TextSurf, (90,125))
        TextSurf, TextRect = functions.text_objects("Go to the store and buy some seeds!", smallText)
        functions.gameDisplay.blit(TextSurf, (90,140))
        TextSurf, TextRect = functions.text_objects("Plant them and fertilize them to grow!", smallText)
        functions.gameDisplay.blit(TextSurf, (90,155))
        TextSurf, TextRect = functions.text_objects("Yellow plants mean they need more fertilizer, green plants mean they are ready to pick!", smallText)
        functions.gameDisplay.blit(TextSurf, (90,170))
        TextSurf, TextRect = functions.text_objects("Pick and sell your grown plants back to the store!", smallText)
        functions.gameDisplay.blit(TextSurf, (90,185))
        TextSurf, TextRect = functions.text_objects("Use your money to buy more plants and plots!", smallText)
        functions.gameDisplay.blit(TextSurf, (90,200))
        TextSurf, TextRect = functions.text_objects("A Note: in the top left corner it shows you what is selected.", smallText, red)
        functions.gameDisplay.blit(TextSurf, (90,225))
        TextSurf, TextRect = functions.text_objects("If it says “None” and you try to perform an action (like picking a plant) the game may crash!", smallText, red)
        functions.gameDisplay.blit(TextSurf, (90,240))
        
        functions.button("Back",350,510,100,50,silver,white,game_intro)
        pygame.display.update()
        functions.clock.tick(15)
                    
def game_loop():
#main game loop. determines what to display based on what pages are set to True in functions file
    
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
            #creates fertilize, plant/pick, and store buttons. runs generateField function.
            #if Fertilize clicked runs functions.field.furtilize
            #if plant/pick clicked runs functions.plantPick
            #if store clicked runs functions.switchStore
            functions.threeButtons("Fertilize", "Plant/Pick", "Store", functions.field.furtilize, functions.plantPick, functions.switchStoreField, functions.selection,True)
            functions.generateField()
            
        elif functions.viewStore == True:
            #creates buy, sell, and field buttons.
            #if buy clicked runs functions.switchStoreBuy
            #if sell clicked runs functions.switchStoreSell
            #if field clicked runs functions.switchStoreField
            TextSurf, TextRect = functions.text_objects("Welcome to the store!", largeText)
            functions.gameDisplay.blit(TextSurf, ((190),((functions.display_height - 400)/2)))
            functions.threeButtons("Buy","Sell","Field", functions.switchStoreBuy,functions.switchStoreSell,functions.switchStoreField, None, None)
            
        elif functions.buy == True:
            #creates back button. runs functions.generateStore function.
            #if back clicked runs functions.switchStoreBuy
            #if an item is selected, creates buy button
            #if sell button clicked runs functions.purchase
            functions.button("Back",166.67,450,150,100,silver,white,functions.switchStoreBuy)
            if functions.selection != None and functions.player.bank - functions.selection.cost > 0:
                functions.button("Buy",483.37,450,150,100,silver,white,functions.purchase,functions.selection,True)
            functions.generateStore()
            
        elif functions.viewSell == True:
            #creates back button. runs functions.showInv function.
            #if back clicked runs functions.switchStoreSell
            #if item is selected creates sell button
            #if sell is clicked runs functions.sell
            functions.button("Back",166.67,450,150,100,silver,white,functions.switchStoreSell)
            if functions.selection != None:
                functions.button("Sell",483.37,450,150,100,silver,white,functions.sell,functions.selection)
            functions.showInv()
            
        elif functions.plant == True:
            #creates back button. runs functions.showInv function.
            #if back clicked runs functions.switchFieldPlant
            #if item is selected creates plant button
            #if sell is clicked runs functions.plant
            functions.showInv()
            functions.button("Back",166.67,450,150,100,silver,white,functions.switchFieldPlant)
            if functions.selection != None:
                functions.button("Plant",483.37,450,150,100,silver,white,functions.field.plant,functions.selection,True)
        pygame.display.update()
        functions.clock.tick(60)

game_intro()
game_loop()
