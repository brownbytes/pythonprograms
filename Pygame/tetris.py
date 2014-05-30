
#############
# this is a initial version of tetris, with few static fucntion calls. 
# will be modifying the same later to make rotation of blocks more dynamic

# game:tetris
# name:durga
#language : python
#date:22 feb 2014
############
# the game is a simple emulation of the classic game of tetris.
# major 4 shapes used in the game are : 0,L,J,Z,S,I.
# each shape is made of 4 tiles and based on user interaction the tile orientation can be changed
############
#lot of trial code, need to purge code. 
###



import pygame,random,sys
from pygame.locals import *
from copy import deepcopy

# building the initial board

boardwidth = 200
boardheight = 400

mainboardside = 600
white = (255,255,25)
black = (0,0,0)
yellow =(255,215,0) #color for S
green = (50,205,50) #color for Z
blue =(	30,144,255) #color for L
red = (144,0,0) #color for J
voilet = (148,0,211) # color for I
orange = (255,127,80) # color for O
smokeywhite=(245,245,245) # lines on board
palegreen=(229,255,204)#background
pink = (222,115,135)#color for T

sidemargin = (mainboardside - boardwidth)/2
topmargin  = (mainboardside - boardheight)/2
gap = 1

minoside = 19
minopos = [] # to store the rect pos mapping details.
block = None

spotside = 20 # defining the spots on the board for minos to fit in
spotnum = 0
spotpos ={}
possible_moves = ['right','left','clockwise','anticlockwise','down']
rowdict = {} # stores current status of the board.
rowlist = []
collist = []

for row in range(topmargin,topmargin+boardheight,spotside):
    rowlist = []
    for col in range (sidemargin,sidemargin+boardwidth,spotside):
        spotpos[spotnum]=(col,row)
        rowdict[(col,row)]='False'
        spotnum += 1

for item in range(len(rowdict.keys())):
    if rowdict.keys()[item][1] not in rowlist:rowlist.append(rowdict.keys()[item][1])# of each row cords (col, row) rowlist keeps track of rows
    if rowdict.keys()[item][0] not in collist:collist.append(rowdict.keys()[item][0])# of each col cords (col, row) collist keeps track of cols

directions = ['down','up','right','left']
default_direction = 'down'
all_blocks = {'T_block':pink,'L_block':blue,'J_block':red,'O_block':orange,'Z_block':green,'S_block':yellow,'I_block':voilet}
##### blocks and rotations,orientations

L_block_pos = []
Z_block_pos = []
S_block_pos = []
J_block_pos = []
I_block_pos = []
O_block_pos = []
T_block_pos = []

#### the block needs to rotate w.r.t current position, hence the below modules help us in updating the position as per the lcoation of the block

def L_block(x,y,index):
    global L_block_pos
    L_block_pos = [[[x,y],[x,y+spotside],[x,y+2*spotside],[x+spotside,y+2*(spotside)]],
                   [[x,y],[x+spotside,y],[x+2*spotside,y],[x,y+spotside]],
                   [[x,y],[x+spotside,y],[x+spotside,y+spotside],[x+spotside,y+2*(spotside)]],
                   [[x,y],[x+spotside,y],[x+2*spotside,y],[x+2*spotside,y-spotside]]]
    return L_block_pos[index]

def Z_block(x,y,index):
    global Z_block_pos
    Z_block_pos = [[[x,y],[x+spotside,y],[x+spotside,y+spotside],[x+2*(spotside),y+spotside]],
                   [[x,y],[x+spotside,y],[x+spotside,y-spotside],[x,y+spotside]],
                   [[x,y],[x+spotside,y],[x+spotside,y+spotside],[x+2*(spotside),y+spotside]],
                   [[x,y],[x+spotside,y],[x+spotside,y-spotside],[x,y+spotside]]]

    return Z_block_pos[index]

def S_block(x,y,index):
    global S_block_pos
    S_block_pos = [[[x,y],[x+spotside,y],[x,y+spotside],[x-spotside,y+spotside]],
                    [[x,y],[x,y+spotside],[x+spotside,y+spotside],[x+spotside,y+2*spotside]],
                    [[x,y],[x+spotside,y],[x,y+spotside],[x-spotside,y+spotside]],
                    [[x,y],[x,y+spotside],[x+spotside,y+spotside],[x+spotside,y+2*spotside]]]
    return S_block_pos[index]

