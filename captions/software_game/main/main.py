import pygame, sys
from pygame.locals import *
import datetime
import random

#initialixation
pygame.init()

#const resources
RUN = True # game's main loop variable
DELAY = 2000
display1 = pygame.display.set_mode((0,0),(pygame.NOFRAME|pygame.FULLSCREEN))
display_info = pygame.display.Info()
display_height = display_info.current_h
display_width = display_info.current_w
print(pygame.image.get_extended())
STATE1 = 1
STATE2 = 1
STATE3 = 1
STATE4 = 1

BACKGROUNDIMAGE = pygame.image.load("../res/images/night_sky.png")
MOLE1_STATE = pygame.image.load("../res/images/mole_hole.png")
MOLE2_STATE = pygame.image.load("../res/images/mole.png")
MOLE3_STATE = pygame.image.load("../res/images/mole_red.png")
MOLE4_STATE = pygame.image.load("../res/images/mole_green.png")

LEVEL = "1"
SCORE = "0"
DEVICE = 0 # make it work on different devices
SCREEN= (124)
res_1280X1024 = ""
res_1366X768 = ""

def get_res():
    #code to load res according to display
    return("../res")

def load_resources_prelim():
    if(DEVICE==""):
        BACKGROUNDIMAGE1 = {src:pygame.image.load() , size:()}
        BACKGROUNDIMAGE2 = {src:pygame.image.load() , size:()}
        BACKGROUNDIMAGE3 = {src:pygame.image.load() , size:()}
        BACKGROUNDIMAGE4 = {src:pygame.image.load() , size:()}
        BACKGROUNDIMAGE5 = {src:pygame.image.load() , size:()}
        BACKGROUNDIMAGE6 = {src:pygame.image.load(), size:()}
        image_set = {}

        mole1 = {src:pygame.image.load() , size:()}
        mole2 = {src:pygame.image.load() , size:()}
        mole3 = {src:pygame.image.load() , size:()}
        level1 = {imgset:(),time:(),win:()}
        level2 = {imgset:(),time:(),win:()}
        level3 = {imgset:(),time:(),win:()}

def load_resources_main():
    if(LEVEL==1):
        mole_set = ()
    elif(LEVEL==2):
        mole_set = ()


def display_prelim():
    global display1
    display1.blit(BACKGROUNDIMAGE, (0,0))
    font1 = pygame.font.SysFont('Comic Sans MS', 30)

    #score board
    label1 = font1.render("Score", True , (50,0,0))
    score_value= font1.render(SCORE, False ,(50,50,0))
    #level value
    label2 = font1.render("Level", True, (50,0,0))
    level_value = font1.render(LEVEL, True,(50,50,0))

    #blits
    #level
    display1.blit(label2,((display_width-200),0))
    display1.blit(level_value,(display_width-50,0))
    #score
    display1.blit(label1,((display_width-200),30))
    display1.blit(score_value,(display_width-50,30))


    display1.blit(MOLE1_STATE,(display_width/2-80,display_height/2-80))
    display1.blit(MOLE1_STATE,(display_width*1/8-80,display_height*3/4))
    display1.blit(MOLE1_STATE,(display_width/2-80, display_height*3/4))
    display1.blit(MOLE1_STATE,(display_width*7/8-80, display_height*3/4))


def state_seter(r0=5):
    global LEVEL
    r1 = random.randint(2,4)
    while r1 == r0:
        r1 = random.randint(2,4)
    global STATE1 , STATE2, STATE3, STATE4
    r2 = random.randint(2,int(LEVEL)+1)
    STATE1 = 1
    STATE2 = 1
    STATE3 = 1
    STATE4 = 1
    if(r1 == 1):
        STATE1 = r2
    elif(r1 == 2):
        STATE2 = r2
    elif(r1 == 3):
        STATE3 = r2
    elif(r1 == 4):
        STATE4 = r2
    else:
        pass

    return(r1)



def display_main():
    global display1
    font1 = pygame.font.SysFont('Comic Sans MS', 30)
    #moles
    display1.blit(BACKGROUNDIMAGE, (0,0))

    #score board
    label1 = font1.render("Score", True , (50,0,0))
    score_value= font1.render(SCORE, False ,(50,50,0))
    #level value
    label2 = font1.render("Level", True, (50,0,0))
    level_value = font1.render(LEVEL, True,(50,50,0))

    #blits
    #level
    display1.blit(label2,((display_width-200),0))
    display1.blit(level_value,(display_width-50,0))
    #score
    display1.blit(label1,((display_width-200),30))
    display1.blit(score_value,(display_width-50,30))


    if(STATE1 ==1):
        display1.blit(MOLE1_STATE, (display_width/2-80,display_height/2-80))
    elif(STATE1 == 2):
        display1.blit(MOLE2_STATE, (display_width/2-80,display_height/2-80))
    elif(STATE1 == 3):
        display1.blit(MOLE3_STATE, (display_width/2-80,display_height/2-80))
    elif(STATE1 == 4):
        display1.blit(MOLE4_STATE, (display_width/2-80,display_height/2-80))

    if(STATE2 ==1):
        display1.blit(MOLE1_STATE, (display_width*1/8-80,display_height*3/4))
    elif(STATE2 == 2):
        display1.blit(MOLE2_STATE, (display_width*1/8-80,display_height*3/4))
    elif(STATE2 == 3):
        display1.blit(MOLE3_STATE, (display_width*1/8-80,display_height*3/4))
    elif(STATE2 == 4):
        display1.blit(MOLE4_STATE, (display_width*1/8-80,display_height*3/4))

    if(STATE3 ==1):
        display1.blit(MOLE1_STATE, (display_width/2-80, display_height*3/4))
    elif(STATE3 == 2):
        display1.blit(MOLE2_STATE, (display_width/2-80, display_height*3/4))
    elif(STATE3 == 3):
        display1.blit(MOLE3_STATE, (display_width/2-80, display_height*3/4))
    elif(STATE3 == 4):
        display1.blit(MOLE4_STATE, (display_width/2-80, display_height*3/4))


    if(STATE4 ==1):
        display1.blit(MOLE1_STATE, (display_width*7/8-80, display_height*3/4))
    elif(STATE4 == 2):
        display1.blit(MOLE2_STATE, (display_width*7/8-80, display_height*3/4))
    elif(STATE4 == 3):
        display1.blit(MOLE3_STATE, (display_width*7/8-80, display_height*3/4))
    elif(STATE4 == 4):
        display1.blit(MOLE4_STATE, (display_width*7/8-80, display_height*3/4))


