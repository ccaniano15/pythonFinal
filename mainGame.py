import objects
import functions
import pygame, sys

pygame.init()
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Farm Life: Live your best farm life!')
clock = pygame.time.Clock()

field = True
store = False

black = (0,0,0)
white = (255,255,255)
lightYellow = (255, 250, 234)
silver = (192,192,192)

def locationSwitch():
    global field
    global store
    if field == True:
        field = False
        store = True
    elif store == True:
        store = False
        field = True       

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def rect(x, y, w, h, color):
    pygame.draw.rect(gameDisplay, color, [x, y, w, h])

def threeButtons(actionThree):
    click = pygame.mouse.get_pressed()

    pygame.draw.rect(gameDisplay, silver,(87.5,450,150,100))
    pygame.draw.rect(gameDisplay, silver,(325,450,150,100))
    pygame.draw.rect(gameDisplay, silver,(562.5,450,150,100))

    if 562.5+150 > pygame.mouse.get_pos()[0] > 562.5 and 450+100 > pygame.mouse.get_pos()[1] > 450:
        if click[0] == 1:
            actionThree



def threeButtonsLabels(text1, text2, text3):
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects(text1, smallText)
        textRect.center = (87.5+(150/2)), (450+(100/2))
        gameDisplay.blit(textSurf, textRect)

        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects(text2, smallText)
        textRect.center = (325+(150/2)), (450+(100/2))
        gameDisplay.blit(textSurf, textRect)

        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects(text3, smallText)
        textRect.center = (562.5+(150/2)), (450+(100/2))
        gameDisplay.blit(textSurf, textRect)

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',40)
        TextSurf, TextRect = text_objects('Farm Life: Live your best farm life!', largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(15)

def game_loop():
    
    crashed = False

    while crashed == False:

        gameDisplay.fill(white)
        rect(0, 400, 800, 200, lightYellow)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            print(event)
            
        if store == True:
            threeButtons(locationSwitch())
            threeButtonsLabels("Buy","Sell","Field")

        if field == True:
            threeButtons(locationSwitch())
            threeButtonsLabels("Fertilize", "Plant/Pick", "Store") 
            
        pygame.display.update()
        clock.tick(60)


game_loop()
