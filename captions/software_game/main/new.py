import pygame, sys
from pygame.locals import *


#initialization
pygame.init()

#resources
BACKGROUNDIMAGE = pygame.image.load("../res/images/night_sky.png")
MOLE1 = pygame.image.load("../res/images/mole_n1.png")
MOLE1 = pygame.image.fromstring( pygame.image.tostring(MOLE1,"RGBA") , (188,142),"RGBA")
TIGER = pygame.image.load("../res/images/hi.png")
TIGER = pygame.image.fromstring(pygame.image.tostring(TIGER,"RGBA"),(256,256),"RGBA")
score = "0"
level = "1"
font1 = pygame.font.SysFont('Comic Sans MS', 30)




#background
print(pygame.image.get_extended())
pygame.image.load("../res/images/night_sky.png")

#display
display=pygame.display.set_mode((0,0),(pygame.NOFRAME|pygame.FULLSCREEN))
display_info = pygame.display.Info()
display_height = display_info.current_h
display_width = display_info.current_w

#clock
clock = pygame.time.Clock()

#background
display.blit(BACKGROUNDIMAGE, (0,0))

# score board
label1 = font1.render("Score", True , (50,0,0))
score_value= font1.render(score, False ,(50,50,0))
# Level
label2 = font1.render("Level", True, (50,0,0))
level_value = font1.render(level, True,(50,50,0))

#blits
#level
display.blit(label2,((display_width-200),0))
display.blit(level_value,(display_width-50,0))
#score
display.blit(label1,((display_width-200),30))
display.blit(score_value,(display_width-50,30))

#moles
display.blit(MOLE1,(display_width/2-80,display_height/2-80))
display.blit(MOLE1,(display_width*1/8-80,display_height*3/4))
display.blit(MOLE1,(display_width/2-80, display_height*3/4))
display.blit(MOLE1,(display_width*7/8-80, display_height*3/4))

#main game loop
while True:

#event handler
    for event in pygame.event.get():
        if(event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()



'''



#change
def change(image,size):

    var1 = pygame.image.tostring(image,"RGBA",False)
    var2 = pygame.image.fromstring(image,size,"RGBA"",False)
    return(var2)
#change
def change():
    if(device==""):
        print(device)
        #file res switch
    elif(device==""):
        print(device)
    elif(device==""):
        print(device)
    elif(device==""):
        print(device)
    return(device)

#change
def change(lev):
    if(lev==""):
        imageset
    elif(lev==""):
        imageset
    elif(lev==""):
        imageset

#change



#time



#hi



#welcome






#first




#
'''
