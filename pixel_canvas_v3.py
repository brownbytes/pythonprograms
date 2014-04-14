#usr/bin/env python
#author:durga
#creates a pixie canvas
#creates a color palete
#can have a grid or no grid settings

import pygame,sys
from pygame.locals import *

#initialise colors:

COLOR_PALETTE = {'AQUA':(0,255,255,255),'BLACK':(0,0,0,255),'BLUE':(0,0,255,255),
                       'FUCHSIA':(255,0,255,255),'MAROON2':(227,25,25),'GRAY':(128,128,128,255),
                       'GREEN':(0,128,0,255),'PALEGOLD':(238,232,170,255),'BISCUI':(238,213,183),
                       'PERU':(205,133,63),'LIME':(0,255,0,255),'MAROON':(128,0,0,255),
                       'NAVYBLUE':(0,0,128,255),'OLIVE':(128,128,0,255),'PURPLE':(128,0,128,255),
                       'RED':(255,0,0,255),'SILVER':(192,192,192,255),'TEAL':(0,128,128,255),
                       'WHITE':(255,255,255,255),'YELLOW':(255,255,0,255)}

action = None
cur_color = COLOR_PALETTE['WHITE']

LEFT_MARGIN = 50
RIGHT_MARGIN = 100
TOP_MARGIN = 75
GAP = 1
no_of_pixels = ' '
CANVASSIDE = 800
PIXIESIDE = 15
COLORTABSIDE = 20
LAYOUT_WIDTH = 700
LAYOUT_HEIGHT  = 750

TOOLBOX_HT = 40
TOOLBOX_WD = 700

blit_pos = {}
color_map = {}
layout = None
palette = None
toolbox = None

class CANVAS(object): # initialise a canvas

    draw_rect = None# gets the size of the start button , which is a surface returned by font
    grid_rect = None
    corner_rect = None
    erase_rect = None
    done_rect = None
    reset_rect = None

    #initialise a canvas of side canvasside, and fill with default color
    def __init__(self):
        self.canvas = pygame.display.set_mode((CANVASSIDE,CANVASSIDE))
        self.canvas.fill(cur_color)
        self.display_palette()
        self.display_panel()
        self.get_corners()
        self.display_layout()

    def display_layout(self):
        global layout
        layout = pygame.Rect((LEFT_MARGIN,TOP_MARGIN),(LAYOUT_WIDTH,LAYOUT_HEIGHT))
        pygame.draw.rect(self.canvas,COLOR_PALETTE['GRAY'],layout,0)
        #self.function_panel('CORNER')


    # displas color palette
    def display_palette(self):
        global palette
        row = LAYOUT_WIDTH+LEFT_MARGIN + 10
        col = TOP_MARGIN
        palette = pygame.Rect((row,col,75,500))
        pygame.draw.rect(self.canvas,COLOR_PALETTE['BLACK'],palette,1)
            
        for color in COLOR_PALETTE:
            pygame.draw.rect(self.canvas,COLOR_PALETTE[color],(row,col,COLORTABSIDE,COLORTABSIDE))
            col += COLORTABSIDE

    # draw 4 static buttons START,GRID,CORNER,DONE
    def display_panel(self):
        global toolbox

        global draw_rect,grid_rect,corner_rect,erase_rect,done_rect,reset_rect

        toolbox = pygame.Rect((LEFT_MARGIN,10),(TOOLBOX_WD,TOOLBOX_HT))
        
        pygame.draw.rect(self.canvas,COLOR_PALETTE['GRAY'],toolbox,0)

        font = pygame.font.match_font('couriernew', bold=True, italic=False) # returns the path to all system font objects obtained from pygame.font.get_fonts()

        font1 = pygame.font.Font(font,20) #DRAW
        font3 = pygame.font.Font(font,20) #CORNER
        font4 = pygame.font.Font(font,20) #DONE
        font5 = pygame.font.Font(font,20) #ERASE
        font6 = pygame.font.Font(font,20) #RESET
        
        draw_button = font1.render('draw',1,COLOR_PALETTE['BLACK'],COLOR_PALETTE['SILVER'])
        corner_button = font3.render('dots',1,COLOR_PALETTE['BLACK'],COLOR_PALETTE['SILVER'])
        done_button = font4.render('finish',1,COLOR_PALETTE['BLACK'],COLOR_PALETTE['SILVER'])
        erase_button = font5.render('erase',1,COLOR_PALETTE['BLACK'],COLOR_PALETTE['SILVER'])
        reset_button = font6.render('reset',1,COLOR_PALETTE['BLACK'],COLOR_PALETTE['SILVER'])
        
        self.canvas.blit(draw_button,(60,15))
        self.canvas.blit(corner_button,(250,15))
        self.canvas.blit(erase_button,(350,15))
        self.canvas.blit(done_button,(450,15))
        self.canvas.blit(reset_button,(550,15))

        draw_rect = pygame.Rect((60,15),pygame.Surface.get_size(draw_button))# gets the size of the draw button , which is a surface returned by font
        corner_rect = pygame.Rect((250,15),pygame.Surface.get_size(corner_button))
        erase_rect = pygame.Rect((350,15),pygame.Surface.get_size(erase_button))
        done_rect = pygame.Rect((450,15),pygame.Surface.get_size(done_button))
        reset_rect = pygame.Rect((550,15),pygame.Surface.get_size(reset_button))
        
    # defines the fucntions of each button the 'start','grid','corner','done' buttons.
    def function_panel(self,option):
        global action
        # create rectange objects for all buttons and check of user has clicked any tool box function
        
         # if user clicks on grid, lines have to be displayed
        if option == 'DRAW':
            action = 'DRAW'
            
        elif option == 'CORNER':
            # raw only the interesction points. All the intersection points ie topleft_corner points can be drawn as a 1x1 rect(1 pixiel) in black.           
            for corner in blit_pos.values():
                pygame.draw.rect(self.canvas,COLOR_PALETTE['BLACK'],(corner[0],corner[1],2,2))
            self.update_canvas()

        elif option == 'ERASE':
            action = 'ERASE'

        elif option == 'DONE':
            #draw the points in same color as the existing pixie color
            for _id in blit_pos.keys():
                if _id in color_map.keys():
                    pygame.draw.rect(self.canvas,color_map[_id],(blit_pos[_id][0],blit_pos[_id][1],2,2))
                else:
                    pygame.draw.rect(self.canvas,COLOR_PALETTE['GRAY'],(blit_pos[_id][0],blit_pos[_id][1],2,2))
            
        elif option == 'RESET':
            self.display_layout()
            

    # get user clicks on the toolbox
    def get_option(self,posx,posy):
        
        if draw_rect.collidepoint(posx,posy):
            return 'DRAW'
        
        elif corner_rect.collidepoint(posx,posy):
            return 'CORNER'
        
        elif erase_rect.collidepoint(posx,posy):
            return 'ERASE'
        
        elif done_rect.collidepoint(posx,posy):
            return 'DONE'

        elif reset_rect.collidepoint(posx,posy):
            return 'RESET'

    #update the canvas everytime
    def update_canvas(self):
        pygame.display.update()

    #the below method  fetches the current color of a position
    def get_color(self,posx,posy):
        pixiecolor = self.canvas.get_at((posx,posy)) #returns RGB of color
        if pixiecolor in COLOR_PALETTE.values():
            for color in COLOR_PALETTE.keys():
                if COLOR_PALETTE[color] == pixiecolor:
                    return COLOR_PALETTE[color] #fetch the color name

    def get_corners(self):
        global blit_pos
        x = LEFT_MARGIN
        y = TOP_MARGIN
        pixie_id = 0
        while y < TOP_MARGIN+LAYOUT_HEIGHT:
            x = LEFT_MARGIN
            while x < (LEFT_MARGIN+LAYOUT_WIDTH):
                blit_pos[pixie_id] = [x,y]
                x += PIXIESIDE
                pixie_id += 1
            y += PIXIESIDE