def background():
    time = datetime.dateime.now()
    if(time.hour <= 7):
        return(BACKGROUNDIMAGE1)
    elif(time.hour <= 10):
        return(BACKGROUNDIMAGE2)
    elif(time.hour <=13):
        return(BACKGROUNDIMAGE3)
    elif(time.hour <= 18):
        return(BACKGROUNDIMAGE4)
    elif(time.hour <= 19):
        return(BACKGROUNDIMAGE5)
    elif(time.hour < 25):
        return(BACKGROUNDIMAGE6)
    else:
        # special # WARNING:            $
        pass

def win():
    global display1 ,RUN
    display1.blit(BACKGROUNDIMAGE,(0,0))
    font2 = pygame.font.SysFont('Comic Snas MS', 180)
    label3 = font2.render("CONGRATULATION", True, (50,50,50))
    font3 = pygame.font.SysFont('Comic Snas MS', 100)
    label4 = font3.render("YOU HAVE WON THE GAME", True, (50,0,0))

    display1.blit(label3, (display_width/8, display_height/2))
    display1.blit(label4, (display_width/8, display_height*3/4))
    pygame.display.update()
    RUN = False

def game_over():
    global display1 ,RUN
    display1.blit(BACKGROUNDIMAGE,(0,0))
    font2 = pygame.font.SysFont('Comic Snas MS', 180)
    label5 = font2.render("GAME OVER", True, (50,50,50))
    display1.blit(label5, (display_width/8, display_height/2))
    pygame.display.update()
    RUN = False



if(__name__ == "__main__"):
    pygame.time.delay(5000)
    display_prelim()
    pygame.display.update()
    r=5#fisrt random

    while RUN:
        for event in pygame.event.get():
            if(event.type == KEYDOWN and event.key == K_s):
                while RUN:
                    r = state_seter(r)
                    #display_prelim()
                    display_main()
                    pygame.display.update()
                    pygame.time.delay(DELAY)
                    type = False
                    for event in pygame.event.get():
                        type = True
                        if(event.type == KEYDOWN and event.key == K_ESCAPE):
                            pygame.quit()
                            sys.exit()
                        elif(event.type == KEYDOWN and event.key == K_w):
                            if(STATE1 == 2):
                                SCORE = str(int(SCORE)+10)
                            elif(STATE1 == 3):
                                SCORE = str(int(SCORE)-5)
                            elif(STATE1 == 4):
                                SCORE = str(int(SCORE)-10)
                            else:
                                SCORE = str(int(SCORE)-10)
                        elif(event.type == KEYDOWN and event.key == K_a):
                            if(STATE2 == 2):
                                SCORE = str(int(SCORE)+10)
                            elif(STATE2 == 3):
                                SCORE = str(int(SCORE)-5)
                            elif(STATE2 == 4):
                                SCORE = str(int(SCORE)-10)
                            else:
                                SCORE = str(int(SCORE)-10)
                        elif(event.type == KEYDOWN and event.key == K_s):
                            if(STATE3 == 2):
                                SCORE = str(int(SCORE)+10)
                            elif(STATE3 == 3):
                                SCORE = str(int(SCORE)-5)
                            elif(STATE3 == 4):
                                SCORE = str(int(SCORE)-10)
                            else:
                                SCORE = str(int(SCORE)-10)
                        elif(event.type == KEYDOWN and event.key == K_d):
                            if(STATE4 == 2):
                                SCORE = str(int(SCORE)+10)
                            elif(STATE4 == 3):
                                SCORE = str(int(SCORE)-5)
                            elif(STATE4 == 4):
                                SCORE = str(int(SCORE)-10)
                            else:
                                SCORE = str(int(SCORE)-10)

                        elif(event.type == KEYDOWN):
                            SCORE = str(int(SCORE)-5)
                    if(type == False and STATE1==2 and STATE==2 and STATE3==2 and STATE4==2):
                            SCORE = str(int(SCORE)-5)

                    if(int(SCORE) >= 100):
                        LEVEL = str(int(LEVEL)+1)
                        DELAY = DELAY -500
                        SCORE = "0"
                    elif(int(SCORE) < 0):
                        game_over()

                    elif(int(LEVEL) == 3 and SCORE >=100):
                        win()
            if(event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
    while True:
            for event in pygame.event.get():
                type = True
                if(event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()


                    #display_main()

                    print("Frame")