def J_block(x,y,index):
    global J_block_pos
    J_block_pos = [[[x,y],[x,y+spotside],[x,y+2*spotside],[x-spotside,y+2*(spotside)]],
                   [[x,y],[x,y+spotside],[x+spotside,y+spotside],[x+2*(spotside),y+spotside]],
                   [[x,y],[x+spotside,y],[x,y+spotside],[x,y+2*spotside]],
                   [[x,y],[x+spotside,y],[x+2*(spotside),y],[x+2*spotside,y+spotside]]]
    return J_block_pos[index]

def O_block(x,y,index):
    global O_block_pos
    O_block_pos = [[[x,y],[x+spotside,y],[x,y+spotside],[x+spotside,y+spotside]],
                   [[x,y],[x+spotside,y],[x,y+spotside],[x+spotside,y+spotside]],
                   [[x,y],[x+spotside,y],[x,y+spotside],[x+spotside,y+spotside]],
                   [[x,y],[x+spotside,y],[x,y+spotside],[x+spotside,y+spotside]]]
    return O_block_pos[index]

def I_block(x,y,index):
    global I_block_pos
    I_block_pos = [[[x,y],[x,y+spotside],[x,y+2*(spotside)],[x,y+3*(spotside)]],
                   [[x,y],[x+spotside,y],[x+2*(spotside),y],[x+3*(spotside),y]],
                   [[x,y],[x,y+spotside],[x,y+2*(spotside)],[x,y+3*(spotside)]],
                   [[x,y],[x+spotside,y],[x+2*(spotside),y],[x+3*(spotside),y]]]
    return I_block_pos[index]

def T_block(x,y,index):
    global T_block_pos
    T_block_pos = [[[x,y],[x+spotside,y],[x+spotside,y+spotside],[x+2*(spotside),y]],
                   [[x,y],[x+spotside,y],[x+spotside,y-spotside],[x+spotside,y+spotside]],
                   [[x,y],[x+spotside,y],[x+spotside,y-spotside],[x+2*spotside,y]],
                   [[x,y],[x,y+spotside],[x,y-spotside],[x+spotside,y]]]
    return T_block_pos[index]


######

SURFACE = pygame.display.set_mode((mainboardside,mainboardside))
SURFACE.fill(palegreen)

board = None

FPS = 5

def control_panel():#displays the control panel on the display surface
    # rightarrow -moveright; leftarrow-moveleft ;  uparrow - rotate right ;downarrow -rotate left ; 'spacebar' - harddrop
    font1 = pygame.font.Font(None,20)
    font2 = pygame.font.Font(None,17)
    banner1 = font1.render('CONTROLS:',1,black)
    banner2 = font2.render('right-arrow::move right',1,black)
    banner3 = font2.render('left-arrow::move left',1,black)
    banner4 = font2.render('up-arrow::rotate clockwise',1,black)
    banner5 = font2.render('down-arrow::rotate anti-clockwise',1,black)
    banner6 = font2.render('space-bar::hard-drop the block',1,black)

    SURFACE.blit(banner1,(10,(topmargin+10)))
    SURFACE.blit(banner2,(10,(topmargin+25)))
    SURFACE.blit(banner3,(10,(topmargin+40)))
    SURFACE.blit(banner4,(10,(topmargin+55)))
    SURFACE.blit(banner5,(10,(topmargin+70)))
    SURFACE.blit(banner6,(10,(topmargin+85)))
       
