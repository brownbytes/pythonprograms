#######################
#name :nibbles........#
#author :durga........#
#######################

import pygame,sys,random,time
from pygame.locals import *

#deinfe a board, blit tiles and create a array of tile with position and seq numbers
boardwidth = 360
boardheight = 360
board = pygame.display.set_mode((boardwidth,boardheight))# creates a surface
board.fill((0,0,0))
tilesize = 11
tilegap = 1

tilegapsize = tilesize+tilegap

tilesperrow = boardwidth/(tilegapsize)
tilespercol = boardheight/(tilegapsize)

tileposdict = {} # to store the tile and row,col mapping
tiledict = {} #to store row,col and tile image mapping
FPS = 5

for col in range(0,tilespercol):
    for row in range(0,tilesperrow):
        tileposdict[(col,row)] = [col*(tilegapsize),row*(tilegapsize)]

for key in tileposdict.keys():
    tiledict[key] = pygame.Surface((tilesize,tilesize))
    tiledict[key].fill((0,255,200))
    board.blit(tiledict[key],tileposdict[key])
    pygame.display.update()

worm =[] #stores the positions of worm (all thr worm segments). All tiles in worm are coloured as worm :D
apple_pos =()

apple = None

direction = None # stores the current direction of motion of worm
direction  = 'left'

###defining worm class

class WORM():
    def __init__(self):
        # initialise a list which contains the worm positions.The list can be appended as the worm grows in size
        global worm 
        worm_head = random.choice(tiledict.keys()) # first block of worm
        worm_tail = worm_head[0] + 1, worm_head[1]
        worm.append(worm_head)
        worm.append(worm_tail)
        
        
    def eat_apple(self):
        #func to check collision points between apple and worm. If yes increase the lenght of worn
        wormtemp = [0,0]
        if apple_pos == worm[0]:
            wormtemp[0],wormtemp[1] = worm[len(worm)-1][0],worm[len(worm)-1][1]
            
            if direction == 'left':
                self.move_left()
                worm.append((wormtemp[0]+1,wormtemp[1])) #increase the lenght from the tail end
            elif direction == 'right':
                self.move_right()
                worm.append((wormtemp[0]-1,wormtemp[1]))
            elif direction == 'up':
                self.move_up()
                worm.append((wormtemp[0],wormtemp[1]+1))                    
            elif direction == 'down':
                self.move_down()
                worm.append((wormtemp[0],wormtemp[1]-1))
            create_worm()
            create_apple()
        
    def move_left(self):
        #func to move the worm left
        global worm
        wormtemp = []
        wormtemp_head = (worm[0][0]-1,worm[0][1])# alinging the head to left.wormtemp_head stores new head coords
        wormtemp.append(wormtemp_head)
        for seg in range(len(worm)-1): # to update the new coorinate of worm in the worm list (moving 1 block to left)and align rest of body w.r.t head
            wormtemp.append(worm[seg])
        worm = wormtemp
        create_worm()
       
    def move_right(self):
        #func to move the worm right
        global worm
        wormtemp = []
        wormtemp_head = (worm[0][0]+1,worm[0][1])
        wormtemp.append(wormtemp_head)
        for seg in range(len(worm)-1): # to update the new coorinate of worm in the worm list (moving 1 block to left)
            wormtemp.append(worm[seg])
        worm = wormtemp
        create_worm()

    def move_up(self):# the movement is in reference to the worm's head position, ie the first seq.wormtemp_head indicates the new head position
        global worm
        wormtemp = []
        wormtemp_head = (worm[0][0],worm[0][1]-1) #aligngin the head to face up.stores new head position coordinatess
        wormtemp.append(wormtemp_head)
        for seg in range(len(worm)-1):# to update the new coorinate of worm in the worm list.aligning the body w.r.t head(wormtemp_head)
            wormtemp.append (worm[seg])
        worm = wormtemp
        create_worm()
        
    def move_down(self): #the movement is in reference to the worm's head position, ie the first seq
        global worm
        wormtemp = []
        wormtemp_head = (worm[0][0],worm[0][1]+1)#aligning the head to face down. stores new head position coordinates
        wormtemp.append(wormtemp_head)
        for seg in range(len(worm)-1): # to update the new coorinate of worm in the worm list.aligning the body w.r.t head (wormtemp_head)
            wormtemp.append(worm[seg])
        worm = wormtemp
        create_worm()
        
    def bite_self(self):
        #to check if the worm mouth collides with any of the worms body
         if worm[0] in worm[1:]:
             return True
        
    def hit_wall(self):
        #to check if worm has hit the wall. Return True/False
        if worm[0][0] <= 0 or worm[0][0] >= tilesperrow or worm[0][1] <= 0 or worm[0][1] >= tilespercol:
            return True
        else :
            return False
        
    def kill_worm(self):
        #if bite_self or hit_wall are true then the work is dead
        if self.hit_wall() or self.bite_self():
            pygame.quit()
            sys.exit()

###randomly create a apple on the screen
def create_apple():

    global tiledict,board,apple_pos,apple
    apple_pos = random.choice(tiledict.keys())
    apple = pygame.Surface((tilesize,tilesize)) #create an apple
    apple.fill((255,0,0))
    board.blit(apple,tileposdict[apple_pos])

def create_worm():

    wormseg = pygame.Surface((tilesize,tilesize)) #create ony body part seq of worm
    wormseg.fill((137,44,44))
    
    for seq in tileposdict.keys():
        if seq in worm:
            board.blit(wormseg,tileposdict[seq])
        elif seq == apple_pos:
            board.blit(apple,tileposdict[apple_pos])
        else:
            board.blit(tiledict[seq],tileposdict[seq])
       
def game_play():
    pygame.init()
    global direction
    wormmy = WORM() # worm object instance
    create_apple()
    create_worm()

    FPSCLOCK = pygame.time.Clock()
    
    while True:
        
        for event in pygame.event.get():
            
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT :
                if direction == 'up' or direction == 'down':
                    direction = 'left'
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                if direction == 'up' or direction == 'down':
                    direction = 'right'
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                if direction == 'right' or direction == 'left': #only when the worm is heading right or left, up direction is possible. not when the worm is heading down
                    direction  = 'up'
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                if direction == 'right' or direction == 'left':
                    direction  = 'down'
 

        if direction == 'left':
            wormmy.move_left() #the worm moves in the direction till the direction is changes
        elif direction == 'right':
            wormmy.move_right()
        elif direction == 'up':
            wormmy.move_up()
        elif direction == 'down':
            wormmy.move_down()

        wormmy.kill_worm()
        wormmy.eat_apple()
    
        pygame.display.update()
        FPSCLOCK.tick(FPS)

game_play()

