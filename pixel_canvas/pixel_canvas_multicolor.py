#!/usr/bin/env python
#author : durga
# the program is a pixel-canvas. clicking on a box colours the box black and double-clicking
#on the same box colours it back to white.
###########


import pygame,sys
from pygame.locals import *

#initialising variables
COLOR = {'AQUA':(0,255,255,255),'BLACK':(0,0,0,255),'BLUE':(0,0,255,255),'FUCHSIA':(255,0,255,255),
'GRAY':(128,128,128,255),'GREEN':(0,128,0,255),'PALEGOLD':(238,232,170,255),'BISCUI':(238,213,183),'PERU':(205,133,63),'LIME':(0,255,0,255),'MAROON':(128,0,0,255),'NAVYBLUE':(0,0,128,255),'OLIVE':(128,128,0,255),'PURPLE':(128,0,128,255),'RED':(255,0,0,255),'SILVER':(192,192,192,255),'TEAL':(0,128,128,255),'WHITE':(255,255,255,255),'YELLOW':(255,255,0,255)}

global curcolor
curcolor='BLACK'

MARGIN = 100
CANVASSIDE = 700
COLORTABWD = 40
COLORTABHT = 20
COLORS_MARGIN_Y = 0
PIXIESIDE = 10
GAP = 2

class PAINT(): #initialise a canvas, paint the boxes

    blitpos = {}    
    
    def __init__(self):
        self.canvas = pygame.display.set_mode((CANVASSIDE,CANVASSIDE))
        self.canvas.fill(COLOR['BLACK'])
        self.freeMarginY = 0 # tracks free y-coordinate in margin for more interfaces to be drawn
        self.plugins = { }

    def blit_pixiey(self,pixiey):
        row = 0
        col = 0
        #check the number of pixiey screens which can fit on the canvas
        pixie_id = 0
        while col < CANVASSIDE:
            row = 0
            while row < (CANVASSIDE-MARGIN):
                self.canvas.blit(pixiey.pixie,(row,col))
                self.blitpos[pixie_id] = [row,col]
                row += (PIXIESIDE+GAP)
                pixie_id += 1
            col += (PIXIESIDE+GAP)

    def blit_colors(self):
        row = CANVASSIDE-MARGIN+10
        col = MARGIN
        for color in COLOR.keys():
            pygame.draw.rect(self.canvas,COLOR[color],(row,col,COLORTABWD,COLORTABHT))
            col += COLORTABHT
        self.freeMarginY = col + COLORTABHT
        global COLORS_MARGIN_Y
        COLORS_MARGIN_Y = self.freeMarginY

    def update_canvas(self):
        pygame.display.update()

    def get_color(self,posx,posy):
        canvascolor = self.canvas.get_at((posx,posy))
        for color in COLOR.keys():
            if COLOR[color] == canvascolor:
                return color
                
    def load_plugins(self):        
        try:
            from plugins.saveload.saveload import SaveLoad   
            self.plugins['saveload'] = SaveLoad(MARGIN, CANVASSIDE, PIXIESIDE, GAP, self)
        except:
            print "Cannot find saveload plugin"

        try:
            from plugins.exportimage.exportimage import ExportImage   
            self.plugins['exportimage'] = ExportImage(MARGIN, CANVASSIDE, PIXIESIDE, GAP, self)
        except:
            print "Cannot find exportimage plugin"
        

class PIXIE(): # each 10*10 box is called a pixie

    clicked = False

    def __init__(self):#intialising a surface known as 'pixie'
        self.pixie = pygame.Surface((PIXIESIDE,PIXIESIDE))
        self.pixie.fill(COLOR['WHITE'])

    def click(self,posx,posy,canvas):#click on a pixie fills the surface pixiey with black
        global curcolor
        outerside = PIXIESIDE+GAP

        if CANVASSIDE-MARGIN <= posx <= CANVASSIDE and posy <= COLORS_MARGIN_Y:
            curcolor = canvas.get_color(posx,posy)

        elif 0<= posx <= CANVASSIDE-MARGIN:
            for id in canvas.blitpos.keys():
                if (canvas.blitpos[id][0] <= posx < canvas.blitpos[id][0]+outerside) and (canvas.blitpos[id][1] <= posy < canvas.blitpos[id][1]+outerside):
                    x = canvas.blitpos[id][0]
                    y = canvas.blitpos[id][1]

                    if canvas.get_color(posx,posy) == 'WHITE':# to fill a empty space with color
                        pygame.draw.rect(canvas.canvas,COLOR[curcolor],(x,y,PIXIESIDE,PIXIESIDE))
                    elif canvas.get_color(posx,posy) != 'WHITE':#if the pixie is already coloured
                        pygame.draw.rect(canvas.canvas,COLOR['WHITE'],(x,y,PIXIESIDE,PIXIESIDE))
def main():
    pygame.init()
    canvas = PAINT()
    pixiey = PIXIE()
    canvas.blit_pixiey(pixiey)
    canvas.blit_colors()
    canvas.load_plugins()
    while True:
        for event in pygame.event.get():
            if ((event.type == QUIT) or (event.type == KEYUP and event.key == K_ESCAPE)):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                (mouse_x,mouse_y) = pygame.mouse.get_pos()
                pixiey.click(mouse_x,mouse_y,canvas)
                for plugin in canvas.plugins.values():
                    plugin.onMouseClick(event)
        canvas.update_canvas()

main()