class Block():
       
    def __init__(self): #called each time a new block has to be displayed.

        global block
        self.generate_block()

    def generate_block(self):
        global block
        block = random.choice(all_blocks.keys())
        self.build_block()


    def build_block(self):
        # the functon builds the block using 4 minos. the intial locations of the minos are stored to display respective block shape'
        global minopos #stores current minos location of each block.
        #the minos are positioned from top to bottom for easy estimation of shape for rotation purposes.
        minopos = []
        if block == 'L_block':
            minopos = L_block(spotpos[4][0],spotpos[4][1],0)
  
        elif block == 'J_block':
            minopos = J_block(spotpos[4][0],spotpos[4][1],0)

        elif block == 'S_block':
            minopos = S_block(spotpos[4][0],spotpos[4][1],0)
            
        elif block == 'T_block':
            minopos = T_block(spotpos[4][0],spotpos[4][1],0)

        elif block == 'Z_block':
            minopos = Z_block(spotpos[4][0],spotpos[4][1],0)

        elif block == 'I_block':
            minopos = I_block(spotpos[4][0],spotpos[4][1],0)

        elif block == 'O_block':
            minopos = O_block(spotpos[4][0],spotpos[4][1],0)

        self.draw_block()
        
    def rotate_block(self,direction): #rotate in lockwise/anticlockwise direction
        global minopos
        global prime
        global orientation
        # if current block position is at r , the next position can be attained by doing an abs value as L_block_pos[len(L_block_pos)//r -1] , which will be cyclic rotation.
        tempr = deepcopy(minopos)
        increment = (4+orientation)%(4)-1
        if direction == 'clockwise':
            orientation = increment
        elif direction == 'anticlockwise':
            orientation = -increment
        
        if block == 'L_block':return L_block(tempr[0][0],tempr[0][1],orientation)

        elif block == 'T_block':return T_block(tempr[0][0],tempr[0][1],orientation)
      
        elif block == 'S_block':return S_block(tempr[0][0],tempr[0][1],orientation)

        elif block == 'Z_block':return Z_block(tempr[0][0],tempr[0][1],orientation)
      
        elif block == 'I_block':return I_block(tempr[0][0],tempr[0][1],orientation)

        elif block == 'J_block':return J_block(tempr[0][0],tempr[0][1],orientation)
      
        elif block == 'O_block':return O_block(tempr[0][0],tempr[0][1],orientation)

        
    def move_block(self,direction): #move in left/right/downwards direction
        global minopos
        global orientation
        #global filledspots
        global vacantspots
        global rowdict
       
        temp =[]
        temp = deepcopy(minopos)
        
        if direction in ['left','right','down']:            
            for nxtmv in temp:
                if direction in possible_moves and direction == 'down':
                    nxtmv[1] += spotside
                if direction in possible_moves and direction == 'left':
                    nxtmv[0] -= spotside
                if direction in possible_moves and direction == 'right':
                    nxtmv[0] += spotside
        elif direction in possible_moves and direction == 'clockwise':
            temp = self.rotate_block('clockwise')
        elif direction in possible_moves and direction == 'anticlockwise':
            temp = self.rotate_block('anticlockwise')
      
        if self.check_boundary(temp):
            minopos = deepcopy(temp) # we dont want duplicate referencing, a temp = minopos[:] does shallow copy and any modification in temp, modifies minopos too, thus defeating the purpose of a temp
        if  'down' not in possible_moves: # if there are no possible moves down wards, update the rowdict to reflect the color of the tile
            for mino in minopos:
                rowdict[tuple(mino)] = all_blocks[block]
            check_row()
            self.generate_block()
        self.draw_block()
        

    def draw_block(self):
        # draw a mino at the minopos       
        for i in range(len(minopos)):
           pygame.draw.rect(SURFACE,all_blocks[block],pygame.Rect(minopos[i],(minoside,minoside)))

           
    def check_boundary(self,temp):
        # checking if the next move is a valid move or not. only if the move is valid, the minopos is updated with next move cooridinates, and corresonding rowdic key is updated with block color
        # 3.when a mino hits the side wall, the verification stops at th first mino , thus breaking the loop everytime at index 0.
        # which results on the tile leaking below the lower boundary as, the boundary gets checked only for index 0 tile
        # also remove left only when its apossible direction, when the tile already hits the left boudnary no point removing left as there is no left
        # the below code also cheks for overlap, if the rowdict(col,row) is not false => there is a block.
        
        global possible_moves
        possible_moves = ['right','left','clockwise','anticlockwise','down']
        move =[]
        for nxtmv in temp:

            if tuple(nxtmv) in rowdict.keys():
                
                if not(topmargin+boardheight-spotside >= nxtmv[1]) or rowdict[tuple(nxtmv)]!= 'False': # if the nxtmv is not within the boundary and if nxtmv is not empty, then dont move downardsa
                    if 'down' in possible_moves and direction == 'down' : possible_moves.remove('down') # only if the block is moving downwards this block of code needs to be executed               
                    move.append('False')
                    break           

                if not(nxtmv[0] >= sidemargin) or rowdict[tuple(nxtmv)]!= 'False':
                    if 'left' in possible_moves : possible_moves.remove('left')
                    move.append('False')
                    #break # --3
                
                if not(nxtmv[0] <= sidemargin+boardwidth-spotside) or rowdict[tuple(nxtmv)]!= 'False':
                    if 'right' in possible_moves : possible_moves.remove('right')
                    move.append('False')
                    #break

            elif tuple(nxtmv) not in rowdict.keys():
                if topmargin+boardheight-spotside <= nxtmv[1]: #if the nxtmv is outside the bottom the box, dont move downwards
                    if 'down' in possible_moves:possible_moves.remove('down')
                    move.append('False')
                    break
                if nxtmv[0] <= sidemargin:
                    if 'left' in possible_moves : possible_moves.remove('left')
                    move.append('False')
                if nxtmv[0] >= sidemargin+boardwidth-spotside:
                    if 'right' in possible_moves : possible_moves.remove('right')
                    move.append('False')
                
        
        if 'False' in move : return False
        else : return True
                      
        
