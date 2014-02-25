#!/usr/bin/env python
# Author: Rahul Anand
# This module provides Export as image feature for Pixel Canvas

##########################################################################################

from libs.PygameButton import PygameButton
import pygame

hasTkGui = False
try:
    from Tkinter import Tk
    from tkFileDialog import asksaveasfilename
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    hasTkGui = True
except:
    pass
    
    
class ExportImage():    

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
        self.exportButton = PygameButton("export", x, y, w=60, h=20, onclick=self.export, canvasSurface=self.canvas.canvas)
        self.canvas.freeMarginY += 20 + 20
            

    def export(self):
        # export canvas as image   
        filename = "pixel_canvas.png"                 
        try:
            if hasTkGui:
                filename = asksaveasfilename(defaultextension=".png", filetypes=[("PNG", ".png")], initialfile="pixel_canvas.png")
            print "Image exported!"
        except:
            print "Error in exporting image"
            return
        exportSurface = pygame.Surface((self.CANVASSIDE-self.MARGIN, self.CANVASSIDE))
        exportSurface.blit(self.canvas.canvas, (0,0))
        pygame.image.save(exportSurface, filename)

        
    def onMouseClick(self, eventObj):
        if (eventObj.pos[0] < self.CANVASSIDE - self.MARGIN or eventObj.pos[1] < self.freeMarginY):
            return
        self.exportButton.onMouseClick(eventObj)
    
    

