#!/usr/bin/env python
# Author: Rahul Anand
# This module provides Save and Load features for Pixel Canvas, in custom data format

##########################################################################################

class SaveLoad():
    self.MARGIN = 100
    self.CANVASSIDE = 700
    self.PIXIESIDE = 10
    self.GAP = 2
    self.canvas = None
    self.saveButton = { 'x': 0, 'y': 0, 'w': 60; 'h': 20, 'color': (255, 255, 255, 255), 'fontcolor': (0, 0, 0, 255) }
    self.loadButton = { 'x': 0, 'y': 0, 'w': 60; 'h': 20, 'color': (255, 255, 255, 255), 'fontcolor': (0, 0, 0, 255) }

    def SaveLoad(self, margin, canvasside, pixieside, gap, canvas):
        self.MARGIN = margin
        self.CANVASSIDE = canvasside
        self.PIXIESIDE = pixieside
        self.GAP = gap
        self.canvas = canvas
        

    def init(self):
        # initialize interface buttons
        x = self.CANVASSIDE - self.MARGIN + 10
		y = MARGIN
		pygame.draw.rect(self.canvas.canvas, COLOR[color], (row,col,COLORTABWD,COLORTABHT))
		col += COLORTABHT
        

    def save(self, filename):
        # save in custom format
        '''
        Text file:
        --------------------------------------
        <savefile identifier>
        <canvas attributes>
        <color arrays, space separated>
        '''
        realPixieSide = self.PIXIESIDE + self.GAP
        for y in range(10): #(CANVASSIDE):
            for x in range(10): #(CANVASSIDE - MARGIN):
                print self.canvas.get_color(x, y), 
                x += realPixieSide                
            print ""
            y += realPixieSide
        

    def load(self, filename):
        # load file and draw on canvas
        pass        

