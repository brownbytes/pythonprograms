#!/usr/bin/env python
# Author: Rahul Anand
# This module provides Save and Load features for Pixel Canvas, in custom data format

##########################################################################################

from libs.PygameButton import PygameButton
import pickle
import pygame

class SaveLoad():    

    def __init__(self, margin, canvasside, pixieside, gap, canvas):        
        self.MARGIN = margin
        self.CANVASSIDE = canvasside
        self.PIXIESIDE = pixieside
        self.GAP = gap
        self.canvas = canvas
        self.freeMarginY = self.canvas.freeMarginY
        x = self.CANVASSIDE - self.MARGIN + 10
        y = self.canvas.freeMarginY + 20
        # initialize interface buttons
        self.saveButton = PygameButton("save", x, y, w=60, h=20, onclick=self.save, canvasSurface=self.canvas.canvas)
        self.loadButton = PygameButton("load", x, y+20+5, w=60, h=20, onclick=self.load, canvasSurface=self.canvas.canvas)
        self.canvas.freeMarginY += 20 + 20 + 5 + 20
            

    def save(self):
        # save in custom format        
        realPixieSide = self.PIXIESIDE + self.GAP        
        y = 0
        pc = []
        while y < self.CANVASSIDE:
            x = 0
            while x < (self.CANVASSIDE - self.MARGIN):
                pc.append(self.canvas.canvas.get_at((x, y)))
                x += realPixieSide                
            y += realPixieSide   
        try:
            pickle.dump( pc, open("save.pc", "wb") )
            print "Canvas saved!"
        except:
            print "Error in saving the canvas"
        

    def load(self):
        # load file and draw on canvas
        try:
            pc = pickle.load( open("save.pc", "rb") )  
            print "Save file loaded!"
        except:
            print "Error in loading save file"
            return
        realPixieSide = self.PIXIESIDE + self.GAP        
        y = 0
        while y < self.CANVASSIDE:
            x = 0
            while x < (self.CANVASSIDE - self.MARGIN):
                pygame.draw.rect(self.canvas.canvas, pc.pop(0), (x, y, self.PIXIESIDE, self.PIXIESIDE))
                x += realPixieSide                
            y += realPixieSide

        
    def onMouseClick(self, eventObj):
        if (eventObj.pos[0] < self.CANVASSIDE - self.MARGIN or eventObj.pos[1] < self.freeMarginY):
            return
        self.saveButton.onMouseClick(eventObj)
        self.loadButton.onMouseClick(eventObj)
    
    

