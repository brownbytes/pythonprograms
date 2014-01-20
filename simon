#####################
#! usr/bin/env python
# simulate
# author :durga
# there is much more to the game , like sound inclusions and other minor animations which I have not done.
###################

import pygame, sys, time, random
from pygame.locals import *


#random shuffling of tiles and high light the tiles in a patern
#storing user clicks
#checking userhighlight and random highlight
#incase user pattern is same as computer pattern append the pattern with next highlight

#defining 4 colours
DYELLOW = (255,255,0)
DRED = (255,51,51)
DGREEN = (0,255,0)
DBLUE = (0,128,255)
darkcolors = [DYELLOW,DRED,DGREEN,DBLUE]

LYELLOW = (255,255,204)
LRED = (255,204,204)
LGREEN = (204,255,204)
LBLUE =(204,229,255)
lightcolors = [LYELLOW,LRED,LGREEN,LBLUE]


BOARDWIDTH = 400
BOARDHEIGHT = 400
tilesize = 150
gapsize = 25#defines tile and gap spaces based on number of tiles
MARGIN = 50
board = pygame.display.set_mode((BOARDWIDTH,BOARDHEIGHT))
chance = 0
TIMEOUT = 10

tilepos = {0:(MARGIN,MARGIN),
           2:(MARGIN,MARGIN+tilesize+gapsize),
           1:(MARGIN+tilesize+gapsize,MARGIN),
           3:(MARGIN+tilesize+gapsize,MARGIN+tilesize+gapsize)} # to store tile pos in the board seq:pos


#naming the color tiles
YELLOW = pygame.Rect(tilepos[0],(tilesize,tilesize))
RED = pygame.Rect(tilepos[1],(tilesize,tilesize))
GREEN  = pygame.Rect(tilepos[2],(tilesize,tilesize))
BLUE = pygame.Rect(tilepos[3],(tilesize,tilesize))

tiledict = {0:YELLOW,1:RED,2:GREEN,3:BLUE} #to store tile and seq number mapping seq:tile
compseq = []

FPS = 10

def restart():
    #restart all the variables and set the game to initial state
    global compseq,chance
    compseq = []
    chance = 0
    #highlight()
            
def blittile(tileno):
    tilenum = tileno
    #called each time a tile is blitted on the board
    for seq in tiledict.keys():
        if seq == tilenum: # if the tile matches the seq , then blit it brigther
            pygame.draw.rect(board,darkcolors[seq],tiledict[seq])
        else: #else blit it in pale color
            pygame.draw.rect(board,lightcolors[seq],tiledict[seq])       
    pygame.display.update()

def userinput(x,y):
    #store the user click positions
    userseq = 0
    userx =x
    usery =y
    for seq in tiledict.keys():
        if tiledict[seq].collidepoint(x,y):
            return seq

def highlight(): # frames the compseq list and highlights the smae
    global compseq
    compseq.append(random.randint(0,3))
    for tilenum in compseq:
        blittile(tilenum) # blits a dark tile only for tht sequence
        pygame.time.wait(500)
    blittile(None) # to blit pale tiles
                                   
    
def main():
    pygame.init()
    pygame.display.update()
    global chance
    userseq = None # chooses the tile number selected by user
    FPSCLOCK = pygame.time.Clock()
    restart()
    userturn = False #flag to store if its user turn to play
    gameover = False # flag to store if game is over
 #   blittile(None) # initially blit all tiles with pale colours

    while not gameover:

        for event in pygame.event.get():

            if event.type == QUIT: # if click on quit button
                pygame.quit()
                sys.exit()

            elif userturn == True and event.type == MOUSEBUTTONDOWN: # if there is a click button action and its user turn then
                x,y = pygame.mouse.get_pos()
                userseq = userinput(x,y)

                if userseq == compseq[chance]: # if user seq is same as the seq in the comp list compseq, blit accordingly and move to compare the next click
                    chance += 1
                    blittile(userseq)
                    pygame.time.delay(500)
                    blittile(None)
                    print userseq

                    if chance == len(compseq): # if the click was last, then game control handed over to the computer
                        userturn = False
                        chance = 0

                elif userseq != compseq[chance]: # if user clicks on incorrect tile, restart the game
                    blittile(userseq)
                    userturn = False
                    gameover = True
                    pygame.time.wait(1000)
            

        if gameover == True: # if game is over. restart the game . the computer generates a new seq
            restart()
            gameover = False

        if userturn == False and gameover == False: # if game not over and , its not user turn, the comp appends another tile to the existing list- compseq
            pygame.display.update()
            pygame.time.wait(1000)
            highlight()
            print compseq
            userturn = True
            
                        
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()