class PIXIE(): # define/initialise a pixie

    def __init__(self): # draw a rectangle of side pixie at corner positions as stored in blitpos
        self.DEFAULT = 'WHITE'

    def draw_pixie(self,canvas,topleft_corner,color): # draw a rectangle at coordinates 'topleft_corner' of a Surface. Each pixie has a topleft_corner cord in surface where it can be drawn
        pygame.draw.rect(canvas,cur_color,(topleft_corner[0],topleft_corner[1],PIXIESIDE,PIXIESIDE),0)

    def erase_pixie(self,canvas,topleft_corner):
        pygame.draw.rect(canvas,COLOR_PALETTE['GRAY'],(topleft_corner[0],topleft_corner[1],PIXIESIDE,PIXIESIDE),0)                           
        
    def click(self,posx,posy,canvas):
        global cur_color  # RGB
        global color_map #id:color

        for ID in blit_pos.keys():
            if (blit_pos[ID][0] <= posx < blit_pos[ID][0]+PIXIESIDE) and (blit_pos[ID][1] <= posy < blit_pos[ID][1]+PIXIESIDE):
                corner= blit_pos[ID]
                
                if action == 'DRAW':
                    print "in draw"
                    self.draw_pixie(canvas.canvas,corner,cur_color)
                    color_map[ID]=cur_color
                    
                elif action == 'ERASE':
                    print "in erase"
                    self. erase_pixie(canvas.canvas,corner)
                    del(color_map[ID]) # else s reside of colored dots is left behind on the canvas

def main():
    pygame.init()
    canvas = CANVAS()
    pixiey = PIXIE()
    global cur_color,action
    action = 'DRAW'

    while True:
        for event in pygame.event.get():
            if ((event.type == QUIT) or (event.type == KEYUP and event.key == K_ESCAPE)):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                (mouse_x,mouse_y) = pygame.mouse.get_pos()
                if palette.collidepoint(mouse_x,mouse_y): # if user clicks in the palette, choose the color
                    cur_color = canvas.get_color(mouse_x,mouse_y)
                elif toolbox.collidepoint(mouse_x,mouse_y): # if user clicks in the toolbox, choose the color
                    option = canvas.get_option(mouse_x,mouse_y)
                    canvas.function_panel(option)
                elif layout.collidepoint(mouse_x,mouse_y): # use the color to color the layout
                    print action
                    pixiey.click(mouse_x,mouse_y,canvas)
                    
        canvas.update_canvas()

main()

        
    