def draw_board():

    global board,SURFACE
    board = pygame.Rect((sidemargin,topmargin),(boardwidth,boardheight)) #defining a rect obj to be drawn on surface
    pygame.draw.rect(SURFACE,black,board)   

    for i in range(0,boardwidth/spotside):#draw vertical lines
        pygame.draw.line(SURFACE,smokeywhite,(sidemargin+(i*spotside),topmargin),(sidemargin+(i*spotside),topmargin+boardheight),1) #draw vertical lines for grid

    for j in range(0,boardheight/spotside): #draw horizontal lines
        pygame.draw.line(SURFACE,smokeywhite,(sidemargin,topmargin+(j*spotside)),(sidemargin+boardwidth,topmargin+(j*spotside)),1) #draw vertical lines for grid

    pygame.display.update()

def update_board():

    for rec in rowdict.keys():
        if rowdict[rec] != 'False':
            pygame.draw.rect(SURFACE,rowdict[rec],pygame.Rect(rec,(minoside,minoside)))
      
    pygame.display.update()


def check_row():
    # picks each row and checks if all the cols in the row are filled? returns true if filled, else returns false.
    global rowdist
    global collist
    sortedrow = sorted(rowlist) # to check the cols of the bottom-most row and not the top most row
    sortedcol = sorted(collist)
    
    for rowid in range(len(sortedrow)-1,0,-1):
        remove  = [] # resetting the remove list for each row. else it increments arithmatically for each row.
        for col in range(len(sortedcol)):
            if rowdict[(sortedcol[col],sortedrow[rowid])] =='False':
                remove.append('False')
            else:
                remove.append('True')
        
        if remove.count('True') == len(collist) or remove.count('False') == len(collist):
            for coll in collist: # if all cols in a row are filled resetting the row to reflect tiles in upper block              
                rowdict[(coll,sortedrow[rowid])] = rowdict[(coll,sortedrow[rowid-1])] # replicate the above row in the vacant row.
                rowdict[(coll,sortedrow[rowid-1])] = 'False' # first make the row as an empty row
        #elif remove.count('False') == len(collist):
            #for coll in collist:
                #rowdict[(coll,sortedrow[rowid])] = rowdict[(coll,sortedrow[rowid-1])]
        else:
            pass
        

def main_game():
    global direction #stores the action of the player
    global orientation # stores the current seq of block being diplayed.
    orientation = 0
    pygame.font.init()
    control_panel()
    single_block = Block()
    FPSCLOCK = pygame.time.Clock()
    while True:
        direction = 'down'
        for event in pygame.event.get():
            if event.type == QUIT: 
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                direction = 'right'

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                direction = 'left'                

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                direction = 'clockwise'

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                direction = 'anticlockwise'
                
        draw_board()
        single_block.move_block(direction)
        update_board()
        FPSCLOCK.tick(FPS)
pygame.display.init()

main_game()

