#!/usr/bin/env python
# Author: Rahul Anand
# This module provides Save and Load features for Pixel Canvas, in custom data format

##########################################################################################

from libs.PygameButton import PygameButton

class SaveLoad():    

    def __init__(self, margin, canvasside, pixieside, gap, canvas):        
        self.MARGIN = margin
        self.CANVASSIDE = canvasside
        self.PIXIESIDE = pixieside
        self.GAP = gap
        self.canvas = canvas
        x = self.CANVASSIDE - self.MARGIN + 10
        y = self.canvas.freeMarginY + 20  
        # initialize interface buttons
        self.saveButton = PygameButton("save", x, y, w=60, h=20, onclick=self.save, canvasSurface=self.canvas.canvas)
        self.loadButton = PygameButton("load", x, y+20+5, w=60, h=20, onclick=self.load, canvasSurface=self.canvas.canvas)
            

    def save(self):
        print "save() called"
        # save in custom format
        '''
        Text file:
        --------------------------------------
        <savefile identifier>
        <canvas attributes>
        <color arrays, space separated>
        '''
        realPixieSide = self.PIXIESIDE + self.GAP
        for y in range(5, realPixieSide): #(CANVASSIDE):
            for x in range(5, realPixieSide): #(CANVASSIDE - MARGIN):
                print self.canvas.get_color(x+5, y+5),                                 
            print ""            
        

    def load(self):
        # load file and draw on canvas
        pass      

        
    def onMouseClick(self, eventObj):
        self.saveButton.onMouseClick(eventObj)
        self.loadButton.onMouseClick(eventObj)
    
    

